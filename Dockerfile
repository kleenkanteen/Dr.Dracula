# Minimal base image
#FROM alpine:latest
FROM python:latest

# Container working directory
#WORKDIR /app

# Copy the application code into the container
COPY main.py /

# Install any dependencies or build the application
# Example commands:
# RUN npm install
# RUN pip install -r requirements.txt
# RUN mvn clean package

# Expose the port on which the app runs
#EXPOSE 3000

# Commands to run the application
CMD ["python", "./main.py"]
