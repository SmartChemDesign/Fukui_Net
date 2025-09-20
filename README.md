# Fukui_Net

Neural network for predicting Fukui indices using Kernel-based Attention Networks (KAN) with Chebyshev graph convolutions.

## Installation

```bash
# Clone and install
git clone <repository-url>
cd Fukui_Net
uv sync
```

## Usage

### Device Information

Check available devices and model status:

```bash
uv run fukui_net info
```

### Single Molecule Prediction

```bash
# Using CPU
uv run fukui_net predict "CCO" --device cpu

# Using GPU
uv run fukui_net predict "CCO" --device cuda:1
```

### Batch Prediction

```bash
uv run fukui_net predict \
    --csv molecules.csv \
    --output predictions.csv \
    --device cuda:1
```

**Input CSV format:**
```csv
smiles,name
CCO,Ethanol
c1ccccc1,Benzene
```

**Output CSV format:**
```csv
smiles,fukui_indices
CCO,"[0.123, -0.045, 0.234, ...]"
c1ccccc1,"[-0.089, 0.156, ...]"
```

## Model Architecture

- **Graph Neural Network**: Processes molecular structure as graphs
- **Kernel-based Attention Networks (KAN)**: Advanced attention mechanisms
- **Chebyshev Convolutions**: Efficient graph convolution operations
- **RDKit Integration**: Molecular featurization


## License

MIT License