# AI Coding Agent Instructions for Management Project

## Project Overview
Django 6.0.1 web application with a single app (`myapp`) for management functionality. Structure: `myproject/` (main Django project), `myapp/` (single Django application), `myenv/` (Python virtual environment).

## Architecture
- **Entry Point**: `manage.py` (Django CLI)
- **Settings**: `myproject/settings.py` - SQLite database, template directory at `templates/`
- **URL Routing**: `myproject/urls.py` → includes `myapp/urls.py`
- **Views**: `myapp/views.py` - Currently minimal (home view only)
- **Models**: `myapp/models.py` - Empty, add domain models here
- **Templates**: `myapp/templates/` - Django templates for rendering

## Critical Workflows

### Running the Application
```bash
# Activate virtual environment
.\myenv\Scripts\activate.bat  # Windows CMD
. .\myenv\Scripts\Activate.ps1  # Windows PowerShell

# Run development server
python manage.py runserver

# Run migrations (after model changes)
python manage.py migrate

# Create superuser for admin panel
python manage.py createsuperuser
```

### Database Operations
- SQLite database at `BASE_DIR / 'db.sqlite3'`
- Add models to `myapp/models.py`, then run migrations
- Admin interface at `/admin/` for CRUD operations

## Code Patterns & Conventions

### View Structure
Use function-based views (current pattern). Views must accept `request` parameter:
```python
# myapp/views.py
from django.shortcuts import render, redirect

def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
```

### URL Configuration
Add routes to `myapp/urls.py`, included in main `myproject/urls.py`:
```python
# myapp/urls.py
path('', views.home, name='home'),
path('resource/', views.resource, name='resource'),
```

### Template Rendering
- Templates located in `myapp/templates/`
- Use Django template tags and context variables
- Current templates: `home.html`, `homew.html`

## Project-Specific Notes
- **DEBUG = True** - Only for development; change for production
- **SECRET_KEY** - Exposed in settings.py; move to environment variable for production
- **No third-party apps** - Only Django built-in and `myapp`
- **Minimal views** - Only home view implemented; expand with more views as needed
- **Template directory** - Configured at project root level, not app-specific

## Common Tasks
- **Add new view**: Define in `myapp/views.py`, import in `myapp/urls.py`, create template
- **Create model**: Define in `myapp/models.py`, register in `myapp/admin.py`, run migrations
- **Add static files**: Place in `myapp/static/` (auto-served via `STATIC_URL = 'static/'`)
