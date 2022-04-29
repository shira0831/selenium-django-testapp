from pathlib import Path


#settings.pyからそのままコピー
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-zd69ptshc_z#0thf(n5268-hvnj$_$-siq5o2zo#gj1q5*4f_h'


#settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


DEBUG = True #ローカルでDebugできるようになります