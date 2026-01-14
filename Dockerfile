# ------------------------------
# Base Image (Small & Fast)
# ------------------------------
FROM python:3.10-slim


# ------------------------------
# Environment Variables
# ------------------------------
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1
  

# ------------------------------
# Working Directory
# ------------------------------
WORKDIR /usr/app


# ------------------------------
# System Dependencies
# ------------------------------
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc curl && \
    rm -rf /var/lib/apt/lists/*


# ------------------------------
# Copy dependency files first
# (Better Docker layer caching)
# ------------------------------
# Install Python Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# ------------------------------
# Copy Application FrontEnd Code
# ------------------------------
COPY . .


# ------------------------------
# Expose Streamlit Port
# ------------------------------
EXPOSE 8502


# ------------------------------
# Run Streamlit App
# ------------------------------
CMD ["streamlit", "run", "app.py", "--server.headless=true", "--server.port=8502", "--server.address=0.0.0.0"]
