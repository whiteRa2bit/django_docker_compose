rm */migrations/0*.py
rm db.sqlite3
python3 manage.py makemigrations server
python manage.py migrate
