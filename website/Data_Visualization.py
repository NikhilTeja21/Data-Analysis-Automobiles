import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import streamlit as st

#setting the name and icon of web app 
st.set_page_config(page_title="Data Visualization",page_icon=":chart_with_downwards_trend:",layout="wide")

#setting title in web app
st.title('Data Analysis of Automotive Industry')

# reading .csv file
df=pd.read_csv("cars_engage_2022.csv")
data=["Make","Model","Variant","Ex-Showroom_Price","Displacement","Cylinder_Configuration","Fuel_Tank_Capacity","Fuel_Type","Body_Type","ARAI_Certified_Mileage","Gears","Power","Seating_Capacity","Type"]
df=df[data]

#dealing with missing data
df.dropna(subset="Make",inplace=True)
df.dropna(subset="Displacement",inplace=True)
df.dropna(subset="Cylinder_Configuration",inplace=True)
df.dropna(subset="Fuel_Tank_Capacity",inplace=True)
df.dropna(subset="Fuel_Type",inplace=True)
df.dropna(subset="Body_Type",inplace=True)
df.dropna(subset="ARAI_Certified_Mileage",inplace=True)
df.dropna(subset="Gears",inplace=True)
df.dropna(subset="Seating_Capacity",inplace=True)
df.dropna(subset="Type",inplace=True)

#changing data_type
df["Ex-Showroom_Price"]=df["Ex-Showroom_Price"].replace(["Rs.",","],"",regex=True).astype(int)
df["Displacement"]=df["Displacement"].replace("cc","",regex=True).astype(int)
df["Fuel_Tank_Capacity"]=df["Fuel_Tank_Capacity"].replace("litres","",regex=True).astype(float)
df["ARAI_Certified_Mileage"]=df["ARAI_Certified_Mileage"].replace(["9.8-10.0","km/litre"],["9.9",""],regex=True).astype(float)
df["Gears"] = df["Gears"].replace("Dual Clutch","",regex=True).astype(int)
df["Seating_Capacity"]=df["Seating_Capacity"].astype(int)
HP = df.Power.str.extract(r'(\d{1,4}).*').astype(int) * 0.98632
HP = HP.apply(lambda x: round(x,2))
df.Power = HP

#displaying dataframe on web app
with st.container():
    st.header('Data Frame')
    st.write(df)

#setting font size to write on web app
st.markdown("""<style>.font {font-size:25px !important;}</style>""", unsafe_allow_html=True)

#plotting graph for most poplar specification
fig1,axes=plt.subplots(2,2,figsize=(10,7))
plt.tight_layout(pad=4)

#most poplar Cylinder_Configuration
sns.set_style('darkgrid')
sns.countplot(x="Cylinder_Configuration",data=df,ax=axes[0,0])
axes[0,0].set_title("Most popular Cylinder Configuration",fontsize=15)
axes[0,0].set_xlabel("Cylinder Configuration",fontsize=11)
axes[0,0].set_ylabel("Count",fontsize=11)

#most poplar Fuel_Type
sns.set_style('darkgrid')
sns.countplot(x="Fuel_Type",data=df,ax=axes[0,1])
axes[0,1].set_title("Most popular Fuel Type",fontsize=15)
axes[0,1].set_xlabel("Fuel Type",fontsize=11)
axes[0,1].set_ylabel("Count",fontsize=11)

#most poplar Number Of Gears
sns.set_style('darkgrid')
sns.countplot(x="Gears",data=df,ax=axes[1,0])
axes[1,0].set_title("Preferable Number Of Gears",fontsize=15)
axes[1,0].set_xlabel("Number Of Gears",fontsize=11)
axes[1,0].set_ylabel("Count",fontsize=11)

#most poplar Number Of Seats
sns.set_style('darkgrid')
sns.countplot(x="Seating_Capacity",data=df,ax=axes[1,1])
axes[1,1].set_title("Preferable Seating Capacity",fontsize=15)
axes[1,1].set_xlabel("Number of Seats",fontsize=11)
axes[1,1].set_ylabel("Count",fontsize=11)

#displaying most popular car specification on web app
with st.container():
    st.write("---")
    st.header('Most Popular Car Specification')
    st.write("")
    fig1
    st.write("")
    st.header('Conclusion')
    st.markdown('<p class="font">From the above graphs we can conclude that most of the customers prefer car with <b>In-line</b> Cylindrical Configuration, <b>Petrol</b> Fuel type , 5 gears and 5 seats</p>', unsafe_allow_html=True)

    #Subplots of piecharts
fig2,axes=plt.subplots(1,2,figsize=(15,11))
plt.tight_layout(pad=4)

#plot Type vs count
type_list=df["Type"].tolist()
type_dict=dict((type_count, type_list.count(type_count)) for type_count in set(type_list))

dict_keys=list(type_dict.keys())
dict_values=list(type_dict.values())

sns.set_style('darkgrid')
color=sns.color_palette("Paired")
axes[0].set_title("Most Popular Type of Car",fontsize=30)
axes[0].pie(dict_values,colors=color, startangle=60)
axes[0].legend(dict_keys)

#plot Body_Type vs count
b_type_list=df["Body_Type"].tolist()
b_type_dict=dict((b_type_count,b_type_list.count(b_type_count)) for b_type_count in set(b_type_list))

b_dict_keys=list(b_type_dict.keys())
b_dict_values=list(b_type_dict.values())

sns.set_style('darkgrid')
color=sns.color_palette("Paired")
axes[1].set_title("Most Popular Body Type",fontsize=30)
axes[1].pie(b_dict_values,colors=color, startangle=30)
axes[1].legend(b_dict_keys)

#displaying most popular car type and body type on web app
with st.container():
    st.write("---")
    st.header('Most Popular Car Type')
    st.write("")
    fig2
    st.write("")
    st.header('Conclusion')
    st.markdown('<p class="font">From the above pie charts we can conclude that most of the customers prefer a <b>Manual</b> car and <b>SUV</b> body type</p>', unsafe_allow_html=True)

with st.container():
    st.write("---")
    st.markdown('<p class="font">Customers data such as prior product responses, customer feedback forms, competitor product successes, and so on, is collected through a variety of channels, including physical retail, e-commerce, and social media</p>', unsafe_allow_html=True)
    st.markdown('<p class="font">Businesses and manufacturing industries can gain insights into customer behaviour by using data analysis tools such as prediction analysis, regression analysis, and budgeting to create comprehensive customer profiles from this data, allowing them to provide a more personalised experience and become more successful and popular</p>', unsafe_allow_html=True)
    st.markdown('<p class="font">In the case of the current dataset under analysis, a <b>Manual Car</b> with <b>In-line Cylindrical Configuration</b>, <b>5 seats</b> with an <b>SUV Body Type</b> is the demand of the market.</p>', unsafe_allow_html=True)
    
#plotting graph Fuel Tank Capacity vs Power
fig3=plt.figure(figsize=(10,6))
sns.regplot(x="Fuel_Tank_Capacity", y="Power", data=df)
plt.title("Fuel Tank Capacity vs Power",fontsize=22)
plt.xlabel("Fuel Tank Capacity",fontsize=16)
plt.ylabel("Power",fontsize=16)
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

#displaying power vs fuel capacity on web app
with st.container():
    st.write("---")
    st.header('Power vs Fuel Tank Capacity')
    st.write("")
    fig3
    st.write("")
    st.header('Conclusion')
    st.markdown('<p class="font">The above graph helps manufacturer to set up appropriate correlation between power of vehicle and its fuel tank</p>', unsafe_allow_html=True)
    st.markdown('<p class="font">It also helps manufacturer to estimate raw material usage, full tank size, costing, maintaining at a cost that makes the vehicle sellable, calls for improvement of automotive technology such that higher power can be reached with less amount of fuel expenditure for the customer.</p>', unsafe_allow_html=True)

#model development
#Simple Regression Model
x=np.array(df["Power"]).reshape(-1,1)
y=np.array(df["Ex-Showroom_Price"]).reshape(-1,1)

x_train, x_test ,y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 100)

slr = LinearRegression()  
slr.fit(x_train, y_train)

accuracy_slr=slr.score(x_test,y_test)
y_pred_slr= slr.predict(x_test)

y_test=y_test.ravel()
y_pred_slr=y_pred_slr.ravel()

#plot actual and predicted values
fig4,ax=plt.subplots(figsize=(10,6))
ax.scatter(x_test,y_test)
ax.plot(x_test, y_pred_slr, 'red')
ax.set_xlabel("Power",fontsize=16)
ax.set_ylabel("Ex-Showroom Price",fontsize=16)
ax.legend(labels=["Sample data","Regression Model"])

#displaying simple reg model on web app
with st.container():
    st.write("---")
    st.header('Simple Linear Regression Model')
    st.write("")
    fig4
    st.write("")
    st.markdown('<p class="font">The accuracy of model is:</p>', unsafe_allow_html=True)
    st.write(accuracy_slr)
    st.header('Conclusion')
    st.markdown('<p class="font">From above observation we can conclude that this Model is <b>accurate</b> </p>', unsafe_allow_html=True)

#Multiple Regression Model
x=df[["Power","Fuel_Tank_Capacity"]].values.reshape(-1,2)
y=df["Ex-Showroom_Price"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 100)

mlr = LinearRegression()  
mlr.fit(x_train, y_train)

accuracy_mlr=mlr.score(x_test,y_test)
y_pred_mlr= mlr.predict(x_test)

X=x_test[:,0]
Y=x_test[:,1]
Z=y_test

#plot actual and predicted values
fig5=plt.figure(figsize=(10,6))
ax=fig5.add_subplot(111,projection='3d')
ax.scatter(X,Y,Z)
ax.scatter(X,Y,y_pred_mlr,c='r')
ax.set_xlabel("Power",fontsize=11)
ax.set_ylabel("Fuel Tank Capacity",fontsize=11)
ax.set_zlabel("Ex-Showroom Price",fontsize=11)
ax.legend(labels=["Sample data","Regression Model"])

#displaying multiple reg model on web app
with st.container():
    st.write("---")
    st.header('Multiple Linear Regression Model')
    st.write("")
    fig5
    st.write("")
    st.markdown('<p class="font">The accuracy of model is:</p>', unsafe_allow_html=True)
    st.write(accuracy_mlr)
    st.header('Conclusion')
    st.markdown('<p class="font">From above observation we can conclude that this Model is <b>accurate</b></p>', unsafe_allow_html=True)   
    