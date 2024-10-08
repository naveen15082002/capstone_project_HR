import os
import pickle
from django.conf import settings
from django.shortcuts import render
import warnings

model_path=os.path.join(settings.BASE_DIR,'predictapp/model.pkl')
with open(model_path,'rb') as model_file:
    model=pickle.load(model_file)

def predict_view(request):
    warnings.filterwarnings('ignore')
    if request.method=='POST':
        DOJ=request.POST.get('DOJ')
        DOJ_value= 1 if DOJ == 'yes' else 0
        duration=request.POST.get('duration')
        notice=request.POST.get('notice')
        OB=request.POST.get('OB')
        if OB=='E0':
            OB_value=0
        elif OB=='E1':
            OB_value=1
        elif OB=='E2':
            OB_value=2
        else:
            OB_value=3
        percentdiff=float(request.POST.get('CTC'))
        JB=request.POST.get('JB')
        JB_value= 1 if JB == 'yes' else 0
        CRA=request.POST.get('CRA')
        CRA_value= 1 if CRA == 'yes' else 0
        CS=request.POST.get('CS')
        if CS=='A':
            CS_value=0
        elif CS=='D':
            CS_value=1
        elif CS=='E':
            CS_value=2
        exp=request.POST.get('exp')
        LOB=request.POST.get('LOB')
    
        if None in [DOJ_value,duration,notice,OB_value,percentdiff,JB_value,CRA_value,CS_value,exp,LOB]:
            return render(request, 'predictapp/predict.html', {'error': 'All fields are required.'})

        # Convert to float and make prediction
        try:
            prediction = model.predict([[int(DOJ_value),int(duration),int(notice),int(OB_value),float(percentdiff),int(JB_value),int(CRA_value),int(CS_value),int(exp),int(LOB)]])
        except ValueError as e:
            return render(request, 'predictapp/predict.html', {'Error': 'Invalid input. Please ensure all inputs are numbers.'})

        return render(request, 'predictapp/result.html', {'prediction': prediction[0]})

    return render(request, 'predictapp/predict.html')