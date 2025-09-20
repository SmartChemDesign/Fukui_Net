# FukuiNet

FukuiNet is a neural network for predicting Fukui indices using Kernel-based Attention Networks (KAN) with Chebyshev graph convolutions.

## Model Description

FukuiNet predicts Fukui indices, which are quantum chemical descriptors that quantify the reactivity of atoms within a molecule. The model uses:

- **Graph Neural Networks**: Processes molecular structure as graphs
- **Kernel-based Attention Networks (KAN)**: Advanced attention mechanisms
- **Chebyshev Convolutions**: Efficient graph convolution operations
- **RDKit Integration**: Molecular featurization

## Model Architecture

- Input: SMILES strings representing molecules
- Graph Construction: RDKit converts SMILES to molecular graphs
- Featurization: Atom and bond features using RDKit descriptors
- Neural Network: KAN layers with Chebyshev graph convolutions
- Output: Fukui indices for each atom in the molecule

## Training Details

- **Training Data**: Molecular datasets with computed Fukui indices
- **Epochs**: 65
- **Global Steps**: 6,204
- **Framework**: PyTorch Lightning 2.2.1

## Usage

```python
from fukui_net.predictor import FukuiNetPredictor

# Initialize predictor
predictor = FukuiNetPredictor("models/final_model.ckpt", device="cuda:1")

# Predict Fukui indices for a molecule
fukui_indices = predictor.predict_smiles("CCO")  # Ethanol
print(fukui_indices)
```

## Installation

```bash
# Clone the repository
git clone https://huggingface.co/Nikolenko-Sergei/FukuiNet
cd FukuiNet

# Install dependencies
uv sync

# Run prediction
uv run fukui_net predict "CCO" --device cuda:1
```

## Scientific Background

Fukui indices are crucial for:

- Drug discovery and ADMET prediction
- Catalyst design
- Material science applications
- Reaction mechanism analysis

## Citation

If you use this model in your research, please cite:

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
