FROM python:3.9
# Set the working directory inside the container
WORKDIR /app

COPY ./app/requirements.txt .

RUN pip install  -r requirements.txt

COPY ./app .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
