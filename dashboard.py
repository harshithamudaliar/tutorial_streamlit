import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Gapminder Dashboard", layout="wide")
st.title("Gapminder Dashboard")

df=px.data.gapminder()
year=st.sidebar.slider("Select Year", int(df['year'].min()), int(df['year'].max()), int(df['year'].min()), step=5)
continents= st.sidebar.multiselect("Select Continents", options=df['continent'].unique(), default=df['continent'].unique())

filtered_df=df[(df['year']==year) & (df['continent'].isin(continents))]

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Number of Countries", filtered_df['country'].nunique())
with col2:
    st.metric("Average Life Expectancy", f"{filtered_df['lifeExp'].mean():.2f} years")
with col3:
    st.metric("Average GDP per Capita", f"${filtered_df['gdpPercap'].mean():.2f}")
fig=px.scatter(filtered_df, x="gdpPercap", y="lifeExp", size="pop", color="continent",
               hover_name="country", log_x=True, size_max=60,
               title=f"Life Expectancy vs GDP per Capita in {year}")
st.plotly_chart(fig, use_container_width=True)

fig2=px.bar(filtered_df.groupby('continent', as_index=False).agg({'pop':'sum'}),
            x='continent', y='pop', title=f"Total Population by Continent in {year}")
st.plotly_chart(fig2, use_container_width=True)