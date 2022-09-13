from pathlib import Path
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="Data Analysis",page_icon=":chart_with_upwards_trend:",layout="wide")

#Function for displaying graphical content(eg: image)
def Graphical_Content(url) :
    r = requests.get(url)
    if r.status_code != 200 :
        return None
    return r.json()

lottie_coding1 = Graphical_Content("https://assets6.lottiefiles.com/packages/lf20_0yfsb3a1.json")
lottie_coding2 = Graphical_Content("https://assets6.lottiefiles.com/packages/lf20_v4isjbj5.json")

#displaying website main motive
with st.container():
    left_column, right_column=st.columns((1,2))
    with left_column:
        st_lottie(lottie_coding1,height=300,key="coding")
    with right_column :
        st.title("Data Analysis Report")
        st.subheader("Data Analysis on Automotive Industry")
        st.write("")
        st.markdown("""<style>.font {font-size:20px !important;}</style>""", unsafe_allow_html=True)
        st.markdown('<p class="font">This Website summarises the Challenge of Data Analysis on a sample dataset of Automotive Industry</p>', unsafe_allow_html=True)

#displaying summary of website
with st.container():
    st.write("---")
    left_column, right_column=st.columns((1,2))
    with left_column:
        st.header("About Project")
        """
        - **The Data Analysis was done on a dataset "cars_engage_2022.csv**"
        - **The dataset "cars_engage_2022.csv" can be downloaded from my Github Profile
            (availabe below)**
    
        - **Using the dataset, data was analysed to find out the most popular Car Specification,
            most popular Car Type and the Power of car based on Fuel Capacity**
      
        - **Models were developed to predict the Future Sales**
        """
        st.write("**1. Simple Linear Regression Model**")
        st.write("**2. Multiple Linear Regression Model**")
    
        """- **Click on below link to view Visualized Data**"""
        st.write("[Data Visualization](https://nikhilteja21-data-analysis-websitedata-visualization-mmo6yi.streamlitapp.com/)")
    with right_column :
        st_lottie(lottie_coding2,height=300)

#Contact form Info
with st.container() :
    st.write("---")
    st.header("My Profile")
    st.markdown('<p class="font">Name: N.Nikhil Teja</p>', unsafe_allow_html=True)
    st.markdown('<p class="font">Branch: Computer Science and Engineering</p>', unsafe_allow_html=True)
    st.markdown('<p class="font">College: Maturi Venkata Subba Rao Enginneering College</p>', unsafe_allow_html=True)
    st.markdown('<p class="font">LinkedIn profile: </p>', unsafe_allow_html=True)
    st.write("[Click Here](https://www.linkedin.com/in/nikhilteja2621)")
    st.markdown('<p class="font">Github profile: </p>', unsafe_allow_html=True)
    st.write("[Click Here](https://github.com/NikhilTeja21)")
