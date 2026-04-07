# Training Run Log: [Model Name] — Run [N]

## Metadata

| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD HH:MM UTC] |
| Author | AI/ML Engineer |
| Model | [Model name] |
| Run ID | [MLflow / W&B / Vertex run ID] |
| Experiment | [Experiment name] |
| Skill | model-trainer |
| Status | [Running / Complete / Failed] |
| Compute | [Instance type and count, e.g., 4× A100 80GB] |
| Duration | [X hours Y minutes] |

## Objective

**What are we trying to learn or improve with this run?**
[One sentence: "Testing whether increasing the dropout rate from 0.1 to 0.3 reduces overfitting observed in Run 12."]

**Hypothesis**: [Increasing dropout will reduce the gap between train and validation loss by > 10% without degrading primary metric.]

## Configuration

### Hyperparameters

| Parameter | This Run | Baseline Run | Notes |
|-----------|----------|-------------|-------|
| Learning rate | [X] | [Y] | |
| Batch size | [X] | [Y] | |
| Epochs / Steps | [X] | [Y] | |
| Optimizer | [Adam / AdamW / SGD] | [Y] | |
| Dropout rate | [X] | [Y] | |
| Weight decay | [X] | [Y] | |
| [Model-specific param] | [X] | [Y] | |

### Data

| Property | Value |
|----------|-------|
| Training set | [N samples, date range] |
| Validation set | [N samples, date range] |
| Test set | [N samples, date range — held out until final evaluation] |
| Preprocessing version | [v1.2 — describe key transforms] |
| Data augmentation | [Yes — describe / No] |
| Class balance | [Balanced / Imbalanced X:1 — how handled] |

### Model Architecture

| Component | Specification |
|-----------|--------------|
| Base architecture | [Architecture name and size] |
| Pretrained weights | [Source, e.g., HuggingFace model ID or None] |
| Modification from base | [What layers added/modified/frozen] |
| Total parameters | [X M] |
| Trainable parameters | [X M] |

## Training Metrics

### Loss Curves

| Epoch | Train Loss | Val Loss | Gap (Overfit Signal) |
|-------|-----------|---------|----------------------|
| 1 | [X] | [X] | [X] |
| 5 | [X] | [X] | [X] |
| 10 | [X] | [X] | [X] |
| Best | [X at epoch N] | [X at epoch N] | [X] |
| Final | [X] | [X] | [X] |

**Early stopping triggered**: [Yes at epoch N / No]
**Convergence**: [Converged / Not converged — reason]

### Primary Metric on Validation Set

| Epoch | Metric Value | Best So Far |
|-------|-------------|------------|
| Best | [X] | [X] |

## Evaluation Results

### Validation Set

| Metric | This Run | Baseline | Delta | Status |
|--------|----------|---------|-------|--------|
| [Primary metric] | [X] | [Y] | [+/-] | [Improved/Worse] |
| [Secondary metric 1] | | | | |
| [Secondary metric 2] | | | | |

### Per-Segment Validation

| Segment | Primary Metric | vs. Overall | Notes |
|---------|---------------|-------------|-------|
| [Segment A] | [X] | [+/-X%] | |
| [Segment B] | [X] | | |

## Infrastructure Notes

| Resource | Peak Usage | Notes |
|----------|-----------|-------|
| GPU memory (per GPU) | [X GB / 80 GB] | [Any OOM events?] |
| GPU utilization | [X%] | [Bottleneck in dataloader? Compute-bound?] |
| Training throughput | [X samples/sec] | |
| Total compute cost | [$X] | |

## Issues Encountered

| Issue | Impact | Resolution |
|-------|--------|------------|
| [e.g., NaN loss at epoch 3] | [Run paused 1 hr] | [Reduced LR; gradient clipping added] |

## Conclusions

**Hypothesis confirmed?** [Yes / No / Partially]

**Key findings**:
1. [Finding 1: e.g., "Dropout 0.3 reduced overfitting gap from 0.42 to 0.18 as hypothesized"]
2. [Finding 2]

**Recommended next run**: [e.g., "Test LR schedule with warmup; keep dropout at 0.3"]

**Ready for formal evaluation?** [Yes — proceed to model-evaluation-runner / No — more training needed]

## Artifact Links

| Artifact | Location |
|----------|----------|
| Model checkpoint (best epoch) | [S3 / GCS path] |
| Full run logs | [MLflow / W&B link] |
| Validation predictions | [Path] |
| Training code version | [Git SHA] |
