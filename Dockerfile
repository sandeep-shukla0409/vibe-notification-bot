# Use official Python base image
FROM python:3.11-slim

ENV PYTHONPATH=/app
# Set working directory inside the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .
COPY webserver/ webserver/
COPY test/ test/

# Expose the Flask port
EXPOSE 8080

RUN useradd -m appuser
USER appuser

# Run the app
CMD ["python", "app.py"]