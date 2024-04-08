# Use the official Python image as the base image
FROM python:3.8-slim

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Set up a working directory
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt requirements.txt

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Expose the port your app runs on (usually 5000)
EXPOSE 5000

# Command to run the Flask app
CMD ["flask", "run"]
