# Use a base image suitable for both frontend and backend requirements
FROM node:14-alpine AS frontend-builder

# Set working directory for frontend
WORKDIR /app/frontend

# Copy frontend source code
COPY frontend/package*.json ./
RUN yarn install
COPY frontend/ .

# Build frontend
RUN yarn build

# Use another stage for the backend
FROM python:latest AS backend-builder

# Set working directory for backend
WORKDIR /app/backend

# Copy backend source code
COPY backend/requirements.txt ./
RUN pip install -r requirements.txt
COPY backend/ .

# Final stage
FROM python:latest

# Copy files from frontend and backend stages
COPY --from=frontend-builder /app/frontend/build /app/frontend/build
COPY --from=backend-builder /app/backend /app/backend

# Expose any necessary ports
# EXPOSE 3000

# Set working directory
WORKDIR /app/backend

# Commands to run the application
CMD ["python", "scrape.py"]
