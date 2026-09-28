FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]

#For multistage
#FROM python:3.12 AS builder

#WORKDIR /app

#COPY requirements.txt .

#RUN python -m venv /opt/venv && /opt/venv/bin/pip install -r requirements.txt

#COPY app.py .


#FROM python:3.12

#COPY --from=builder /opt/venv /opt/venv

#ENV PATH="/opt/venv/bin:$PATH"

#WORKDIR /app

#COPY --from=builder /app/app.py .

#CMD ["python", "app.py"]
