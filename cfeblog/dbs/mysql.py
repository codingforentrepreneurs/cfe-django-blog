import os

MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get(
    "MYSQL_ROOT_PASSWORD"
)  # using the ROOT User Password for Local Tests
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE")
MYSQL_HOST = os.environ.get("MYSQL_HOST")
MYSQL_TCP_PORT = os.environ.get("MYSQL_TCP_PORT")
MYSQL_DB_IS_AVAIL = all(
    [MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE, MYSQL_HOST, MYSQL_TCP_PORT]
)

if MYSQL_DB_IS_AVAIL:
    # print("using mysql")
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": MYSQL_DATABASE,
            "USER": MYSQL_USER,
            "PASSWORD": MYSQL_PASSWORD,
            "HOST": MYSQL_HOST,
            "PORT": MYSQL_TCP_PORT,
        }
    }
