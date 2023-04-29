import streamlit as st 
import comp1
import pandas
from streamlit_card import card

placeholder = st.empty()
def clicked(lol): 
    st.title("College Collation App")
    st.dataframe(lol["Review "])


with placeholder.container(): 
    st.title("College Collation App")
    college=st.selectbox("Choose a College",("PES University","RVCE","MSRIT","BIT","DSU","BMS","MIT","Reva University","Amrita","New Horizon","CMRIT","MVJ","NMIT","NITK","Alliance","Presidency","Jain University","AIT","GAT","RNSIT","Christ"))
    review=comp1.processing(college)
    btn = st.button("See all reviews",on_click=clicked,args=(review[0],))
    st.markdown(review[1])
    if btn:
        placeholder.empty()
