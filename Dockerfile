# Use official Python slim image
FROM python:3.13-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first to install dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory contents to /app in container
COPY . .

# Run the app with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
