from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load CSV
df = pd.read_csv("hospital_records.csv")

# Home Page
@app.route('/')

def home():
    return render_template("index.html")

# Search Patient
@app.route('/search', methods=['POST'])

def search():

    search_value = request.form['search'].lower()

    result = df[
        (df['Name'].str.lower().str.contains(search_value)) |
        (df['Disease'].str.lower().str.contains(search_value))
    ]

    patients = result.to_dict(orient='records')

    return render_template(
        "index.html",
        patients=patients
    )

if __name__ == '__main__':
    app.run(debug=True)