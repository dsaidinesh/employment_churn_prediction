from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)



with open('pipeline.pkl', 'rb') as f:
    pipeline = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    satisfaction_level = float(request.form['satisfaction_level'])
    last_evaluation = float(request.form['last_evaluation'])
    number_project = int(request.form['number_project'])
    average_montly_hours = int(request.form['average_montly_hours'])
    time_spend_company = int(request.form['time_spend_company'])
    work_accident = int(request.form['work_accident'])
    promotion_last_5years = int(request.form['promotion_last_5years'])
    departments = request.form['departments']
    salary = request.form['salary']

    # Create DataFrame for prediction
    sample = pd.DataFrame({
        'satisfaction_level': [satisfaction_level],
        'last_evaluation': [last_evaluation],
        'number_project': [number_project],
        'average_montly_hours': [average_montly_hours],
        'time_spend_company': [time_spend_company],
        'Work_accident': [work_accident],
        'promotion_last_5years': [promotion_last_5years],
        'departments': [departments],
        'salary': [salary]
    })

    result = pipeline.predict(sample)

    if result == 1:
        prediction = "An employee may leave the organization."
    else:
        prediction = "An employee may stay with the organization."

    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
