# %%
import pandas as pd
import seaborn as sns
import numpy as np
import streamlit as st
# %% [markdown]
# Data yuklenir
# 
print(st.title("Titanik faciəsindən sağ çıxa bilərdinizmi?"))


#name = st.text_input("Adınız:")
age = st.slider("Yaşınız", 1, 100,1)
sibling = st.slider("Sizinlə birlikdə olan ailə üzvlərinizin sayı",1,10,1)
gender = st.selectbox("Cins", options = ["Kişi","Qadın"] )
p_class = st.selectbox("Sərnişin sinfi",options=['Birinci sinif' , 'İkinci sinif' , 'Üçüncü sinif'])
# %%
data = pd.read_csv("train.csv")

# %%








# %%


# %%
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan,strategy="mean")


# %%


# %%
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

data["Sex"] = le.fit_transform(data["Sex"])

# %%
#data["Age"] = data["Age"].dropna(inplace=True)

# %%
data.drop("Cabin",axis=1,inplace=True)

# %%
data["Embarked"] = le.fit_transform(data["Embarked"])

# %%
data.drop(["Name","Ticket"],inplace=True,axis=1)

# %%
data["Age"].dropna(axis=0,inplace=True)

# %%
data.dropna(inplace=True)

# %%
data.drop("PassengerId",axis=1,inplace=True)

# %%


# %%
x =  data.drop(["Survived","Parch","Fare","Embarked"],axis=1)
y = data["Survived"]

# %%
from sklearn.model_selection import train_test_split


# %%
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=101)


# %%
from sklearn.linear_model import LogisticRegression

LR = LogisticRegression()

LR.fit(X_train,y_train)

# %%
#

# %%
gender = 1 if gender =="Kişi" else 0

if p_class =="Birinci sinif":
    p_class = 1
elif p_class =="İkinci sinif":
    p_class = 2
else:
    p_class = 3

input_data = {
    'Pclass':p_class,"Sex":gender,"Age":age,"SibSp":sibling
}
df = pd.DataFrame(data=input_data,index=[0])

prediction = LR.predict(df)
predict_probability = LR.predict_proba(df)
if prediction[0] == 1:
	st.subheader('{} % ehtimalla sağ qalardınız.'.format(round(predict_probability[0][1]*100 , 3)))
else:
	st.subheader('{} % ehtimalla ölərdiniz'.format(round(predict_probability[0][0]*100 , 3)))
# %%
from sklearn.metrics import classification_report
#print(classification_report(y_test,prediction))

# %%


# %%



