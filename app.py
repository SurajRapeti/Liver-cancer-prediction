#import flask  # type: ignore
from flask import Flask,render_template,request # type: ignore
import numpy as nu  # type: ignore
import pandas as pa  # type: ignore
import pickle  

app = Flask(__name__)
model = pickle.load(open('liver.pkl','rb'))

@app.route("/")
def test():
    return render_template("liver.html")

@app.route("/predict", methods=['POST','GET'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_values = [nu.array(input_features)]
    print(input_features)
    
    features_names = ['Age','Gender','Total_Bilirubin','Direct_Bilirubin','Alkaline_Phosphotase','Alamine_Aminotransferase',
                      'Aspartate_Aminotransferase','Total_Protiens','Albumin','Albumin_and_Globulin_Ratio']
    
    df = pa.DataFrame(features_values)
    output = None
    output = model.predict(df)
    print(output)
    return render_template("predict.html", output = output)

if __name__=='__main__':
   app.run(debug=True)

#female=0  male=1