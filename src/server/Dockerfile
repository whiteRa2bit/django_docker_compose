FROM python:3.8

RUN mkdir /app/
WORKDIR /app/
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000
RUN python manage.py makemigrations server
RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
# CMD ["/bin/bash"]