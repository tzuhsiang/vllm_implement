# vLLM API 服務實作

這個專案實作了一個基於 vLLM 的高效能推論 API 服務，使用 Docker 容器化部署。

## 功能特點

- 使用 OpenLLaMA 7B 作為基礎模型
- FastAPI 實作 REST API
- Docker 容器化部署
- GPU 加速支援
- 可配置的代理設定
- 使用 Git LFS 管理大型模型文件

## 系統需求

- NVIDIA GPU with CUDA support
- Docker
- Docker Compose
- CUDA 驅動版本 >= 11.8
- Git LFS

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

### 1. 安裝 Git LFS

如果尚未安裝 Git LFS，請先安裝：

```bash
# Ubuntu/Debian
sudo apt install git-lfs

# macOS
brew install git-lfs

# 初始化 Git LFS
git lfs install
```

### 2. 克隆專案（包含模型）

```bash
# 克隆專案（這會自動下載模型文件）
git clone https://github.com/tzuhsiang/vllm_implement.git
cd vllm_implement

# 如果模型文件沒有自動下載，手動執行：
git lfs pull
```

> 注意：模型文件較大，下載可能需要一些時間。確保您有足夠的網路帶寬和磁碟空間。

### 3. 配置代理設定（如需要）

```bash
# 複製代理設定範本
cp env/proxy.env.example env/proxy.env

# 編輯代理設定
vim env/proxy.env  # 或使用其他編輯器
```

修改 `env/proxy.env` 中的代理設定：
```ini
HTTP_PROXY=http://your-proxy-server:port
HTTPS_PROXY=http://your-proxy-server:port
NO_PROXY=localhost,127.0.0.1
```

### 4. 啟動服務

```bash
docker compose up --build
```

### 5. 測試服務

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

## 故障排除

### 模型文件下載問題

如果遇到模型文件下載問題：

1. 確認已安裝 Git LFS：
```bash
git lfs install
```

2. 強制重新下載 LFS 文件：
```bash
git lfs fetch --all
git lfs pull
```

3. 檢查代理設定：
如果在代理環境中，確保 Git 也配置了正確的代理：
```bash
git config --global http.proxy http://proxy-server:port
```

## 貢獻

歡迎提交 Issue 或 Pull Request 來改進這個專案。

## 授權

本專案使用 MIT 授權。請注意，使用的語言模型可能有其自己的授權條款。
