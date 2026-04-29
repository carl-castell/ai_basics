# Titanic Challenge — SE_14 AI Basics

This is my submission for the Titanic Challenge, part of the SE_14 Artificial
Intelligence Basics module. The task is to train a neural network that predicts
which Titanic passengers survived the sinking, and to systematically experiment
with hyperparameters to find a good model.

The challenge is based on the [Kaggle Titanic competition](https://www.kaggle.com/c/titanic),
and the starter notebook was provided as part of the course. The dataset itself
is from Kaggle (already preprocessed for this exercise).

## What's in this repo

- `notebooks/experiment.py` — the script I use to run a single experiment.
  Edit the config block at the top, run it, and it trains the model, saves a
  loss plot, prints metrics, and copies a ready-to-paste markdown block to the
  clipboard.
- `notebooks/Titanic_Challenge - extended.ipynb` — the original starter notebook.
- `docs/experiments.md` — **the main write-up.** Every experiment I ran is logged
  here, with config, results, confusion matrix, loss plot, and my observations.
- `docs/plots/` — saved loss plots from each run.
- `input/data.csv` — the dataset.
- `requirements.txt` — Python dependencies.

👉 **[Read the experiments and discussion in docs/experiments.md](docs/experiments.md)**

## How it works

For each run:

1. Edit the config block in `experiment.py`
2. Run the script
3. Paste the markdown output into `experiments.md`


## Setup (macOS)

These instructions assume you're on macOS with Homebrew installed.

### 1. Install Python 3.12

TensorFlow doesn't yet support Python 3.13+, so we use 3.12.

```bash
brew install python@3.12
```

### 2. Clone the repo and create a virtual environment

```bash
git clone https://github.com/carl-castell/ai_basics.git
cd ai_basics
python3.12 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt now.

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run an experiment

```bash
python notebooks/experiment.py
```

The first run is the baseline. To try a different configuration, open
`notebooks/experiment.py` and edit the values in the CONFIG block at the top
(experiment ID, hidden layers, optimizer, etc.), then run it again.

## Credits

- The challenge is based on the [Kaggle Titanic competition](https://www.kaggle.com/c/titanic).
- The starter notebook and preprocessed dataset were provided as part of the
  SE_14 AI Basics course.