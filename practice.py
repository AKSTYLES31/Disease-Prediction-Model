import numpy as np
import pandas as pd
import tkinter as tk
from sklearn import tree
from tkinter import ttk
from sklearn.metrics import accuracy_score

sym=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']

disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']


l2 = [0] * len(sym)

df = pd.read_csv("training.csv")
tr = pd.read_csv("testing.csv")

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

df.dropna(inplace=True)
tr.dropna(inplace=True)

X = df[sym]
y = df["prognosis"]
X_test = tr[sym]
y_test = tr["prognosis"]

clf3 = tree.DecisionTreeClassifier()
clf3 = clf3.fit(X, y)

def predict_disease():
    symptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get()]
    if all(symptoms):
        l2 = [0] * len(sym)
        for i, symptom in enumerate(symptoms):
            if symptom in sym:
                l2[sym.index(symptom)] = 1
        input_test = [l2]
        predicted = clf3.predict(input_test)[0]
        predicted = int(predicted)
        disease_name = disease[predicted]
        t1.delete("1.0", tk.END)
        t1.insert(tk.END, disease_name)
    else:
        t1.delete("1.0", tk.END)
        t1.insert(tk.END, "Please enter all symptoms")

# Create a function to update the symptoms list
def update_symptoms(event):
    selected_symptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get()]
    available_symptoms = [symptom for symptom in sym if symptom not in selected_symptoms]

    Symptom1['values'] = available_symptoms
    Symptom2['values'] = available_symptoms
    Symptom3['values'] = available_symptoms

# Create the main application window
root = tk.Tk()
root.title("Disease Prediction Model")

window_width = 600
window_height = 400
root.geometry(f"{window_width}x{window_height}")

# Create and configure Combobox widgets for symptoms
tk.Label(root, text="Symptom 1:").pack()
Symptom1 = ttk.Combobox(root, values=sym, width=30)
Symptom1.pack()

tk.Label(root, text="Symptom 2:").pack()
Symptom2 = ttk.Combobox(root, values=sym, width=30)
Symptom2.pack()

tk.Label(root, text="Symptom 3:").pack()
Symptom3 = ttk.Combobox(root, values=sym, width=30)
Symptom3.pack()

Symptom1.bind('<<ComboboxSelected>>', update_symptoms)
Symptom2.bind('<<ComboboxSelected>>', update_symptoms)
Symptom3.bind('<<ComboboxSelected>>', update_symptoms)

# Create a button to predict the disease
predict_button = tk.Button(root, text="Predict Disease", command=predict_disease)
predict_button.pack()

# Create a text box to display the result
t1 = tk.Text(root, height=3, width=30)
t1.pack()

root.mainloop()