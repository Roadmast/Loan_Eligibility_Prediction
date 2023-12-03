from flask import Flask,render_template,request
import pickle
import numpy as np

with open("Loan_Prediction.pkl",'rb') as f:
    model = pickle.load(f)
    

#create an object instance
app =Flask(__name__)

@app.route('/surya')
def check():
    return "S.V.Surya Narayana"

@app.route('/')#by default methods = ['GET']
def new():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    applicant_income=int(request.form['applicant_income'])
    coapplicant_income=int(request.form['coapplicant_income'])
    loan_amount=int(request.form['loan_amount'])
    loan_term=int(request.form['loan_term'])
    gender=int(request.form['gender'])
    married=int(request.form['married'])
    dependents=int(request.form['dependents'])
    education=int(request.form['education'])
    self_employed=int(request.form['self_employed'])
    credit_history=int(request.form['credit_history'])
    property_area=int(request.form['property_area'])

    input_data=np.array([[applicant_income,coapplicant_income,
                          loan_amount,loan_term,gender,married,dependents,
                          education,self_employed,credit_history,
                          property_area]])
    prediction_model=model.predict(input_data)[0]
    if prediction_model==1:
        prediction='Loan will be Approved'
    else:
        prediction='Loan is Rejected'
    return render_template("index.html",prediction=prediction)
    
    

app.run()
