# Use an official Python runtime as a parent image
FROM python:3.11-slim-bookworm

# Set environment variables for Python
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE employee_management.settings

# Create and set the working directory
RUN mkdir /app
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY .. /app/

# Expose the port the application runs on
EXPOSE 8000

# Start the application
CMD ["sh", "start.sh"]
