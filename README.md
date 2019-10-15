# spamfilter
Machine-learning spam filter

API implemented in Flask-Restful, python3. Served with gunicorn.
Also includes a React client created with create-react-app.

Setup and Usage on Linux
========================

1. Set up Nginx according to vendor instructions.
2. Install pipenv, used for managing python dependencies.
3. Place nginx/spamfilter site configuration to your Nginx configuration. Restart Nginx
   Note you may need to adjust the server root location.
4. Start API
   
       $ pipenv run gunicorn --bind 0.0.0.0 api.api:app

5. Make a client build

       $ cd ui
       $ npm run

6. Profit!
   (Better instructions coming later)
