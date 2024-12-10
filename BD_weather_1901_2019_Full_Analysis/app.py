from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model and scaler
model = joblib.load('rainfall_model.pkl')
scaler = joblib.load('scaler.pkl')

# Define the feature columns used during training
feature_columns = [
    'Year', 'Temperature',  # Continuous features
    # One-hot encoded months (ensure these match training data)
    'Month_2', 'Month_3', 'Month_4', 'Month_5', 'Month_6', 'Month_7',
    'Month_8', 'Month_9', 'Month_10', 'Month_11', 'Month_12'
]

@app.route('/')
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    year = int(request.form.get('Year'))
    month = int(request.form.get('Month'))
    temperature = float(request.form.get('Temperature'))

    # Prepare the input data
    input_data = pd.DataFrame({
        'Year': [year],
        'Month': [month],
        'Temperature': [temperature]
    })

    # One-hot encode and align with training data
    input_data = pd.get_dummies(input_data, columns=['Month'], drop_first=True)
    input_data = input_data.reindex(columns=feature_columns, fill_value=0)

    # Scale the input data
    input_data_scaled = scaler.transform(input_data)

    # Make the prediction
    predicted_rainfall = model.predict(input_data_scaled)[0]

    # Render the template with the prediction
    return render_template(
        'index.html',
        prediction=round(predicted_rainfall, 2),
        year=year,
        month=month,
        temperature=temperature
    )

if __name__ == '__main__':
    app.run(debug=True)
