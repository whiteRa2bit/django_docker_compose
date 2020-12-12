FROM python:3.8

RUN mkdir /app/
WORKDIR /app/
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000
RUN ["chmod", "+x", "clean_db.sh"]
RUN ./clean_db.sh
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
# CMD ["/bin/bash"]