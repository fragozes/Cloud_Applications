# Start with Python 3.13
FROM python:3.13
ENV DATABASE_NAME="book_store"
ENV DATABASE_HOST="postgres:password@book_store_db"

# Define onde os comandos vão correr dentro do container
WORKDIR /app


# Copy your project files
COPY . /app

# Install your libraries
RUN pip install --no-cache-dir -r requirements.txt

# Start your app
CMD ["python", "app.py"]