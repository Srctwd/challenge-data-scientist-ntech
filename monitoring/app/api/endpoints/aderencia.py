"""Endpoint para cálculo de aderência."""
import os
from fastapi import APIRouter, Request
import pandas as pd
import numpy as np
import pickle
from scipy.stats import kstest

router = APIRouter(prefix="/aderencia")

@router.post("")
async def adherence(path: Request):
    data = await path.body()
    data = data.decode("utf-8")
    #Loading csv
    df = pd.read_csv(data, compression="gzip")
    df = df.replace(np.nan, None)
    X = df.drop(["REF_DATE"], axis=1)

    #Model
    f = open(os.path.abspath(__file__ + 4 * '/..')+"/model.pkl", "rb")
    model = pickle.load(f)
    y_pred = model.predict(X)
    df["TARGET"] = y_pred

    print(df.head())


    df_test = pd.read_csv("/home/srctwd/challenge-data-scientist-ntech/datasets/credit_01/test.gz", compression="gzip")
    print(kstest(df["TARGET"], df_test["TARGET"]))


    return 21


