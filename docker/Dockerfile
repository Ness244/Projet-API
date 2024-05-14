FROM python:3.12

RUN useradd --create-home -U --home-dir /home/python --uid 1000 python

WORKDIR /home/python

USER python

#COPY requirements.txt .

#RUN pip install --user  -r requirements.txt

#CMD ["python", "-m", "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]
