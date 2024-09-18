import streamlit as st

st.title("🎈 My new app")
name=st.text_input("Enter your name")
btn= st.button("show")
if btn:
  st.write(f'Hello {name}')
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
