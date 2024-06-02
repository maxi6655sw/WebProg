FROM python:3.10-slim-buster

RUN mkdir app
WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt


COPY .. /app

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD ["manage.py", "runserver","0.0.0.0:5000"]
