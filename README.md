# studydeck_forum
A discussion forum for the studydeck website.

## Setup Instructions
### Add this to .env file
```
# Django Core Settings
DEBUG=true
SECRET_KEY=django-insecure-development-secret-key-studydeck-1234567890
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1] web

# Database Configuration (Docker/PostgreSQL)
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

### Then run the following command
```shell
docker compose up --build
```

### For creating superuser
```
docker exec -i -t studydeck-forum-web-1 python manage.py createsuperuser
```
And then follow the instructions.
