from subgrounds.subgrounds import Subgrounds
sg = Subgrounds()
import streamlit as st
import pandas as pd
import numpy as np

st.write('working')

button = st.button('click me')
if(button == True):
  st.write('test')
  df = pd.DataFrame(np.random.randint(0,100,size=(10, 3)), columns=list('ABC')) 
  df.to_csv('test.csv') 
  
