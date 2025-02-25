# vLLM 推論服務

這是一個使用 vLLM 建立的高效能 LLM 推論服務。本專案使用 Docker 進行容器化部署，並提供 REST API 介面。

## 系統需求

- NVIDIA GPU with CUDA support
- Docker
- Docker Compose
- CUDA 驅動版本 >= 11.8

## 專案結構

```
vllm_implement/
├── app/
│   ├── main.py          # FastAPI 應用程式
│   └── test_api.py      # API 測試腳本
├── config/
│   └── settings.env     # 環境變數配置
├── model/               # 模型存放目錄
├── docker-compose.yml   # Docker Compose 配置
├── Dockerfile          # Docker 映像檔配置
└── requirements.txt    # Python 套件依賴
```

## 快速開始

1. 複製模型檔案到 model 目錄：
   ```bash
   # 將您的模型檔案放到 model 目錄中
   cp /path/to/your/model/* ./model/
   ```

2. 配置環境變數：
   - 檢查並修改 `config/settings.env` 中的設定
   - 特別注意 `MODEL_PATH` 和 GPU 相關設定

3. 啟動服務：
   ```bash
   docker compose up --build
   ```

4. 測試服務：
   ```bash
   # 在另一個終端中執行測試腳本
   python app/test_api.py "您的測試文本"
   ```

## API 端點

### 1. 文本生成 `/generate`

**請求範例：**
```bash
curl -X POST "http://localhost:8000/generate" \
     -H "Content-Type: application/json" \
     -d '{
       "prompt": "請用繁體中文解釋什麼是人工智慧？",
       "max_tokens": 512,
       "temperature": 0.7,
       "top_p": 0.95
     }'
```

### 2. 健康檢查 `/health`

**請求範例：**
```bash
curl "http://localhost:8000/health"
```

## 配置說明

### 環境變數

可在 `config/settings.env` 中配置以下參數：

- `MODEL_PATH`: 模型路徑
- `MAX_TOKENS`: 最大生成 token 數
- `HOST`: 服務主機
- `PORT`: 服務連接埠
- `CUDA_VISIBLE_DEVICES`: 使用的 GPU 設備
- `GPU_MEMORY_UTILIZATION`: GPU 記憶體使用率
- `MAX_NUM_BATCHED_TOKENS`: 批次處理的最大 token 數

## 故障排除

1. 如果遇到 CUDA 錯誤：
   - 確認 NVIDIA 驅動版本是否符合要求
   - 檢查 GPU 是否被正確識別

2. 如果服務無法啟動：
   - 檢查日誌輸出
   - 確認 model 目錄中是否有正確的模型檔案
   - 驗證環境變數設定

3. 如果 API 回應過慢：
   - 調整 `MAX_NUM_BATCHED_TOKENS`
   - 檢查 GPU 記憶體使用情況

## 注意事項

- 請確保 model 目錄中放置了正確的模型檔案
- 建議在生產環境中調整 `settings.env` 中的參數以優化效能
- 使用代理伺服器時，請確認 `docker-compose.yml` 中的代理設定正確
