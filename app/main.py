from typing import Optional, List, Dict
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from vllm import LLM, SamplingParams
import logging
import os

# 配置日誌
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="vLLM Inference API")

# 模型配置
MODEL_PATH = os.getenv("MODEL_PATH", "/model/open_llama_7b")
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "512"))

# 初始化 vLLM
try:
    llm = LLM(
        model=MODEL_PATH,
        # trust_remote_code=True,  # Qwen 需要這個設定
        dtype="float16",
        gpu_memory_utilization=0.85
    )
    logger.info(f"Model loaded successfully from {MODEL_PATH}")
except Exception as e:
    logger.error(f"Error loading model: {str(e)}")
    raise

class GenerateRequest(BaseModel):
    prompt: str
    max_tokens: Optional[int] = Field(default=MAX_TOKENS)
    temperature: Optional[float] = Field(default=0.7)
    top_p: Optional[float] = Field(default=0.95)
    presence_penalty: Optional[float] = Field(default=0.0)
    frequency_penalty: Optional[float] = Field(default=0.0)
    stop: Optional[List[str]] = Field(default=None)

class GenerateResponse(BaseModel):
    text: str
    usage: Dict[str, int]

@app.post("/generate", response_model=GenerateResponse)
async def generate_text(request: GenerateRequest):
    try:
        # 設定採樣參數
        sampling_params = SamplingParams(
            max_tokens=request.max_tokens,
            temperature=request.temperature,
            top_p=request.top_p,
            presence_penalty=request.presence_penalty,
            frequency_penalty=request.frequency_penalty,
            stop=request.stop
        )

        # 生成文本
        outputs = llm.generate([request.prompt], sampling_params)
        generated_text = outputs[0].outputs[0].text

        # 計算 token 使用量
        usage = {
            "prompt_tokens": len(request.prompt.split()),  # 簡單估算
            "completion_tokens": len(generated_text.split()),  # 簡單估算
            "total_tokens": len(request.prompt.split()) + len(generated_text.split())
        }

        return GenerateResponse(text=generated_text, usage=usage)
    
    except Exception as e:
        logger.error(f"Generation error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy", "model_loaded": True}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
