import requests
import json
import sys

def test_generate(prompt: str, url: str = "http://localhost:8000"):
    """測試文本生成 API"""
    
    # API 請求的資料
    payload = {
        "prompt": prompt,
        "max_tokens": 512,
        "temperature": 0.7,
        "top_p": 0.95
    }

    try:
        # 發送 POST 請求到 /generate 端點
        response = requests.post(
            f"{url}/generate",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        # 檢查回應狀態
        response.raise_for_status()
        
        # 解析回應
        result = response.json()
        
        print("\n=== 生成結果 ===")
        print(f"生成的文本: {result['text']}")
        print("\n=== Token 使用統計 ===")
        print(f"Prompt tokens: {result['usage']['prompt_tokens']}")
        print(f"Completion tokens: {result['usage']['completion_tokens']}")
        print(f"Total tokens: {result['usage']['total_tokens']}")
        
    except requests.exceptions.RequestException as e:
        print(f"API 請求錯誤: {e}")
        if hasattr(e.response, 'text'):
            print(f"錯誤詳情: {e.response.text}")
        sys.exit(1)

def test_health(url: str = "http://localhost:8000"):
    """測試健康檢查端點"""
    
    try:
        response = requests.get(f"{url}/health")
        response.raise_for_status()
        result = response.json()
        print("\n=== 健康檢查 ===")
        print(f"狀態: {result['status']}")
        print(f"模型載入: {result['model_loaded']}")
        
    except requests.exceptions.RequestException as e:
        print(f"健康檢查錯誤: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # 預設的測試提示
    default_prompt = "請用繁體中文解釋什麼是人工智慧？"
    
    # 從命令列參數獲取提示，如果沒有提供就使用預設值
    prompt = sys.argv[1] if len(sys.argv) > 1 else default_prompt
    
    # 執行測試
    print("開始測試 vLLM API...")
    test_health()
    test_generate(prompt)
    print("\n測試完成!")
