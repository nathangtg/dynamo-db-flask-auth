FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app   
COPY . /app

# Expose port 5000 as default
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app
ENV FLASK_ENV=production

# Run the Flask Application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
