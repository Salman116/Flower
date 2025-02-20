# 🌸 Flower: Celery Monitoring with Django

## 📌 Overview
This project sets up Celery and Flower for asynchronous task management and monitoring in a Django application.

---

## 🚀 Setting Up the Django Project

1. **Create a Virtual Environment**
   ```sh
   python -m venv venv
   cd venv/Scripts
   activate
   ```
2. **Install Required Packages**
   ```sh
   pip install django django-cors-headers djangorestframework django-rest-knox \
       python-decouple django-filter django-storages psycopg2-binary pillow \
       cryptography whitenoise boto3 django-import-export django-tinymce
   ```
3. **Create a Django Project & App**
   ```sh
   django-admin startproject myproject .
   python manage.py startapp app
   ```
4. **Register Installed Apps** (in `settings.py`)
   ```python
   INSTALLED_APPS = [
       'app',
       'knox',
       'rest_framework',
       'corsheaders',
       'import_export',
       'tinymce',
       'storages',
   ]
   ```

---

## ⚙️ Installing Celery & Flower
Install Celery, Flower, and Redis:
```sh
pip install celery flower redis
```

---

## 🔧 Configuring Celery in Django

### 1️⃣ Update `settings.py`
```python
import os
from celery import Celery

# Celery settings
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
```

### 2️⃣ Initialize Celery in `myproject/__init__.py`
```python
from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when Django starts
from .celery import app as celery_app

__all__ = ('celery_app',)
```

### 3️⃣ Create Celery Configuration in `myproject/celery.py`
```python
import os
from celery import Celery

# Set default Django settings module for Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

app = Celery("myproject")

# Load task modules from all registered Django app configs
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
```

---

## 📝 Adding Celery Tasks in Django Apps

### 1️⃣ Create `tasks.py` Inside Your App
```python
from celery import shared_task

@shared_task
def add(x, y):
    return x + y
```

### 2️⃣ Call the Celery Task
```python
from app.tasks import add
add.delay(10, 20)  # Runs asynchronously
```

---

## 📦 Setting Up Redis as the Message Broker

1. **Install Redis (Linux/macOS)**
   ```sh
   sudo apt update
   sudo apt install redis
   sudo systemctl start redis
   sudo systemctl enable redis
   ```

2. **Verify Redis is Running**
   ```sh
   redis-cli ping  # Should return 'PONG'
   ```

---

## 🚀 Running Celery & Flower

### 1️⃣ Start Celery Worker
```sh
celery -A myproject worker --loglevel=info
```

### 2️⃣ Start Flower (Celery Monitoring Tool)
```sh
celery -A myproject flower
```
Now, visit `http://localhost:5555` to monitor Celery tasks with Flower.

---

## ✅ Done!
You have successfully set up **Celery** with **Flower** in Django! 🎉

