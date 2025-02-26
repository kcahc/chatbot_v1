FROM python:3.10

WORKDIR /app
COPY . /app

# Install both backend and frontend dependencies
RUN pip install --no-cache-dir -r backend/requirements.txt
RUN pip install --no-cache-dir -r frontend/requirements.txt

# Expose the backend port
EXPOSE 8000

# Run the FastAPI app; you can adjust the command to include the frontend if desired
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]
