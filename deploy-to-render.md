
# 🚀 ChronoBound CM – Deploy to Render

### Step 1: Push this project to your GitHub repository

### Step 2: Go to [Render](https://render.com)

- Click **New → Web Service**
- Connect your GitHub account
- Select this repo

### Step 3: Use the following settings

- **Environment:** Python 3
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`
- **Port:** 5000 (Render auto-detects this)

Render will provide a free HTTPS endpoint. Update `openapi.json` with the live Render URL if needed.
