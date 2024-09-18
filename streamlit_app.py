import streamlit as st
import pandas as pd
import plotly.express as plt

st.sidebar.title('Sidebar')
# st.title("🎈 Test app")
# name=st.text_input("Enter your name")
# btn= st.button("show")
# if btn:
#   st.write(f'Hello {name}')
# with st.sidebar:
#   st.subheader('Select the shape')

# area=None
# st.header("Calculate Area")
# choose=st.selectbox('choose the shape ',['rectangle','circle'])
# if choose == 'rectangle':
#   h=st.number_input('Enter the length',min_value=1,max_value=100)
#   w=st.number_input('Enter the width',min_value=1,max_value=100)
#   area=w*h
# elif choose == 'circle':
#   r=st.number_input('Enter the radius',min_value=1,max_value=100)
#   area=3.14*r*r
# btn=st.button('calculate')
# if btn:
#   with st.spinner('Loading....'):
#     #st.time.sleep(2)
#     st.write(f'The area is {area}')


file=st.file_uploader('Upload a file',type=['csv'])
if file is not None:
 df=pd.read_csv(file)
 st.write(df)
 num_row=st.slider('choose num rows' , min_value=1,max_value=len(df),step=1)
 name_column=st.multiselect('choose columns',df.columns.tolist())
 if name_column :
  st.write(df[:num_row][name_column])
  
  fig=plt.scatter(df,x='Quantity',y='OrderValue')
  st.plotly_chart(fig)
 else :
   st.write(df[:num_row])
 num_col=df.select_dtypes(include='number').columns.tolist()
 tab1 , tab2=st.tabs(['scatter','histogram'])
 with tab1:
  col1,col2,col3=st.columns(3)
  with col1:
   x_col=st.selectbox('choose x axis',num_col)
  with col2: 
   y_col=st.selectbox('choose y axis',num_col)
  with col3:
   color=st.selectbox('choose color',df.columns.tolist())

 with tab2:
  fig=plt.scatter(df,x='Quantity',y='OrderValue')
  st.plotly_chart(fig)
  x_col=st.selectbox('choose x axis',num_col)
  plt.histogram(df,x=x_col)

   
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
