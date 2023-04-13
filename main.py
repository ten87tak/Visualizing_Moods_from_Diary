import streamlit as st
import glob
import plotly.express as px
from nltk.sentiment import SentimentIntensityAnalyzer
from pathlib import Path


filepaths = glob.glob("diary\*.txt")
# print(filepaths)
# This gives me a list of filenames.

analyzer = SentimentIntensityAnalyzer()
# It's not necessary to create this object repeatedly in the for-loop!
# So, this stays in the global area:)


pos_items = []
neg_items = []
dates = []
for filepath in filepaths:
    with open(filepath, encoding="utf-8") as file:
        text = file.read()

    scores = analyzer.polarity_scores(text)
    # print(scores)
    # print(scores["pos"])
    pos_items.append(scores["pos"])
    neg_items.append(scores["neg"])
# print(pos_items)
# [0.065, 0.17, 0.203, 0.238, 0.159, 0.062, 0.177]
    date = Path(filepath).stem
    dates.append(date)
# print(dates)
# ['2023-10-21', '2023-10-22', '2023-10-23', '2023-10-24', '2023-10-25', '2023-10-26', '2023-10-27']


# st.set_page_config(layout="centered")

st.title("Diary Tone")

st.subheader("Positivity")

p_figure = px.line(x=dates, y=pos_items, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(p_figure)

st.write("")
st.write("")

st.subheader("Negativity")

n_figure = px.line(x=dates, y=neg_items, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(n_figure)


