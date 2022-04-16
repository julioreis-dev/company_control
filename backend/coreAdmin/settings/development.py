from .settings import *


# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config("SECRET_KEY", cast=str)
SECRET_KEY = "+e%70$7p#q8-)!3^ub56r%w-3-u&=!1v-@g@=te6o!lx*$8gfk"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(str(BASE_DIR), "db.sqlite3"),
    }
}
