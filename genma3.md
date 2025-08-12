#部署模型
docker run --gpus all \
    -v /home/thhuang/myproject/vllm_implement/models/gemma-3-4b-it:/models/gemma-3-4b-it \
    --env "TRANSFORMERS_OFFLINE=1" \
    -p 9999:8000 \
    --ipc=host \
    --name vllm \
    vllm/vllm-openai:v0.10.0 \
    --model /models/gemma-3-4b-it


#測試佈署
curl https://10.144.84.72:9999/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "/models/gemma-3-4b-it",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"}
        ]
    }'