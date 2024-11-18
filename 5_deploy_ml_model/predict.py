import pickle

from flask import Flask
from flask import request # to modify the request data type
from flask import jsonify # to convert the result to a json object

    
model_file = 'model_C=1.0.bin' 

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('churn')

@app.route('/predict', methods=['POST'])

def predict():
    customer = request.get_json() # ths will convert the request to a python dictionary
    
    X  = dv.transform([customer])
    Y_pred = model.predict_proba(X)[0, 1]
    churn = Y_pred > 0.5

    result = {
        'churn_probability': float(Y_pred),
        'churn': bool(churn)
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696) # This is our local server
 