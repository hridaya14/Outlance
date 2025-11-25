FROM python:3.11-slim

# Install system dependencies for Chromium/Playwright
RUN apt-get update && apt-get install -y \
    wget gnupg unzip libnss3 libatk1.0-0 libatk-bridge2.0-0 \
    libcups2 libxkbcommon0 libgtk-3-0 libxcomposite1 libxdamage1 \
    libxrandr2 libasound2 libpangocairo-1.0-0 libpango-1.0-0 \
    libcairo2 libx11-xcb1 libxtst6 libxss1 libgbm1 xvfb \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install Playwright + Chromium
RUN playwright install --with-deps chromium

COPY app/ app/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]

