"""
Title:  Backup Budget Bakers Wallet Info
Desc:   A script to source retrieve BudgetBakers Wallet info & save them to a DB for future use
Author: Yassin Eltahir
Date:   2018-09-29
"""

#%%
import BudgetBakers as bb
import pyodbc
import yaml
import pandas as pd
from sqlalchemy import create_engine
import psycopg2 
import io


# Load up the config
conf = yaml.load(open('conf.yaml','r'))

# Instantiate & authenticate wallet object to retrieve transation history
wallet = bb.BudgetBakers()
wallet.token = conf['auth']['token']
wallet.user = conf['auth']['user']

# Create DB Connection
engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(
    conf['db']['username'],
    conf['db']['password'],
    conf['db']['server'],
    conf['db']['port'],
    conf['db']['dbname']
))
destination = 'finance.wallet'



#%%
# Get Existing Records
qry = "SELECT * FROM {}".format(destination)
df_existing = pd.read_sql(con = engine, sql = qry)


#%%
# Source both user accounts & category mappings
user_categories_df = wallet.category_collection(DataFrame=True)
user_records_df = wallet.record_collection(DataFrame=True)

# Clean up the data to it contains only the items of interest
df = pd.merge(user_records_df, user_categories_df, left_on = "categoryId", right_on = "id")
df = df[['date','name','refAmount','note','id_x']]
df.rename({
            'date':'transaction_time',
            'name':'category',
            'note': 'notes',
            'refAmount':'amount',
            'id_x':'transaction_id'}
        , inplace=True, axis="columns")
df.transaction_time = pd.to_datetime(df.transaction_time).astype(str)

#%%
# Upsert to get only the new records & apply records updates
df = pd.concat([df_existing[~df_existing.transaction_id.isin(df.transaction_id)], df], sort=False)


#%%
# Upload to DB
if df.shape[0] > 0:

    df.head(0).to_sql(destination, engine,if_exists='replace',index=False) #truncates the table
    conn = engine.raw_connection()
    cur = conn.cursor()
    output = io.StringIO()
    df.to_csv(output, sep='\t', header=False, index=False)
    output.seek(0)
    contents = output.getvalue()
    cur.copy_from(output, destination, null="") # null values become ''
    conn.commit()