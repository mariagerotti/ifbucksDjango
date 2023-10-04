FROM python:3.10.6

RUN apt-get update


WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN pip install -r requirements.txt


COPY . .

ENV PYTHONUNBUFFERED=1
RUN python manage.py migrate
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]