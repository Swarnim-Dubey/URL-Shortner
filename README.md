# URL Shortener

A simple URL shortener web application built with **Python**, **SQL**, **JavaScript**, **HTML**, and **CSS**. The project follows a clean separation between backend and frontend, making it beginner-friendly while still being scalable for future improvements.

---

## Features

* Shorten long URLs into compact shareable links
* Redirect shortened URLs to the original destination
* Store URL mappings in a SQL database
* Simple and responsive frontend interface
* Organized backend and frontend structure
* Easy to extend with analytics, authentication, or custom aliases

---

## Tech Stack

### Backend

* Python
* FastAPI / Flask-style backend structure
* SQL database
* Uvicorn

### Frontend

* HTML
* CSS
* JavaScript

### Database

* SQLite (default setup)

---

## Folder Explanation

### `backend/app/`

Contains the main backend logic.

* `config.py` → Application configuration and settings
* `models.py` → Database models/tables
* `routes.py` → API endpoints and route handling
* `utils.py` → Helper functions such as URL generation and validation

### `backend/database/`

Handles database connection and initialization.

* `db.py` → Database setup and session management

### `frontend/`

Contains all client-side files.

* `index.html` → Main webpage
* `style.css` → Styling for the UI
* `script.js` → Frontend logic and API calls

### Root Files

* `main.py` → Entry point for running the application
* `pyproject.toml` → Project dependencies and configuration
* `README.md` → Project documentation

---

## Installation

### 1. Clone the Repository

```bash
git clone <https://github.com/Swarnim-Dubey/URL-Shortner>
cd URL-Shortner
```

### 2. Create a Virtual Environment

Using `uv`:

```bash
uv venv
```

Activate the environment:

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
uv sync
```

Or install manually:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
uv run main.py
```

The application should start on:

```text
http://127.0.0.1:8000
```

---

## How It Works

1. User enters a long URL in the frontend.
2. Frontend sends the URL to the backend API.
3. Backend generates a unique short code.
4. The original URL and short code are stored in the database.
5. When the short URL is opened, the backend redirects the user to the original URL.

---

## Example Flow

### Original URL

```text
https://example.com/very/long/url/path
```

### Shortened URL

```text
http://127.0.0.1:8000/abc123
```

---

## Future Improvements

* Custom short aliases
* QR code generation
* Click analytics
* User authentication
* Expiration dates for links
* Copy-to-clipboard button
* Dark mode UI

---

## Development Notes

* The project uses a modular structure for easier maintenance.
* Frontend and backend are separated for better scalability.
* SQLite is suitable for development and small projects.
* The structure can later be upgraded to PostgreSQL or MySQL.

---

## Learning Goals

This project is useful for learning:

* Backend API development
* Database integration
* Frontend-backend communication
* URL routing and redirection
* Project structuring in Python
* Full-stack development basics

---
