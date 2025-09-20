# Hugging Face Upload Instructions

## Prerequisites

1. **Get Hugging Face Token**:
   - Go to https://huggingface.co/settings/tokens
   - Create a new token with "Write" permissions
   - Copy the token

2. **Install Git LFS** (if not already installed):
   ```bash
   # Ubuntu/Debian
   sudo apt install git-lfs
   
   # macOS
   brew install git-lfs
   ```

## Upload Steps

1. **Authenticate with Hugging Face**:
   ```bash
   # Set token as environment variable
   export HUGGINGFACE_HUB_TOKEN="your_token_here"
   
   # Or use hf auth login (interactive)
   uv run hf auth login
   ```

2. **Initialize Git LFS**:
   ```bash
   git lfs install
   ```

3. **Add LFS tracking for model files**:
   ```bash
   git lfs track "*.ckpt"
   git lfs track "*.pth"
   git lfs track "*.pt"
   git lfs track "*.bin"
   ```

4. **Push to Hugging Face**:
   ```bash
   git push -u origin main
   ```

## Alternative: Direct Upload

If Git LFS is not available, you can use the Hugging Face CLI:

```bash
# Upload the entire repository
uv run hf upload Nikolenko-Sergei/FukuiNet .

# Upload specific files
uv run hf upload Nikolenko-Sergei/FukuiNet models/final_model.ckpt
uv run hf upload Nikolenko-Sergei/FukuiNet README.md
uv run hf upload Nikolenko-Sergei/FukuiNet model_card.md
```

## Verification

After upload, check your model at:
https://huggingface.co/Nikolenko-Sergei/FukuiNet

The repository should contain:
- ✅ Model checkpoint (`models/final_model.ckpt`)
- ✅ Source code (`fukui_net/`)
- ✅ Documentation (`README.md`, `model_card.md`)
- ✅ Configuration files (`pyproject.toml`, `.gitattributes`)
- ✅ Tests (`tests/`)
