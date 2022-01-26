from flask import Flask, url_for
from flask import render_template
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/')
def read():
    patient_tb = pd.read_csv("./data/patient_tb.csv")
    #print(patient_tb.head(5))
    #print(patient_tb.info())
    #print(patient_tb.dtypes)

    #print(patient_tb)

    duplicates = patient_tb.duplicated(subset=['MostRecentTestDate'])
    #print(duplicates)

    #print(duplicates.value_counts())
    patient_tb = patient_tb.drop_duplicates(subset=['MostRecentTestDate'])
    #print(patient_tb)
    patient_tb.to_csv("patient_tb_updated.csv")

if __name__ == "__main__":
    app.run()
