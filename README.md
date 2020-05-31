# heroku_flaskr
# 手順
```
pip3 freeze > requirements.txt
heroku create
heroku addons:create heroku-postgresql
heroku config:set FLASK_APP=flaskr
heroku config:set FLASK_ENV=development
git push heroku master
```

# run
```
flask run -h 0.0.0.0 -p $PORT
```

# gevent
```
python server.py
```
