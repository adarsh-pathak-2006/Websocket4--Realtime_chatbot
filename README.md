# Realtime AI Chatbot (Django Channels & Gemini)

A production-ready, full-stack real-time AI chatbot application built with Django Channels (WebSockets) and the Google GenAI API.

## Features

- **Real-Time WebSockets:** Instant two-way communication powered by Django Channels and Redis.
- **Asynchronous AI Streaming:** The backend uses the `google-genai` async client (`client.aio`) to stream AI responses chunk-by-chunk without blocking the main event loop.
- **Dynamic UI:** A modern frontend that dynamically appends streaming text chunks to a single chat bubble, providing a smooth "typewriter" effect similar to ChatGPT.
- **Production Ready:** Pre-configured for deployment on Render with proper proxy headers, CSRF trusted origins, and environment variable support.

## Tech Stack

- **Backend Framework:** Django & Django Channels
- **AI Integration:** Google Gemini API (`gemini-2.5-flash`)
- **WebSockets:** Daphne (ASGI Server)
- **Frontend:** HTML, CSS (Vanilla with Glassmorphism UI), Vanilla JavaScript

## Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/adarsh-pathak-2006/Websocket4--Realtime_chatbot.git
cd Websocket4--Realtime_chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Variables
Create a `.env` file in the root directory (next to `manage.py`) with the following variables:
```env
SECRET_KEY="your-secret-key"
GEMINI_API_KEY="your-google-gemini-api-key"
```

### 4. Run Migrations & Start Server
```bash
python manage.py migrate
python manage.py runserver
```
*(Ensure you have Daphne installed and configured in `INSTALLED_APPS` so `runserver` starts the ASGI server).*

## Deployment (Render)

This project is configured for deployment on Render.

1. **Build Command:** `./build.sh` (If you have a build script) or `pip install -r requirements.txt && python manage.py migrate`
2. **Start Command:** `daphne real_time.asgi:application --port $PORT --bind 0.0.0.0`
3. **Environment Variables for Production:**
   - `SECRET_KEY`: Your secure secret key
   - `GEMINI_API_KEY`: Your Google GenAI API key
   - `ALLOWED_HOSTS`: `*` (or your specific render URL)
   - `CSRF_TRUSTED_ORIGINS`: `https://your-app-name.onrender.com`
