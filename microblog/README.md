# Microblog

## Getting started

mkdir microblog

cd microblog

python3 -m venv venv

source venv/bin/activate

pip install flask

flask run --port 5001

pip install python-dotenv

flask run

### Database migration
flask db init

flask db migrate -m "users table"

flask db upgrade

### Flask extentions
- flask-wtf
- flask-sqlalchemy
- flask-migrate