# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 20:35:54 2024

@author: User
"""
from flask import Flask,request, jsonify, render_template, url_for, redirect
import joblib
import numpy as np
import pandas as pd


model = joblib.load('model/9_diseases_logistic_regression_model.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Key_objectives')
def Key_objectives():
    return render_template('Key_objectives.html')

@app.route('/the_9_diseases')
def the_9_diseases():
    return render_template('the_9_diseases.html')

@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/start_diagnosis', methods=['GET','POST'])
def start_diagnosis():
    
  try:
   if request.method == 'POST':  
    age = request.form.get('age')#dans le formulaire HTML
    if age and age.strip():
        age = int(age)
    else:
        return "Erreur: le champ âge est requis.", 400
    
    name = request.form.get('name')
    print(f"Age:{age} et type_age={type(age)} ")
    ethnicity = [int(request.form.get(ethnicity, 0))for ethnicity in ['Asian',
       'Caucasian', 'Hispanic', 'Other']]
    print(f"ethnicity:{ethnicity} et type_ethnicity={type(ethnicity)}", ethnicity)
    
    #recuperer les symptomes dans le checkbox
    symptoms = []
    symptom_names = ['  frequent urination', ' abdominal pain', ' bloating',
       ' blurred vision', ' chest pain', ' chest tightness', ' chills',
       ' chronic cough', ' coughing', ' dizziness', ' fatigue', ' fever',
       ' frequent urination', ' headache', ' healthy', ' increased thirst',
       ' irregular heartbeat', ' muscle pain', ' nausea', ' night sweats',
       ' no symptoms', ' nosebleeds', ' rash', ' shortness of breath',
       ' stomach pain', ' swollen lymph nodes', ' vomiting', ' weakness',
       ' weight loss', ' wheezing']
    
    for symptom in symptom_names:
        symptoms.append(1 if request.form.get(symptom, 'no')=='yes' else 0)
    #print(f"symptoms:{symptoms} et type_symptoms={type(symptoms)}")
       
    input_features = np.array(symptoms + [age] + ethnicity).reshape(1, -1)

    #Prédiction
    prediction = model.predict(input_features)[0]
    probability = model.predict_proba(input_features)[0].max()*100
    #print("Prediction:", prediction)
    return render_template('Answer.html', name=name, prediction=prediction, probability=round(probability, 2))
    
   return render_template('start_diagnosis.html')

  except Exception as e:
       print(f"Erreur lors du traitement de données: {e}")
       return "Une erreur s'est produite lors de la prédiction.", 500
  except ValueError as ve:
       print(f"Erreur de conversion de données: {ve}")
       return "Données non valides.", 400
   
#execution de l'application Flask
if __name__ == '__main__':
    app.run(debug=True)
app.debug = True

#     print(f"erreur lors du traitement des données: {e}")
#     return "Une erreur s'est produite"