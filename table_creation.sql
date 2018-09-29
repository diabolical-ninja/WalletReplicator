"""
Title:  Record Table Creation
Desc:   Script to create the table for logging
Author: Yassin Eltahir
Date:   2018-09-29
"""

CREATE TABLE finance.wallet (
    transaction_time timestamp,
    category VARCHAR(255),
    amount NUMERIC(2),
    notes VARCHAR,
    transaction_id UUID
)