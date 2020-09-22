import pandas as pd
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import  LinearRegression
import joblib

mydata=pd.read_csv(r"C:\Users\Aditya\Desktop\lockdown ML\insurance.csv")
x=mydata.iloc[:,[0,1,2,3,4,5]].values
y=mydata.iloc[:,6].values
lab=LabelEncoder()


x[:,1]=lab.fit_transform(x[:,1])
x[:,4]=lab.fit_transform(x[:,4])


ct=ColumnTransformer(transformers=[('on',OneHotEncoder(),[5])],remainder="passthrough")
x=ct.fit_transform(x)



x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=1)

mymodel=LinearRegression()
mymodel.fit(x_train,y_train)
print(x_test[0,:])
print(y_test[0])
joblib.dump(mymodel,'model.pkl')
