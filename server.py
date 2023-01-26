import numpy as np
import pandas as pd
import streamlit as st
from flask import Flask, jsonify, render_template, request
from PIL import Image
from pickle5 import pickle
from numpy import genfromtxt

app = Flask(__name__)
model = pickle.load(open('UC1_svc_model.sav', 'rb'))
labels ={
  'Y': "Yes",
  'N': "No",
}

@app.route('/')
def welcome():
    return "Index Page"

@app.route('/predict',methods=['POST'])
def predict(pred):
    prediction=model.predict(pred)
    return labels[prediction[0]]
def main():
    st.title("Auto insurance fraud detection")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Intelligent Automobile insurance fraud detector </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    # sl = st.text_input("Sepal Length","Type Here")
    # sw = st.text_input("Sepal Width","Type Here")
    # pl = st.text_input("Petal Length","Type Here")
    # pw = st.text_input("Petal Width","Type Here")
    filein = st.file_uploader("Upload the test csv input here")

    if filein is not None:
    
        my_df = pd.read_csv(filein)
        st.dataframe(my_df)

        #my_data = my_df.to_numpy()
    

    result=""
    if st.button("Predict"):
        result=predict(my_df)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")
if __name__=='__main__':
    main()