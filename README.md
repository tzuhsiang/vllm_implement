# vLLM API 服務實作

這個專案實作了一個基於 vLLM 的高效能推論 API 服務，使用 Docker 容器化部署。

## 功能特點

- 使用 OpenLLaMA 7B 作為基礎模型
- FastAPI 實作 REST API
- Docker 容器化部署
- GPU 加速支援
- 可配置的代理設定

## 系統需求

- NVIDIA GPU with CUDA support
- Docker
- Docker Compose
- CUDA 驅動版本 >= 11.8

## 專案結構

```
vllm_implement/
├── app/              # API 服務程式碼
│   ├── main.py      # FastAPI 應用程式
│   └── test_api.py  # API 測試腳本
├── config/           # 配置文件
│   └── settings.env # 環境設定
├── env/             # 環境變數
│   └── proxy.env    # 代理設定
├── model/           # 模型存放目錄
├── Dockerfile       # Docker 映像檔配置
└── docker-compose.yml
```

## 快速開始

1. 下載模型並放置到 model 目錄：
```bash
cd model
git clone https://huggingface.co/openlm-research/open_llama_7b
```

2. 配置代理設定（如需要）：
編輯 `env/proxy.env`

3. 啟動服務：
```bash
docker compose up --build
```

4. 測試服務：
```bash
# 使用提供的測試腳本
python app/test_api.py

# 或使用 curl
curl -X POST "http://localhost:8000/generate" \
     -H "Content-Type: application/json" \
     -d '{
           "prompt": "請解釋什麼是人工智慧？",
           "max_tokens": 512,
           "temperature": 0.7
         }'
```

## API 端點

### 生成文本 `/generate`

**請求格式：**
```json
{
    "prompt": "您的提示詞",
    "max_tokens": 512,
    "temperature": 0.7,
    "top_p": 0.95
}
```

### 健康檢查 `/health`

用於確認服務狀態。

## 貢獻

歡迎提交 Issue 或 Pull Request 來改進這個專案。

## 授權

本專案使用 MIT 授權。請注意，使用的語言模型可能有其自己的授權條款。
