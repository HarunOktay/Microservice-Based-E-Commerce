FROM python:3.9-slim

WORKDIR /app

# Gerekli paketleri kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyala
COPY . .

# Streamlit konfigürasyonu
ENV PORT=8501
EXPOSE 8501

# protobuf için çözüm
ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

# Streamlit'i çalıştır
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"] 