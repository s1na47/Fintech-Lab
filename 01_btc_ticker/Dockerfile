# 1. Base Image: Use Alpine (Same tech as Busybox)
FROM python:3.9-alpine

# 2. Set directory
WORKDIR /app

# 3. Copy files
COPY requirements.txt .
COPY main.py .

# 4. Install dependencies 
# (Alpine needs no-cache to keep it small)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Run it
CMD ["python", "-u", "main.py"]