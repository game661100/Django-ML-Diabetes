from django.shortcuts import render
from tensorflow.keras.models import load_model
import numpy 

#Load your model here
model = load_model("diabetes_trained_model.h5")

# Create your views here.
def homepage(request):

    if request.method == 'POST':   
        try:   
            preg = float(request.POST['Pregnancies'])
            glu = float(request.POST['Glucose'])
            blood = float(request.POST['BloodPressure'])
            skin = float(request.POST['SkinThickness'])
            insulin = float(request.POST['Insulin'])
            bmi = float(request.POST['BMI'])
            dped = float(request.POST['DiabetesPedigreeFunction'])
            age = float(request.POST['Age'])

            inp = numpy.array([ [preg, glu, blood, skin, insulin, bmi, dped, age] ])
            prediction = model.predict(x=inp)
            percent_diabetes = round(prediction[0][0])    
            result = ""
            if percent_diabetes == 1:
                result = "You have high risk of having diabetes"
            else:
                result = "You have no risk of having diabetes"
            context = {
                'result' : result
            }
            return render(request, "index.html", context)
 
        except:
            context = {
                'result' : "An error has occured"
            }
            return render(request, "index.html", context)
 
    return render(request, "index.html")