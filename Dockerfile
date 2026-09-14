# Use a small, official base image
FROM python:3.11-slim

# Create a non-root user for better security (Docker best practice)
RUN useradd -m appuser

WORKDIR /app

# Copy dependency file first to leverage Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Switch to non-root user
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]