# Checklist: Model Training Execution

Comprehensive checklist for reproducible, tracked, and production-grade model training. Aligned with MLOps best practices for experiment tracking (MLflow/W&B), distributed training, and artifact management.

## How to Use

Work through each section in sequence. Mark items `[x]` when verified. Items marked `[REQUIRED]` are non-negotiable — training without them is not production-grade. Items marked `[RECOMMENDED]` are best practices for large or high-stakes models.

---

## Section 1: Pre-Training Data Preparation

- [ ] `[REQUIRED]` Training data loaded from versioned snapshot (DVC tag, dataset hash, or feature store version ID — NOT "latest")
- [ ] `[REQUIRED]` Training data version ID recorded in experiment config
- [ ] `[REQUIRED]` Preprocessing pipeline applied (normalization, encoding, imputation) — same pipeline version as serving
- [ ] `[REQUIRED]` Train/validation/test splits created with stratification on target class
- [ ] `[REQUIRED]` No data leakage across splits verified (time-based split for time-series; hash-based for i.i.d. data)
- [ ] `[REQUIRED]` Class imbalance quantified and handling strategy documented (oversampling, class weights, or no action with rationale)
- [ ] `[RECOMMENDED]` Data profiling run on training split: null rates, value distributions, outlier count per feature

---

## Section 2: Experiment Configuration

- [ ] `[REQUIRED]` Experiment registered in tracking system (MLflow or W&B) with descriptive name and project tag
- [ ] `[REQUIRED]` Random seeds fixed for all sources of randomness: `random.seed`, `np.random.seed`, `torch.manual_seed`, `tf.random.set_seed`
- [ ] `[REQUIRED]` All hyperparameters logged to tracking system before training starts
- [ ] `[REQUIRED]` Model architecture definition committed to version control (not notebook cells)
- [ ] `[REQUIRED]` Dependency versions pinned: `requirements.txt` or `conda env export` committed
- [ ] `[REQUIRED]` GPU/CPU resource allocation documented in experiment config
- [ ] `[RECOMMENDED]` Container image SHA logged as part of experiment metadata

---

## Section 3: Training Execution

- [ ] `[REQUIRED]` Training executed as a script (not a notebook) that can be run from the command line
- [ ] `[REQUIRED]` Model checkpointing enabled: save every N epochs or on validation metric improvement
- [ ] `[REQUIRED]` Training loss and validation metrics logged per epoch to tracking system
- [ ] `[REQUIRED]` Early stopping configured to prevent overfitting (patience = N epochs without validation improvement)
- [ ] `[REQUIRED]` Out-of-memory and CUDA error handling in place
- [ ] `[RECOMMENDED]` Gradient norms logged to detect exploding/vanishing gradients
- [ ] `[RECOMMENDED]` Learning rate schedule logged per step for diagnostics

### For Distributed Training

- [ ] `[REQUIRED]` Distributed training framework configured (PyTorch DDP, Horovod, or managed equivalent)
- [ ] `[REQUIRED]` Worker count and GPU allocation documented
- [ ] `[REQUIRED]` Gradient synchronization strategy documented (all-reduce vs. parameter server)
- [ ] `[RECOMMENDED]` Fault tolerance enabled: training resumes from last checkpoint on worker failure

---

## Section 4: Hyperparameter Tuning

- [ ] `[REQUIRED]` Hyperparameter search space documented with rationale for each parameter range
- [ ] `[REQUIRED]` Tuning method selected and documented: Bayesian optimization (Optuna), random search, or grid search
- [ ] `[REQUIRED]` All trials logged to tracking system (hyperparameters + validation metrics per trial)
- [ ] `[REQUIRED]` Best configuration selected from validation set performance ONLY — test set not touched
- [ ] `[RECOMMENDED]` Bayesian optimization used for > 5 hyperparameters (more efficient than grid search)
- [ ] `[RECOMMENDED]` Sensitivity analysis run on top 3 hyperparameters to understand robustness

---

## Section 5: Artifact Registration

- [ ] `[REQUIRED]` Best model checkpoint registered in model registry (MLflow Model Registry or equivalent)
- [ ] `[REQUIRED]` Following lineage metadata attached to registered model:
  - `training_data_version` (dataset hash or URI)
  - `feature_pipeline_version` (preprocessing pipeline version)
  - `hyperparameters` (full JSON from tracking run)
  - `training_metrics` (all validation metrics at final epoch)
  - `environment_spec` (dependency hash, GPU type)
  - `training_run_id` (tracking system run ID)
- [ ] `[REQUIRED]` Model set to "Staging" state in registry — not "Production" until evaluation passes
- [ ] `[REQUIRED]` Model artifact size documented (MB) for serving feasibility check
- [ ] `[RECOMMENDED]` Lineage hash computed: SHA256(training_data_hash + model_code_hash + hyperparameter_hash)
- [ ] `[RECOMMENDED]` Inference script co-registered with model artifact for serving reproducibility

---

## Section 6: Post-Training Quality Checks

- [ ] `[REQUIRED]` Training loss converged (no divergence; final training loss < initial training loss)
- [ ] `[REQUIRED]` Validation metrics meet minimum acceptable value from model requirements
- [ ] `[REQUIRED]` No significant gap between training and validation performance (< 5% difference indicates no severe overfitting)
- [ ] `[REQUIRED]` Model inference tested locally: sample input → expected output format
- [ ] `[RECOMMENDED]` Learning curves saved as artifacts (loss/metric vs. epoch)
- [ ] `[RECOMMENDED]` Confusion matrix or prediction distribution included in tracking run

---

## Training Completion Sign-Off

| Section | Status | Run ID / Evidence |
|---------|--------|------------------|
| 1. Data Preparation | [ ] Complete / [ ] Partial | |
| 2. Experiment Config | [ ] Complete / [ ] Partial | |
| 3. Training Execution | [ ] Complete / [ ] Partial | |
| 4. HP Tuning | [ ] Complete / [ ] Partial / [ ] Skipped with rationale | |
| 5. Artifact Registration | [ ] Complete / [ ] Partial | |
| 6. Quality Checks | [ ] Complete / [ ] Partial | |

**Training Status**: `[ ] READY FOR EVALUATION` `[ ] NEEDS REWORK — see notes` `[ ] FAILED`

**AI/ML Engineer**: _________________________ Date: _________
