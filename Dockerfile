FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpango1.0-0 \
    libcairo2 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    libgdk-pixbuf2.0-dev \
    && apt-get clean

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "generate_invoice.py"]
