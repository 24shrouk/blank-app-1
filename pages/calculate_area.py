import streamlit as st
st.header("Calculate Area")
choose=st.selectbox('choose the shape ',['rectangle','circle'])
if choose == 'rectangle':
  h=st.number_input('Enter the length',min_value=1,max_value=100)
  w=st.number_input('Enter the width',min_value=1,max_value=100)
  area=w*h
elif choose == 'circle':
  r=st.number_input('Enter the radius',min_value=1,max_value=100)
  area=3.14*r*r
btn=st.button('calculate')
if btn:
  with st.spinner('Loading....'):
    #st.time.sleep(2)
    st.write(f'The area is {area}')
