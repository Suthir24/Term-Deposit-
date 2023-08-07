from django.shortcuts import render
import joblib

def index(request):
    return render(request, 'index.html')

def predict(request):
    if request.method == 'POST':
        age = int(request.POST['age'])
        job = int(request.POST['job'])
        marital = int(request.POST['marital'])
        education = int(request.POST['education'])
        default = int(request.POST['default'])
        balance = int(request.POST['balance'])
        housing = int(request.POST['housing'])
        loan = int(request.POST['loan'])
        contact = int(request.POST['contact'])
        day = int(request.POST['day'])
        month = int(request.POST['month'])
        duration = int(request.POST['duration'])
        campaign = int(request.POST['campaign'])
        poutcome = int(request.POST['poutcome'])

        # Load the trained model
        model = joblib.load('/Users/suka/caps/savedModels/subscriber_main_model.joblib')

        # Make prediction using the loaded model
        input_data = [[age, job, marital, education, default, balance, housing, loan, contact, day, month, duration, campaign, poutcome]]
        prediction = model.predict(input_data)

        return render(request, 'result.html', {'prediction': prediction[0]})
