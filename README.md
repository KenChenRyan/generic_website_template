[Tutorial](https://www.youtube.com/watch?v=MwZwr5Tvyxo) for python-flask

## What to use to keep the server going
Gunicorn (A python3 module) that keeps the python files in check and supervisor (apt install program) keeps gunicorn constantly running. Also nginx is the (industry standard?) web server.
#### Restart the server with 
```
sudo systemctl restart nginx
```
Restarting supervisor
```
sudo supervisorctl reload
```
This [link](https://stackoverflow.com/questions/18859063/supervisor-socket-error-issue) is helpful regarding configuring supervisor 

supervisor constantly runs the command 
```
gunicorn -w 3 run:app
```

## pip modules to install for web
__Recomennded to be done using a venv__
* flask
* flask_sqlalchemy (Database)
* flask_bcrypt (Encryption)
* flask_wtf \[Forms (POST and GET)\]

### Steps for setting up venv
Run these commands in the shell
(Install it through pip3 first)
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
## Tips for setting up developer enviornment
Setup the python venv

Run "run.py"
