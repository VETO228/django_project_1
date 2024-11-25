FROM python:3.8

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /TaskTracker

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]