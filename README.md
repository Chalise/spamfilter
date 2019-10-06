# spamfilter
Machine-learning spam filter

API implemented in Flask-Restful, python3. Served with gunicorn.

API in debug mode:
$ python3 api.py

API with gunicorn:
$ gunicorn --bind 0.0.0.0 api.api:app

With gunicorn you can then try:
curl -X POST http://127.0.0.1:8000/spam
