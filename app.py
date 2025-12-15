import streamlit as st 
import plotly.express as px

st.title("Minimal Streamlit App")
name=st.text_input("Enter your name:")
age=st.slider("Select your age:",0,100,10)
st.write(f"Hello, {name}. You are {age} years old.")

col1,col2=st.columns(2)
col1.write("Holiday on Christmas")
col2.write("Examination on Christmas")

@st.cache_data
def load_data():
    return px.data.gapminder()

df=load_data()
fig=px.scatter(df.query("year==2007"),x="gdpPercap",y="lifeExp",size="pop",color="continent",
               hover_name="country",log_x=True,size_max=60)
st.plotly_chart(fig)