FROM python:3

COPY /app /app
COPY /env-var/prod /app/.env
COPY requirements.txt /app
COPY /output /app/output

WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["/app/run.sh"]