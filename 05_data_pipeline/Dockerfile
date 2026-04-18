# 1. Use a lightweight Python base
FROM python:3.11-slim

# 2. Set the working directory
WORKDIR /app

# 3. Copy our requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy our actual script
COPY pipeline.py .

# 5. Run the script (the -u flag ensures we see logs immediately)
CMD ["python", "-u", "pipeline.py"]
