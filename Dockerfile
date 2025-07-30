# Use an official Python runtime as a base image
FROM python:3.11-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy requirements.txt first if it exists
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the port your app runs on (adjust if needed)
EXPOSE 8000

# Command to run your Python application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"]

