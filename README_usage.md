# vLLM API 使用指南

## 1. 使用測試腳本

我們提供了一個簡單的測試腳本 `test_api.py`，您可以這樣使用：

```bash
# 使用預設提示詞
python app/test_api.py

# 使用自定義提示詞
python app/test_api.py "請解釋量子電腦的原理"
```

## 2. 直接調用 API

### 文本生成 API

**端點：** `POST http://localhost:8000/generate`

**請求格式：**
```json
{
    "prompt": "您的提示詞",
    "max_tokens": 512,      // 可選，預設值 512
    "temperature": 0.7,     // 可選，預設值 0.7
    "top_p": 0.95,         // 可選，預設值 0.95
}
```

**使用 curl 的例子：**
```bash
curl -X POST "http://localhost:8000/generate" \
     -H "Content-Type: application/json" \
     -d '{
           "prompt": "請解釋什麼是人工智慧？",
           "max_tokens": 512,
           "temperature": 0.7
         }'
```

**使用 Python requests 的例子：**
```python
import requests
import json

url = "http://localhost:8000/generate"
payload = {
    "prompt": "請解釋什麼是人工智慧？",
    "max_tokens": 512,
    "temperature": 0.7
}

response = requests.post(url, json=payload)
result = response.json()
print(result["text"])  # 輸出生成的文本
print(result["usage"]) # 輸出 token 使用統計
```

### 健康檢查 API

可以使用以下命令檢查服務是否正常運行：

```bash
curl http://localhost:8000/health
```

## API 參數說明

- `prompt`: 要處理的輸入文本
- `max_tokens`: 生成文本的最大長度
- `temperature`: 控制文本生成的隨機性（0.0-1.0）
  - 較高的值（如 0.8）會產生更多樣化的輸出
  - 較低的值（如 0.2）會產生更確定性的輸出
- `top_p`: 控制採樣的範圍（0.0-1.0）
- `presence_penalty`: 控制主題重複度（-2.0 到 2.0）
- `frequency_penalty`: 控制詞彙重複度（-2.0 到 2.0）

## 回應格式

```json
{
    "text": "生成的文本內容",
    "usage": {
        "prompt_tokens": 10,       // 輸入使用的 token 數
        "completion_tokens": 50,    // 生成使用的 token 數
        "total_tokens": 60         // 總共使用的 token 數
    }
}
```

## 注意事項

1. 確保服務已經啟動並在運行中
2. 預設服務地址是 `http://localhost:8000`
3. 如果遇到超時，可以調整 `max_tokens` 參數
4. 對於較長的生成任務，建議適當增加請求超時時間
