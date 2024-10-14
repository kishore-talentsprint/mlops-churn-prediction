# Use Python 3.8 as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the necessary files into the container
COPY models/ ./models/
COPY src/ ./src/
COPY requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run the model script
CMD ["python", "src/run_model.py"]
