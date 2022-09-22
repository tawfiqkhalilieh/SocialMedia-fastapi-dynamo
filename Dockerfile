FROM python:3.8-slim

LABEL maintainer="Tawfiq Khalilieh <xtcoding@gmail.com>"

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 4000

COPY ./app ./app

CMD [ "uvicorn", "app.main:app", "--port", "4000", "--host", "0.0.0.0" ]