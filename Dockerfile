FROM nvidia/cuda:12.1.0-devel-ubuntu22.04

# 從構建參數設定代理
ARG HTTP_PROXY
ARG HTTPS_PROXY

# 設定環境變數
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV HTTP_PROXY=$HTTP_PROXY
ENV HTTPS_PROXY=$HTTPS_PROXY

# 安裝系統依賴
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

# 安裝 Python 套件
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# 設定工作目錄
WORKDIR /app

# 複製應用程式代碼
COPY ./app /app

# 啟動命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
