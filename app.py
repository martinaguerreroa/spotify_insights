# app.py

import streamlit as st
import pandas as pd
import altair as alt
from utils import preprocess_spotify_data

st.title("Your Spotify Listening Stats")

# Upload JSON
uploaded_file = st.file_uploader("Upload your Spotify JSON", type="json")

# Set colors
default_colors = ["#4E79A7", "#F28E2B", "#E15759", "#76B7B2", "#59A14F", "#EDC949", "#AF7AA1", "#FF9DA7", "#9C755F", "#BAB0AC"]


if uploaded_file:
    df = pd.read_json(uploaded_file)
    df = preprocess_spotify_data(df)

    top_artists_df = (
        df.groupby("artistName")["minPlayed"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    artist_colors = {
        name: color for name, color in zip(top_artists_df["artistName"], default_colors)
    }

    option = st.selectbox(
        "Select the insight you want to view:",
        [
            "Top Artists by Minutes Played",
            "Top Artists by Streams",
            "Top Songs",
            "Most Active Days"
        ]
    )


    if option == "Top Artists by Minutes Played":
        st.subheader("Top Artists by Minutes Played")
        chart = (
            alt.Chart(top_artists_df)
            .mark_bar()
            .encode(
                x=alt.X("minPlayed:Q", title="Minutes Played"),
                y=alt.Y("artistName:N", sort="-x", title="Artist"),
                color=alt.Color("artistName:N",
                                scale=alt.Scale(domain=list(artist_colors.keys()),
                                                range=list(artist_colors.values())),
                                legend=None),
                tooltip=["artistName", "minPlayed"]
            )
            .properties(width=700, height=400)
        )
        st.altair_chart(chart)



    elif option == "Top Artists by Streams":
        st.subheader("Top Artists by Streams")
        top_artists_s = df["artistName"].value_counts().head(10)
        top_artists_s_df = top_artists_s.reset_index()
        top_artists_s_df.columns = ["artistName", "streams"]
        chart = (
            alt.Chart(top_artists_s_df)
            .mark_bar()
            .encode(
                x=alt.X("streams:Q", title="Streams"),
                y=alt.Y("artistName:N", sort="-x", title="Artist"),
                color=alt.Color("artistName:N",
                                scale=alt.Scale(domain=list(artist_colors.keys()),
                                                range=list(artist_colors.values())),
                                legend=None),
                tooltip=["artistName", "streams"]
            )
            .properties(width=700, height=400)
        )
        st.altair_chart(chart)

    elif option == "Top Songs":
        st.subheader("Top Songs")
        top_songs_df = (
            df.groupby(["artistName", "trackName"])["minPlayed"]
            .sum()
            .sort_values(ascending=False)
            .head(20)
            .reset_index()
        )
        top_songs_df["song"] = top_songs_df["artistName"] + " – " + top_songs_df["trackName"]
        chart = (
            alt.Chart(top_songs_df)
            .mark_bar(color="#FF9DA7")  # or any preferred hex
            .encode(
                x=alt.X("minPlayed:Q", title="Minutes Played"),
                y=alt.Y("song:N", sort="-x", title="Song", axis=alt.Axis(labelLimit=0)),
                tooltip=["artistName", "trackName", "minPlayed"]
            )
            .properties(width=800, height=600)
        )
        st.altair_chart(chart)

    elif option == "Most Active Days":
        st.subheader("Most Active Days")
        top_days_df = (
            df.groupby("date")["minPlayed"]
            .sum()
            .sort_values(ascending=False)
            .head(20)
            .reset_index()
        )
        top_days_df["date"] = top_days_df["date"].astype(str)
        chart = (
            alt.Chart(top_days_df)
            .mark_bar(color="#E15759")
            .encode(
                x=alt.X("minPlayed:Q", title="Minutes Played"),
                y=alt.Y("date:N", sort="-x", title="Date", axis=alt.Axis(labelLimit=0)),
                tooltip=["date", "minPlayed"]
            )
            .properties(width=800, height=600)
        )
        st.altair_chart(chart)




