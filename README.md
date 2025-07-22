# Spotify Listening Insights

This project lets you explore your personal Spotify listening data using either an interactive Streamlit dashboard or a Jupyter notebook for deeper analysis. You upload your Spotify `.json` export, and it gives you clean, customizable visualizations of how you actually listen to music — not just the yearly Wrapped summary.

I built this because I was curious about my own habits, and honestly, Spotify's default analytics don’t go deep enough.

---

## What You Can See

- **Top Artists by Minutes Played**
- **Top Artists by Streams**
- **Top Songs** (ranked by minutes)
- **Most Active Listening Days**

Both the notebook and the app generate clean, minimal bar charts (using Altair or Matplotlib), and in the app version you can switch between views with a dropdown.

---

## How to Use This

You’ve got two options:

### 1. Streamlit App (Interactive Dashboard)

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/spotify_insights.git
cd spotify_insights

# Set up environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Launch app
streamlit run app.py
```

### 2. Jupyter Notebook

```bash
To run it:
# Clone the repo
cd spotify_insights

# Install requirements
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook spotify_insights_notebook.ipynb

```

