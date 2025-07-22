
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and preprocess data
def load_spotify_data(*files):
    dfs = [pd.read_json(f) for f in files]
    return pd.concat(dfs, ignore_index=True)

def preprocess_spotify_data(df):
    df["minPlayed"] = df["msPlayed"] / 60000
    df["endTime"] = pd.to_datetime(df["endTime"])
    df["date"] = df["endTime"].dt.date
    df["time"] = df["endTime"].dt.time
    return df

# Set style and color scheme
sns.set_style("ticks")
colors = {
    "primary": "#4B6EA8",      # muted blue
    "secondary": "#8797AF",    # soft slate gray-blue
    "accent": "#A3C4BC",       # desaturated mint
    "highlight": "#E2C2B9",    # soft clay pink
    "background": "#FAFAFA",   # off-white
    "text": "#2C2C2C",         # near-black for contrast
    "grid": "#D9D9D9",         # light gray gridlines
    "stream": "#7B9E89",       # muted green
    "time": "#6A89CC",         # washed denim blue
    "track": "#B2948E",        # toned-down terracotta
    "daily": "#7F8C8D",        # warm gray
}


# Most listened to artist by time
def top_artists_by_time(df_history):
    df_top_artists_by_time = (
        df_history.groupby("artistName")["minPlayed"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    df_top_artists_by_time.head(10).plot(
        kind = "barh",
        x = "artistName",
        y = "minPlayed", 
        figsize = (10,6), 
        color = colors["time"],
        legend = False)
    plt.title("Your Top 10 Artists by Listening Time", fontsize=18, fontname="DIN Alternate", color=colors["text"])
    plt.xlabel("Minutes Played", fontsize=12, fontname="Avenir Next Condensed")
    plt.ylabel("")
    plt.grid(True, axis='x', linestyle='--', alpha=0.5)
    plt.xticks(color=colors["text"], fontname="Avenir Next Condensed")
    plt.yticks(color=colors["text"], fontname="Avenir Next Condensed")
    plt.gca().invert_yaxis()
    plt.gcf().set_facecolor(colors["background"])
    plt.tight_layout()
    plt.show()

# Most listened to artist by streams
def top_artists_by_streams(df_history):
    df_top_artists_by_streams = df_history["artistName"].value_counts()
    df_top_artists_by_streams.head(10).plot(
        kind="barh", 
        figsize = (10,6), 
        color = colors["stream"],
        legend = False)
    plt.title("Your Top 10 Artists by Number of Streams", fontsize=18, fontname="DIN Alternate", color=colors["text"])
    plt.xlabel("Streams", fontsize=12, fontname="Avenir Next Condensed", color=colors["text"])
    plt.ylabel("")
    plt.grid(True, axis='x', linestyle='--', alpha=0.5)
    plt.xticks(color=colors["text"], fontname="Avenir Next Condensed")
    plt.yticks(color=colors["text"], fontname="Avenir Next Condensed")
    plt.gca().invert_yaxis()
    plt.gcf().set_facecolor(colors["background"])
    plt.tight_layout()
    plt.show()

# Top songs 
def top_songs(df_history):
    df_top_songs = (
        df_history.groupby(["artistName", "trackName"])["minPlayed"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    df_top_songs.head(20).plot(
        kind = "barh",
        x = "trackName",
        y = "minPlayed",
        figsize = (10, 6),
        color = colors["track"],
        legend = False)
    plt.xlabel("Minutes Played", fontsize=12, fontname="Avenir Next Condensed", color=colors["text"])
    plt.title("Your Top 20 Songs", fontsize=18, fontname="DIN Alternate", color=colors["text"])
    plt.ylabel("")
    plt.grid(True, axis='x', linestyle='--', alpha=0.5)
    plt.xticks(color=colors["text"], fontname="Avenir Next Condensed")
    plt.yticks(color=colors["text"], fontname="Avenir Next Condensed")
    plt.gca().invert_yaxis()
    plt.gcf().set_facecolor(colors["background"])
    plt.tight_layout()
    plt.show()

# Most active days
def days(df_history):
    daily_minutes = (
        df_history.groupby("date")["minPlayed"]
        .sum()
        .sort_values(ascending=False)
        .head(20)
    )
    daily_minutes.plot(
        kind = "barh",
        figsize = (10, 6),
        color = colors["daily"],
        legend = False)
    plt.title("Days with Highest Listening Activity", fontsize=18, fontname="DIN Alternate", color=colors["text"])
    plt.ylabel("Date", fontsize=12, fontname="Avenir Next Condensed", color=colors["text"])
    plt.xlabel("Minutes Played", fontsize=12, fontname="Avenir Next Condensed", color=colors["text"])
    plt.grid(True, axis='x', linestyle='--', alpha=0.5)
    plt.xticks(color=colors["text"], fontname="Avenir Next Condensed")
    plt.yticks(color=colors["text"], fontname="Avenir Next Condensed")
    plt.gcf().set_facecolor(colors["background"])
    plt.tight_layout()
    plt.show()





