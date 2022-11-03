# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 17:17:41 2022

@author: greenuser
"""
#pyinstalle --onefile start_hash.py

#import os
#import sys
import pandas as pd
import base64
import hmac
import hashlib


def hash_vars(value_to_encode):

    # Extraer las cadenas de un fichero encriptado?
    FR = hmac.new(base64.b64decode("QW50cmFjaXRh"),
                  msg=bytes(value_to_encode.encode()),
                  digestmod=hashlib.sha256).hexdigest()

    SR = hmac.new(base64.b64decode("U1VNTUExMTI="),
                  msg=bytes(FR.encode()),
                  digestmod=hashlib.sha256).hexdigest()

    return SR


def hash_flow():

    # Dar a elegir entre CIPA, DNI o Ambas
    vars_to_encode = ["CIPA"]

    # Dar a elegir el nombre del fichero0 
    df = pd.read_excel("DATA.xlsx", dtype = "str" )
    df.columns = df.columns.str.upper()

    vars_hash = [i + "_HASH" for i in vars_to_encode]
    
    for i,v in enumerate(vars_to_encode):
        df[vars_hash[i]] = df[v].apply(lambda x: hash_vars(str(x)))

    return df


if __name__ == "__main__":

    df = hash_flow()
    df.to_excel("DATA_HASH.xlsx", index=False, header=True)
