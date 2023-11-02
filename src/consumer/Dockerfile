# Use the official Python image from the dockerhub
FROM python:3.11

# Set the work directory in docker
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY consumer.py .

# Specify the command to run on container start
CMD ["python", "consumer.py"]
