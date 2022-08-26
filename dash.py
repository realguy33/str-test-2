from subgrounds.subgrounds import Subgrounds
sg = Subgrounds()
import streamlit as st
import pandas as pd

st.write('working')

button = st.button('click me')
if(button == True):
  # list of name, degree, score 
  nme = ["aparna", "pankaj", "sudhir", "Geeku"] 
  deg = ["MBA", "BCA", "M.Tech", "MBA"] 
  scr = [90, 40, 80, 98] 
     
  # dictionary of lists  
  dict = {'name': nme, 'degree': deg, 'score': scr}  
       
  df = pd.DataFrame(dict) 
    
  # saving the dataframe 
  df.to_csv('GFG.csv') 
  
