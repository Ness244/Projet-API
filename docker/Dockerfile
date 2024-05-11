FROM python:3.11

RUN addgroup --gid 1000 python
RUN useradd --create-home --home-dir /home/python --uid 1000 --gid 1000 python

WORKDIR /home/python

RUN apt update && apt install -y \
    python3-dev \
    libmysqlclient-dev

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]