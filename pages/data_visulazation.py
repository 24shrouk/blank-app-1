

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
  fig=plt.scatter(df,x='Quantity',y='OrderValue')
  st.plotly_chart(fig)

#  with tab2:
  
  
  
#   fig2=plt.histogram(df,x='Quantity')
#   st.plotly_chart(fig2)
