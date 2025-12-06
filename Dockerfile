# 1. Use a lightweight Python base image
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the requirements file first (for better caching)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code
COPY . .

# 6. Expose the port Streamlit uses
EXPOSE 8501

# 7. Command to run the app when container starts
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]