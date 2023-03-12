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
    X_train = df.drop(["REF_DATE", "TARGET"], axis=1)
    y_train = df["TARGET"]

    #Volumetry
    volumetry = df["REF_DATE"].str[:7].value_counts().to_dict()

    #Model
    f = open(os.path.abspath(__file__ + 4 * '/..')+"/model.pkl", "rb")
    model = pickle.load(f)
    score = model.predict(X_train)
    fpr, tpr, thresholds = sklearn.metrics.roc_curve(y_train, score)
    response = str([fpr, tpr, thresholds, volumetry])

    return response
