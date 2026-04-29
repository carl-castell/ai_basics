
import os
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import subprocess

# ============================================================
# CONFIG — edit these for each experiment
# ============================================================
EXPERIMENT_ID = "EXP-0"

HIDDEN_LAYERS = [50,50]
ACTIVATION    = "tanh"
OPTIMIZER     = "adam"
EPOCHS        = 25
BATCH_SIZE    = 32
# ============================================================


#Load and split data
data = pd.read_csv("input/data.csv")
data.drop(["FareClass"], axis=1, inplace=True)

feature_cols = ["Sex", "Embarked", "Title_1", "Title_2", "Title_3", "Title_4",
                "Title_5", "Age_1", "Age_2", "Age_3", "Age_4", "Age_5",
                "Family_Alone", "Family_Small", "Family_Large", "Pclass_2", "Pclass_3"]
X, y = data[feature_cols], data["Survived"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)


#Build model
layers = [tf.keras.layers.Input(shape=(X_train.shape[1],))]
for n in HIDDEN_LAYERS:
    layers.append(tf.keras.layers.Dense(n, activation=ACTIVATION))
layers.append(tf.keras.layers.Dense(1, activation="sigmoid"))

model = tf.keras.Sequential(layers)
model.compile(optimizer=OPTIMIZER, loss="binary_crossentropy", metrics=["accuracy"])


#Train
history = model.fit(X_train, y_train,
                    epochs=EPOCHS, batch_size=BATCH_SIZE,
                    validation_data=(X_test, y_test), verbose=1)


#Save loss plot
os.makedirs("docs/plots", exist_ok=True)
plt.figure()
plt.plot(history.history["loss"], label="train_loss")
plt.plot(history.history["val_loss"], label="val_loss")
plt.title(f"Loss — {EXPERIMENT_ID}")
plt.xlabel("epoch")
plt.ylabel("loss")
plt.legend()
plt.savefig(f"docs/plots/{EXPERIMENT_ID}.png", dpi=100, bbox_inches="tight")
plt.close()


#Compute metrics
y_pred = np.rint(model.predict(X_test, verbose=0))
cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm[0, 0], cm[0, 1], cm[1, 0], cm[1, 1]

accuracy  = (tn + tp) / cm.sum()
precision = tp / (fp + tp) if (fp + tp) else 0
recall    = tp / (fn + tp) if (fn + tp) else 0
f1        = 2 * precision * recall / (precision + recall) if (precision + recall) else 0
train_acc = history.history["accuracy"][-1]

# Build markdown block
md_block = f"""### Run {EXPERIMENT_ID}

**Config**
- Hidden layers: {HIDDEN_LAYERS}
- Activation: {ACTIVATION}
- Optimizer: {OPTIMIZER}
- Epochs: {EPOCHS}
- Batch size: {BATCH_SIZE}

**Results**
- Train accuracy: {train_acc:.3f}
- Test accuracy: {accuracy:.3f}
- Precision: {precision:.3f}
- Recall: {recall:.3f}
- F1: {f1:.3f}

![](plots/{EXPERIMENT_ID}.png)

**Confusion matrix**

|  | Predicted Dead | Predicted Survived |
|---|---|---|
| **Actual Dead** | {tn} | {fp} |
| **Actual Survived** | {fn} | {tp} |

**Observation:**

---"""

#print and copy to clipboard
print("\n" + "=" * 60)
print("MARKDOWN BLOCK (also copied to clipboard)")
print("=" * 60 + "\n")
print(md_block)

try:
    subprocess.run(["pbcopy"], input=md_block, text=True, check=True)
    print("\n✓ Copied to clipboard. Paste into docs/experiments.md.")
except (subprocess.CalledProcessError, FileNotFoundError):
    print("\n(Clipboard copy failed — paste manually from above.)")