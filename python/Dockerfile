FROM python:3-alpine

WORKDIR /src

COPY . .

RUN pip install -r requirements.txt

ENV FLASK_APP=api.py

EXPOSE 8000

CMD [ "python","api.py"]