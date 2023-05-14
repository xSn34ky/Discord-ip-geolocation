FROM python:3
WORKDIR /app
COPY . /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "unclesam.py"]
