"""
Title:  BudgetBakers API
Desc:   Python Library for the BudgetBakers (Wallet) Rest API (http://docs.budgetbakersv30apiv1.apiary.io/#)
Author: Yassin Eltahir
"""

import requests
import pandas as pd


class BudgetBakers:
    '''
    BudgetBakers API: http://docs.budgetbakersv30apiv1.apiary.io/#
    
    Each instance must be provided:
        - X-Token: Rest Authentication Token from the App (Android)
        - X-Key:   Users Email Address
    '''
    
    def __init__(self):
        self.url = 'https://api.budgetbakers.com/api/v1/'
        self.token = None
        self.user = None
        
        
    #USER
    def check_email(self):
        '''
        Checks if a user exists
        '''
        
        url = self.url + 'user/exists/' + self.user
        
        headers = {
            'x-token': self.token
        }
        
        try:
            response = requests.request("GET", url, headers=headers)
            
            if response.status_code == 200:
                return True
            else:
                return False
            
        except Exception as ex:
            print( "Oh No! Something went wrong validating user...")
            print( ex)
    
    
    # ACCOUNT
    def accounts_collection(self, DataFrame = False):
        '''
        Get Users Accounts
        
        DataFrame: By default the JSON (dict) is returned. Option to return a Pandas DataFrame instead
        '''
    
        url = self.url + 'accounts'
        headers = {
            'x-token': self.token,
            'x-user': self.user
        }
        
        try:
            response = requests.request("GET", url, headers=headers)
            
            if DataFrame:
                return pd.DataFrame(response.json())
            else:
                return response.json()
            
        except Exception as ex:
            print( "Oh No! Something went wrong collecting your accounts...")
            print( ex)
            
    
    
    # CATEGORIES
    def category_collection(self, DataFrame = False):
        '''
        Get Users Category Collection
        
        DataFrame: By default the JSON (dict) is returned. Option to return a Pandas DataFrame instead
        '''
        
        url = self.url + 'categories'
        headers = {
            'x-token': self.token,
            'x-user': self.user
        }
        
        try:
            response = requests.request("GET", url, headers=headers)
            
            if DataFrame:
                return pd.DataFrame(response.json())
            else:
                return response.json()
            
        except Exception as ex:
            print( "Oh No! Something went wrong collecting your categories...")
            print( ex)
    
    
    # CURRENCY
    def currency_collection(self, DataFrame = False):
        '''
        Get Users Currencies
        
        DataFrame: By default the JSON (dict) is returned. Option to return a Pandas DataFrame instead
        '''
        
        url = self.url + "currencies"
        headers = {
            'x-token': self.token,
            'x-user': self.user
        }
        
        try:
            response = requests.request("GET", url, headers=headers)
            
            if DataFrame:
                return pd.DataFrame(response.json())
            else:
                return response.json()
            
        except Exception as ex:
            print( "Oh No! Something went wrong collecting your currencies...")
            print( ex)         
    
    
    # RECORDS
    def record_collection(self, DataFrame = False):
        '''
        Get Users Record Collection
        
        DataFrame: By default the JSON (dict) is returned. Option to return a Pandas DataFrame instead
        '''
        
        url = self.url + "records"
        headers = {
            'x-token': self.token,
            'x-user': self.user
        }
        
        try:
            response = requests.request("GET", url, headers=headers)
            
            if DataFrame:
                return pd.DataFrame(response.json())
            else:
                return response.json()
            
        except Exception as ex:
            print( "Oh No! Something went wrong collecting your records...")
            print( ex)
    
    
    
    # BALANCE
    def overall_balance(self):
        '''
        Gets the users overall balance
        '''
        
        url = self.url + 'balance'
        headers = {
            'x-token': self.token,
            'x-user': self.user
        }
    
        try:
            response = requests.request("GET", url, headers=headers)
            return response.json()
            
        except Exception as ex:
            print( "Oh No! Something went wrong getting your balance...")
            print( ex)
            
            
    def account_balance(self, account_id):
        '''
        Gets the users balance for a specific account
        '''
        
        url = self.url + 'balance/account/' + account_id
        headers = {
            'x-token': self.token,
            'x-user': self.user
        }
    
        try:
            response = requests.request("GET", url, headers=headers)
            return response.json()
            
        except Exception as ex:
            print( "Oh No! Something went wrong getting your account balance...")
            print( ex)