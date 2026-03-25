FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server.py .
COPY math_mcp_server.py .
COPY perf_mcp_server.py .

EXPOSE 8080

CMD ["python", "server.py"]
