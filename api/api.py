import joblib
import pandas as pd 
from  flask import Flask,jsonify,request
import os

app=Flask(__name__)
bas_dir=os.path.dirname(os.path.abspath(__file__))
pr_root=os.path.dirname(bas_dir)
model_path=os.path.join(pr_root,"model","rf_model.pkl")
feat_path=os.path.join(pr_root,'model','feature.pkl')

def preprocessing(data,feat):
    df=pd.DataFrame([data])

    df=pd.get_dummies(df)

    for col in feat:
        if col not in df.columns:
            df[col]=0
    
    df=df[feat]
    return df
model=joblib.load(model_path)
feat=joblib.load(feat_path)

@app.route('/')
def home():
    return "Medical Cost Prediction API running! "

@app.route("/predict",methods=['POST'])
def predict():
    data=request.get_json()

    input_df=preprocessing(data,feat)
    prediction=model.predict(input_df)

    return( jsonify({"Prediction": float(prediction[0])}))

if __name__=="__main__":
    app.run(debug=True)