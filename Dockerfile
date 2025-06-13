FROM python:3-alpine3.22

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN mkdir logs

CMD ["python", "investor.py"]
