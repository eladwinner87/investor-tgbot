FROM python:3.9.23-slim-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN mkdir logs

CMD ["python", "investorTgBot.py"]
