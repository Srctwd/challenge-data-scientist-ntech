#Endpoint for performance calculations.
from fastapi import APIRouter, Request
import pandas as pd
import numpy as np
import pickle
import sklearn
import os

router = APIRouter(prefix="/performance")

@router.post("")
async def performance(records: Request):
    data = await records.json()

    #DataFrame
    df = pd.DataFrame(data)
    df = df.replace(np.nan, None)
    X_test = df.drop(["REF_DATE", "TARGET"], axis=1)
    y_test = df["TARGET"]

    #Volumetry
    volumetry = df["REF_DATE"].str[:7].value_counts().to_dict()

    #Model
    f = open(os.path.abspath(__file__ + 4 * '/..')+"/model.pkl", "rb")
    model = pickle.load(f)
    y_pred = model.predict(X_test)
    AUC = sklearn.metrics.roc_auc_score(y_test, y_pred)
    accuracy = sklearn.metrics.accuracy_score(y_test, y_pred)
    response = str([volumetry, AUC, accuracy])

    return response
