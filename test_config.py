#!/usr/bin/env python3
"""Test that AutoModel works without tokenizer_config.json"""

def test():
    from transformers import AutoModel

    print("Testing AutoModel.from_pretrained() without tokenizer_config.json...")
    model = AutoModel.from_pretrained(".", trust_remote_code=True)

    print("Testing prediction...")
    result = model.predict("CCO")
    print(f"✓ Success: {len(result)} atoms")

    return True

if __name__ == "__main__":
    test()
