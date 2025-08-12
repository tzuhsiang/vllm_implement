# 目標資料夾可自行調整
TARGET_DIR=/home/thhuang/myproject/vllm_implement/models/gemma-3-12b-it

mkdir -p "$TARGET_DIR"

# 建議先在瀏覽器/HF 上接受 gemma-3-12b-it 的授權，並確認環境有 HF_TOKEN
# 下載時把必需檔案一次抓齊
hf download google/gemma-3-12b-it \
  --local-dir "$TARGET_DIR" \
  --include \
    "config.json" \
    "generation_config.json" \
    "tokenizer.json" \
    "tokenizer.model" \
    "tokenizer_config.json" \
    "special_tokens_map.json" \
    "preprocessor_config.json" \
    "added_tokens.json" \
    "chat_template.json" \
    "model.safetensors.index.json" \
    "model-*.safetensors" \
  --max-workers 1
