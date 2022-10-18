# CFE Django Blog

This is boilerplate code that you can use to learn how to bring Django into production.

## TLDR;

This is definitely coming soon -- basically a list of all commands to get this repo working locally.

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
- You can use _any_ virtual environment manager (poetry, pipenv, virtualenv, etc)

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

### Step 5: Select a Database

As of now, we have the following supported databases for this boilerplate code: `sqlite`, `mysql`, `postgres`

#### `sqlite`

No action needed. Django will managed sqlite for you.

#### `mysql`

To install Python client:

```
$(venv) python -m pip install mysqlclient
```

> If macOS, you must run `brew install mysql` (assuming you have [homebrew](https://brew.sh) installed)

Be sure you add `mysqlclient` to `requirements.txt` like:

```
echo "mysqlclient" >> requirements.txt
```

> Using the double `>>` vs a single `>` is the difference between appending and overwriting respectively.

#### `postgres`

```
$(venv) python -m pip install psycopg2
```

> You may need to use `python -m pip install psycopg2-binary` during development.

Be sure you add `psycopg2` to `requirements.txt` like:

```
echo "psycopg2" >> requirements.txt
```

> Using the double `>>` vs a single `>` is the difference between appending and overwriting respectively.

### Step 6: Setup your `.env`

Create your `.env` file (or reference the `.env-sample` in the repo).

```
echo "" > .env
```

Below is an example of _development-ready_ `.env` file for this project. **ALWAYS** update these values when going into production.

```
# required keys
DJANGO_SECRET_KEY=gy_1$n9zsaacs^a4a1&-i%e95fe&d3pa+e^@5s*tke*r1b%*cu
DATABASE_BACKEND=postgres

# mysql db setup
MYSQL_DATABASE=cfeblog-m-db
MYSQL_USER=cfeblog-m-user
MYSQL_PASSWORD=RaSNF5H3ElCbDrGUGpdRSEx-IuDzkeHFL_S_QBuH5tk
MYSQL_ROOT_PASSWORD=2mLTcmdPzU2LOa0TpAlLPoNf1XtIKsKvNn5WBiszczs
MYSQL_TCP_PORT=3007
MYSQL_HOST=127.0.0.1

# postgres db setup
POSTGRES_DB=cfeblog-p-db
POSTGRES_USER=cfeblog-m-user
POSTGRES_PASSWORD=NwgFCimzL0Oqd539EYzsztY04uzw2jaVEIrH1OK2sz0
POSTGRES_PORT=5431
POSTGRES_HOST=localhost
```

To generate secrets use one of the following method(s):

##### Use Django to create a one-off secret key (bookmark this [blog post](https://www.codingforentrepreneurs.com/blog/create-a-one-off-django-secret-key/)):

```
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

This is the recommended method for creating the `DJANGO_SECRET_KEY`

##### Use Python to create a url safe secret:

```
python -c "import secrets;print(secrets.token_urlsafe(32))"
```

### Step 6: Local Development with Docker Compose

Running our local environment with the same type of database as our production database is critical. For this, we'll use Docker and Docker Compose.

With Docker, your machine can have a _lot_ of instances of MySQL/Postgres/Redis running with minimal configuration. This is true for macOS, Windows, and nearly all distros of Linux that can run Docker.

Without Docker, having more than 1 version of any of these running is a huge pain. A pain that _might_ be worth going through if you like to bleed from your eyes. It's also an uncessary pain because we're talking about the _development_ environment.

Now on to the nitty gritty.

In our `docker-compose.yaml` file, you'll see configuration for the services:

- `mysql_db`
- `postgres_db`
- `redis_db`

But wait, there is not a `web` service for Django in `docker-compose.yaml`... why not? Two reasons:

- If you need it, you can add it.
- If you're new to Python, Virtual Environments, Django, Docker, VSCode, Git, or whatever it makes things even more complex.

If you're new to Docker compose, this might suck too. Sorry about that. But I hope you trust me that, in this case, the juice is worth the squeeze (aka it's worth the effort in learning how to use it).

Since I wanted to support both `mysql` and `postgres` I wanted to make use of Docker Compose's [profiles](https://docs.docker.com/compose/profiles/) feature.

Basicaly, you can use a profile to "activate" different services within a Docker compose file (instead of having a bunch of different Docker compose files).

In our case, `docker-compose.yaml` has three profiles:

- `mysql` (includes the `mysql_db` and `redis_db` services)
- `postgres` (includes the `postgres_db` and `redis_db` services)
- `redis` (runs only the `redis_db` service)

To run any given profile you just do:

```
docker compose --profile mysql up
```

> Just replace `--profile postgres` if you want to use that one.

Also, keep in mind that some systems require you to use `docker-compose` instead of `docker compose`.

I recommend running this profile in background mode (aka detached mode):

```
docker compose --profile mysql up -d
```

> Again, just replace `--profile postgres` if you want to use that one.
