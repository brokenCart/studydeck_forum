# StudyDeck Forum

StudyDeck Forum is a full-featured discussion platform built for StudyDeck, enabling students at BITS Pilani to share academic resources, discuss coursework, and collaborate within an authenticated and moderated community.

## Description

StudyDeck Forum is designed to streamline academic communication and resource sharing across campus. Built on Django 6.0 and PostgreSQL, the platform features institutional Google OAuth 2.0 authentication, rich Markdown content editing, nested discussion threads, AJAX upvoting, trigram similarity search, and automated email notifications.

### Tech Stack Overview

- **Backend:** Django 6.0 on Python 3.14+
- **Database:** PostgreSQL 15 with trigram similarity (`pg_trgm`) extension (SQLite3 fallback for local development)
- **Authentication:** `django-allauth` configured for Google OAuth 2.0 with institutional email validation
- **Frontend:** Django Templates, Bootstrap 5.3 (Dark Mode), EasyMDE Markdown editor, and highlight.js
- **WSGI / Reverse Proxy:** Gunicorn and Nginx
- **Containerization:** Docker & Docker Compose
- **Package Management:** uv

## Key Features

### Authentication and Access Control
- **Google OAuth Login:** Single Sign-On authentication via `django-allauth`.
- **Domain Restriction:** Enforces login exclusively for BITS Pilani email addresses (`@pilani.bits-pilani.ac.in`, `@goa.bits-pilani.ac.in`, `@hyderabad.bits-pilani.ac.in`).
- **User Profiles:** Automatically displays user Google profile avatars across threads and comments.

### Discussion Threads
- **Academic Context:** Link threads to specific courses, course resources (PDF, Video, Link), categories, and tags.
- **Markdown Support:** Content rendering with sanitized HTML, code blocks, tables, images, and blockquotes.
- **Syntax Highlighting:** Automatic code snippet formatting powered by `highlight.js`.
- **Soft Deletion:** Threads are marked as deleted rather than permanently removed from the database.

### Replies and Conversations
- **Nested Replies:** Support for direct thread replies and nested quotes/responses to existing replies.
- **Deep Linking:** Pagination-aware links to parent replies across thread pages.

### Voting System
- **AJAX Upvoting:** Real-time upvoting and un-upvoting for threads and replies without page reloads.
- **Vote Integrity:** Enforced database constraints ensuring one vote per user per item.
- **Popularity Sorting:** Sort content dynamically based on total upvote count.

### Search and Organization
- **Trigram Similarity Search:** Fuzzy title search on PostgreSQL using the `pg_trgm` extension.
- **Categories and Tags:** Navigation by category slugs and multi-tag filtering.
- **Dynamic Resource Select:** AJAX-powered resource dropdowns filtered based on the selected course.

### Moderation Tools
- **Thread Locking:** Ability for moderators to lock and unlock threads to control discussions.
- **Content Removal:** Permission-gated deletion of any thread or reply.
- **Reporting System:** User reporting workflow for inappropriate content.
- **Moderator Dashboard:** Centralized view for moderators to inspect and resolve content reports.

### Email Notifications
- **Asynchronous Alerts:** Background thread notifications sent when users receive replies to their threads or comments.
- **Configurable Backends:** Console logging for development environments and SMTP (Gmail) integration for production.

## Installation

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)
- Python 3.14+ and [uv](https://github.com/astral-sh/uv) (for local development without Docker)
- A [Google Cloud Console](https://console.cloud.google.com/) project with OAuth 2.0 credentials

### 1. Clone the Repository

```bash
git clone git@github.com:brokenCart/studydeck-forum.git
cd studydeck-forum
```

### 2. Environment Configuration

Create a `.env` file in the project root directory with the following variables:

```env
# Django Core Settings
DEBUG=true
SECRET_KEY=django-insecure-development-secret-key-studydeck-1234567890
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] web

# Database Configuration (Docker / PostgreSQL)
DATABASE=postgresql
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=studydeck_db
SQL_USER=studydeck_user
SQL_PASSWORD=securepassword123
SQL_HOST=db
SQL_PORT=5432

# Social Authentication (Google OAuth)
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_SECRET=your-google-client-secret

# Email / SMTP Settings (Used when DEBUG is set to false)
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password
DEFAULT_FROM_EMAIL=your-email@gmail.com
```

Note: Replace `your-google-client-id` and `your-google-client-secret` with your actual Google OAuth 2.0 credentials. Add `http://localhost:8000/accounts/google/login/callback/` to your authorized redirect URIs in Google Cloud Console.

### 3. Running with Docker

Start the containerized application and PostgreSQL database:

```bash
docker compose up --build
```

Access the application at `http://localhost:8000`.

To create an admin superuser:

```bash
docker exec -it studydeck-forum-web-1 python manage.py createsuperuser
```

Access the Django admin portal at `http://localhost:8000/admin/`.

### 4. Running Locally (Without Docker)

To run locally using SQLite:

```bash
# Install dependencies
uv sync

# Run database migrations
uv run python manage.py migrate

# Start the development server
uv run python manage.py runserver
```

Note: PostgreSQL trigram search (`pg_trgm`) is not supported under SQLite.

### 5. Production Deployment

To launch the production stack with Gunicorn and Nginx:

```bash
docker compose -f docker-compose.prod.yml up --build -d
```
