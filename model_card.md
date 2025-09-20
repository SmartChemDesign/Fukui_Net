# FukuiNet

FukuiNet predicts Fukui indices using Kernel-based Attention Networks (KAN) with Chebyshev graph convolutions.

## Model Description

FukuiNet predicts Fukui indices - quantum chemical descriptors that quantify molecular reactivity. The model uses:

- **Graph Neural Networks**: Molecular structure as graphs
- **Kernel-based Attention Networks (KAN)**: Advanced attention mechanisms
- **Chebyshev Convolutions**: Efficient graph operations
- **RDKit Integration**: Molecular featurization

## Usage

```python
from transformers import AutoModel

model = AutoModel.from_pretrained("Nikolenko-Sergei/FukuiNet", trust_remote_code=True)
fukui_indices = model.predict("CCO")  # Ethanol
```

## Training Details

- **Epochs**: 65
- **Global Steps**: 6,204
- **Framework**: PyTorch Lightning 2.2.1

## Applications

- Drug discovery and ADMET prediction
- Catalyst design
- Material science
- Reaction mechanism analysis

## Citation

```bibtex
@software{fukui_net,
  title={FukuiNet: Predicting Fukui Indices with Kernel-based Attention Networks},
  author={Nikolenko, Sergei},
  year={2024},
  url={https://huggingface.co/Nikolenko-Sergei/FukuiNet}
}
```

## License

MIT License