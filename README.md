# CFE Django Blog

This is boilerplate code that you can use to learn how to bring Django into production.

## Getting Started

### Step 1: Fork / Clone

First, decide where this project will live.

```
mkdir -p ~/dev
cd ~/dev
```

> I always use the `~/Dev` folder which translates to `/users/cfe/Dev` (macOS / Linux) or `C:\Users\cfe\Dev` (windows). This location is optional.

Fork or clone this repo:

```
git clone https://github.com/codingforentrepreneurs/cfe-django-blog
```

### Step 2: Create a Virtual Environment

Isolate your python project from other python projects by using the built-in [venv](https://docs.python.org/dev/library/venv.html) module:

```
python3.10 -m venv venv
```

- I recommend Python 3.8 and up
- You can use _any_ virtual enviornment manager (poetry, pipenv, virtualenv, etc)

### Step 3: Activate Virtual Environment

_macOS/Linux_

```
source venv/bin/activate
```

_Windows_

```
.\venv\Scripts\activate
```

### Step 4: Install Requirements

```
$(venv) python -m pip install pip --upgrade
$(venv) python -m pip install -r requirements.txt
```

- `$(venv)` is merely denoting the virtual environment is activated
- In `requirements.txt` you'll see `django>=3.2,<4.0` -- this means I'm using the latest version of Django 3.2 since it's an LTS release.
- You can use `venv/bin/python -m pip install -r requirements.txt` (mac/linux) or `venv\bin\python -m pip install -r requirements.txt` (windows)
- `pip install ...` is not as reliable as `python -m pip install ...`
