# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir -r Requirements.txt

# Create the data directory
RUN mkdir -p /data

# Mount the data volume
VOLUME ["/data"]

# Run the testweb.py script
CMD ["python", "testweb.py"]
