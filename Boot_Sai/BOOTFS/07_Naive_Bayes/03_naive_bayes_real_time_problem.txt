# ============================================================
# NAIVE BAYES CLASSIFIER ON ANY DATASET - REAL-TIME PROBLEM
# Problem: Medical screening - predict whether a breast tumour is
# MALIGNANT or BENIGN from cell measurements, then classify a
# "new patient" record entered at run time.
# Dataset: sklearn Breast Cancer Wisconsin (569 records, 30 features)
# Also shows Naive Bayes computed BY HAND on a tiny weather dataset.
# Run: python 03_naive_bayes_real_time_problem.txt
# ============================================================
from sklearn.datasets import load_breast_cancer
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

# ---------------- PART 1 : sklearn on a real dataset ----------------
data = load_breast_cancer()
X, y = data.data, data.target                   # 0 = malignant, 1 = benign
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=1, stratify=y)

model = GaussianNB()
model.fit(Xtr, ytr)
pred = model.predict(Xte)

print("===== PART 1: Breast cancer screening =====")
print("Training records:", len(Xtr), "| Test records:", len(Xte))
print("Accuracy :", round(accuracy_score(yte, pred), 3))
print("Precision:", round(precision_score(yte, pred), 3))
print("Recall   :", round(recall_score(yte, pred), 3))
print("Confusion matrix:\n", confusion_matrix(yte, pred))

new_patient = Xte[0:1]                           # simulate a new record
p = model.predict_proba(new_patient)[0]
print(f"\nNew patient -> {data.target_names[p.argmax()].upper()} "
      f"(P(malignant)={p[0]:.3f}, P(benign)={p[1]:.3f})\n")

# ---------------- PART 2 : Naive Bayes by hand ----------------
# Problem: Will students play cricket today?
weather = [  # (outlook, temperature, play)
    ("sunny", "hot", "no"), ("sunny", "mild", "no"), ("overcast", "hot", "yes"),
    ("rainy", "mild", "yes"), ("rainy", "cool", "yes"), ("rainy", "cool", "no"),
    ("overcast", "cool", "yes"), ("sunny", "mild", "no"), ("sunny", "cool", "yes"),
    ("rainy", "mild", "yes"), ("sunny", "mild", "yes"), ("overcast", "mild", "yes"),
    ("overcast", "hot", "yes"), ("rainy", "mild", "no"),
]

def naive_bayes(outlook, temp):
    scores = {}
    for c in ("yes", "no"):
        rows = [r for r in weather if r[2] == c]
        prior = len(rows) / len(weather)
        p_out = sum(r[0] == outlook for r in rows) / len(rows)
        p_tmp = sum(r[1] == temp for r in rows) / len(rows)
        scores[c] = prior * p_out * p_tmp
        print(f"  P({c}) * P({outlook}|{c}) * P({temp}|{c}) = "
              f"{prior:.3f} * {p_out:.3f} * {p_tmp:.3f} = {scores[c]:.4f}")
    total = sum(scores.values())
    for c in scores:
        print(f"  Posterior P({c} | {outlook}, {temp}) = {scores[c] / total:.3f}")
    return max(scores, key=scores.get)

print("===== PART 2: Naive Bayes by hand =====")
print("Prediction for (sunny, cool):", naive_bayes("sunny", "cool").upper())
