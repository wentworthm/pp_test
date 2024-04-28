FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app

RUN pip install --no-cache-dir fastapi uvicorn[standard]

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]