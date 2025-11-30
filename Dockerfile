# Base image with Python pre-installed
FROM python:3.11-slim

# Working directory inside container
WORKDIR /app

# Copy dependencies file first (for caching)
COPY requirements.txt .

# Install dependencies without saving cache to reduce image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port for application
EXPOSE 8000

# Command to run when container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
