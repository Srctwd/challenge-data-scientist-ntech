"""Endpoint para cálculo de aderência."""
import os
from fastapi import APIRouter, Request
import pandas as pd
import numpy as np
import pickle
from scipy.stats import kstest
import sklearn.preprocessing as pp
import re

router = APIRouter(prefix="/aderencia")

@router.post("")
async def adherence(path: Request):
    data = await path.body()
    data = data.decode("utf-8")
    print(data)
    #Loading csv
    df = pd.read_csv(data, compression="gzip")
    print(df.head)
    df = df.replace(np.nan, None)
    X = df.drop(["REF_DATE"], axis=1)
    if "TARGET" in df:
        X = X.drop(["TARGET"], axis=1)
    




    #Model
    f = open(os.path.abspath(__file__ + 4 * '/..')+"/model.pkl", "rb")
    model = pickle.load(f)
 
    try:
        y_pred = model.predict_proba(X)[:,1]
    except Exception as error:
        err_message = re.search("unknown categories \[.*\].*column \d*", str(error))
        if err_message:
            value_name = (str(err_message.string).split("\'")[1].split("\'")[0])
            print(value_name)
            X.iloc[:,119] = X.iloc[:,119].replace(value_name, np.nan) #hardcoding column number with unkown categories for now.

        else:
            print(error)

    y_pred = model.predict_proba(X)[:,1]

    print(y_pred)
    X["TARGET"] = y_pred

    df_test = pd.read_csv("/home/srctwd/challenge-data-scientist-ntech/datasets/credit_01/test.gz", compression="gzip")


    return str(kstest(X["TARGET"], df_test["TARGET"]))

    
"""     try:
        y_pred = model.predict(X)
    except Exception as error:
        x = re.search("unknown categories \[.*\].*column \d*", str(error))
        if x:
            value_name = (str(x.string).split("[")[1].split("]")[0])
            column_number = x.string.split(" ")[2]
            print(value_name)
            print(x.group().split(" ")[-1])
            for i in range(len(df)):
                if i == 78:
                    print(df.iloc[i].unique())
            df.drop(df.iloc(78))
          
    
           print(df.iloc[:,79].unique())
           df.iloc[:,79] = df.iloc[:,79].replace(value_name, np.nan)
            print(df.iloc[:,79].unique())
        else:
            print(error)
 """          





'''
 '''



'''
     i=119
    aux=True
    while aux:
        try:
            y_pred = model.predict(X)
            aux = False
            
        except Exception as error:
            if i>140:
                aux = False
            print(error)
            X.iloc[:,i] = X.iloc[:,i].replace("MUITO PROXIMO", np.nan)
            print(X.iloc[:,i].name)
            print(X.iloc[:,i].unique())
            i += 1
#            for j in X:
#                if len(X[j].unique()) == 5:
#                    print(X[j].name)
#                    print(X[j].unique())
'''