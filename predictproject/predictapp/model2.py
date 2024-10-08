import pandas as pd
import pickle

dataset=pd.read_csv(r'C:\HR Prediction\predictproject\predictapp\HR analysis.csv')
x=dataset.iloc[:,:-1]
y=dataset.iloc[:,-1:]

from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier(max_depth=6, n_estimators=50, random_state=45)

rf_model=rf.fit(x,y)

pickle.dump(rf_model,open('model.pkl','wb'))

model=pickle.load(open('model.pkl','rb'))
print(model.predict(x.iloc[0,:].values.reshape(1,-1)))