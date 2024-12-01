import streamlit as st


st.title("MUHAHAHAHAHAHAHAHAHAHAHAHAHHAAHHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHHAAHA")
st.header("YOKOSO..")
st.write("Watashino Soul Socity")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQSSziPlpjdNAeJ7gYYjgObLLjo8JirEK6Ayw&s")


import pandas as pd
import streamlit as st


st.title("HI, I'm ChillGuy")
st.header("I'm here for chill don't mind me.")
st.image("https://today-obs.line-scdn.net/0hTaElgcflC054FRpgOkt0GUBDBz9LcxFHWiFFL1tAVS5UOU1KEHJYLV0VVGJdcUUfWHNGLghGVClSJxsaRg/w644")

st.title("FARM!!!!!!!!")
df = pd.read_csv("../datasets/1642645053.csv", encoding="tis-620")
st.write(df)


st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Cow_female_black_white.jpg/1200px-Cow_female_black_white.jpg")
st.title("Analysis")
st.write(df.describe())

st.title("Titanic")
df1 = pd.read_csv("../datasets/titanic.csv", encoding="tis-620")
st.write(df)

st.title("Analysis")
st.write(df1.describe())

st.image("https://files.oaiusercontent.com/file-BREGxuSW2YBmVXubz6k28T?se=2024-12-01T06%3A32%3A00Z&sp=r&sv=2024-08-04&sr=b&rscc=max-age%3D604800%2C%20immutable%2C%20private&rscd=attachment%3B%20filename%3D438e3008-30c5-4a0d-8dc2-1abcaca504aa.webp&sig=7So8G9wQi28yXZ/97%2BWN13fYaVtTEsOrO0Ar1j4xZEI%3D")

st.title("Try URL")
url ="https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/titanic.csv"
df2 = pd.read_csv(url)
st.write(df2)

number = st.slider("Select a number", 0, 100, 50)
st.write("The current number is ", number)

rating = st.radio(
    "How would you rate this class?",
    ("1", "2", "3", "4", "5")
)
st.write(f"You selected {rating}")



url1 = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"



df3 = pd.read_csv(url1)
df_grouped_by_species = df3.groupby("species")["body_mass_g"].mean()
st.bar_chart(df_grouped_by_species)




import plotly.express as px

fig = px.bar(df_grouped_by_species.reset_index(), x="species", y="body_mass_g")
st.plotly_chart(fig)


with st.sidebar:
    st.write("This is a sidebar")
    option = st.selectbox(
        "Which number do you like best?",
        ["1", "2", "3", "4", "5"]
    )
    st.image("")