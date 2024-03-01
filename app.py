from flask import Flask, render_template, request
import pickle
app = Flask(__name__)

model = pickle.load(open('MY_MODEL.pkl', "rb"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    form_data = request.form.to_dict()

    features = [int(form_data[attr]) for attr in form_data]

    prediction = model.predict([features])[0]

    return f'The predicted result is(CANCER:1 and NOT CANCER:0): {prediction}'

if __name__ == '__main__':
    app.run(debug=True)




























'''import pickle
import numpy as np
from flask import Flask , render_template , request

#load model
model = pickle.load(open('MY_MODEL.pkl', "rb"))

#load scaler
# scalerfile = 'scaler.save'
# scaler = pickle.load(open(scalerfile, 'rb'))


#flask consructor
app = Flask(__name__)

@app.route('/')

@app.route('/main_template',methods=["GET"])
def main_template():

    return render_template('index.html')

#get form data
@app.route('/predict',methods=['GET','POST'])
def predict():

    #checking request type
    str_req_type = request.method

    #convert string value into numeric value
    if request.method == str(str_req_type):

        if request.args.get('gender') == 'Male':
            gender = 0

        else:
            gender = 1
        age = request.args.get('age')
        smoking  = request.args.get('smoking')
        anxiety= request.args.get('anxity')
        peer_pressure= request.args.get('peer_pressure')
        chronic_disease= request.args.get('chronic_disease')
        fatigue= request.args.get('fatigue')
        allergy= request.args.get('allergy')
        wheezing= request.args.get('wheezing')
        alcohol_consuming= request.args.get('alcohol_consuming')
        coughing= request.args.get('coughing')
        shortness_breath= request.args.get('shortness_breath')
        swallowing_difficulty= request.args.get('swallowing_difficulty')
        chestpain= request.args.get('chestpain')
        #store form values into set
        values = [gender, age,smoking,anxiety,peer_pressure,chronic_disease,fatigue,allergy,wheezing,alcohol_consuming,coughing,shortness_breath,swallowing_difficulty,chestpain]

        #turn into array & reshape array for prediction
        input_array = np.asarray(values)
        input_array_reshape = input_array.reshape(1, -1)

        #sclae the inputed reshaped data
        #scaled_set = scaler.transform(input_array_reshape)

        # predict with inputed values
        predicted= model.predict(input_array_reshape)

        #display predicted valuesin result.html file
        return  render_template('result.html', predicted_value=predicted[0])
    else:
        return render_template('index.html')


if __name__ == '_main_':
    app.run(debug=True)'''