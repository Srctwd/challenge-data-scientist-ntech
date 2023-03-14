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
    #Loading csv

    try:
        df = pd.read_csv(data, compression="gzip")
    except:
        error = "Invalid path"
        return error
    
    df = df.fillna(np.nan)
    df = df.drop(["REF_DATE"], axis=1)
    if "TARGET" in df:
        df = df.drop(["TARGET"], axis=1)

    




    #Model
    f = open(os.path.abspath(__file__ + 4 * '/..')+"/model.pkl", "rb")
    model = pickle.load(f)
 
    try:
        y_pred = model.predict_proba(df)[:,1]
    except Exception as error:
        err_message = re.search("unknown categories \[.*\].*column \d*", str(error))
        if err_message:
            value_name = (str(err_message.string).split("\'")[1].split("\'")[0])
            df.iloc[:,119] = df.iloc[:,119].replace(value_name, np.nan) #hardcoding column number with unkown categories for now.

        else:
            print(error)


    y_pred = model.predict_proba(df)[:,1]
    df["TARGET"] = y_pred

    df_test = pd.read_csv("/home/srctwd/challenge-data-scientist-ntech/datasets/credit_01/test.gz", compression="gzip")
    X_test = df_test.drop(["REF_DATE", "TARGET"], axis=1)
    y_test = model.predict_proba(X_test)[:,1]


    return str(kstest(y_test, y_pred))
#    df_test = pd.read_csv("/home/srctwd/challenge-data-scientist-ntech/datasets/credit_01/test.gz", compression="gzip")
#    gz = df_test["TARGET"].to_list()
#    kstest_result = kstest(y_pred, gz)
#    print(y_pred)
#    print(kstest_result)

    


    return str(kstest_result)