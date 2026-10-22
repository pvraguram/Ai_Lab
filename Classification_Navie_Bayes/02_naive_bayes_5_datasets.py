# ============================================================
# NAIVE BAYES ON 5 DIFFERENT REAL-WORLD DATASETS
# All datasets are built into scikit-learn (no download needed):
#   1. Iris            - flower species
#   2. Wine            - wine cultivar
#   3. Breast Cancer   - malignant / benign tumour (medical)
#   4. Digits          - handwritten digit recognition
#   5. SMS/Email spam  - small text dataset (MultinomialNB)
# Metrics: accuracy, precision, recall, F1 (macro average)
# Run: python 02_naive_bayes_5_datasets.txt
# ============================================================
from sklearn.datasets import load_iris, load_wine, load_breast_cancer, load_digits
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

results = []

def evaluate(name, model, X, y):
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3,
                                          random_state=42, stratify=y)
    model.fit(Xtr, ytr)
    p = model.predict(Xte)
    results.append((name, len(y), accuracy_score(yte, p),
                    precision_score(yte, p, average='macro', zero_division=0),
                    recall_score(yte, p, average='macro', zero_division=0),
                    f1_score(yte, p, average='macro', zero_division=0)))

# 1-4: numeric datasets -> Gaussian Naive Bayes
for name, loader in [("Iris", load_iris), ("Wine", load_wine),
                     ("Breast Cancer", load_breast_cancer), ("Digits", load_digits)]:
    d = loader()
    evaluate(name, GaussianNB(), d.data, d.target)

# 5: text dataset -> Multinomial Naive Bayes
spam = [
    "Congratulations you won a free lottery ticket claim now",
    "Win cash prize now click the link",
    "Claim your free reward today limited offer",
    "You have been selected for a free iPhone",
    "Free money waiting for you click here",
    "Urgent your account will be suspended verify now",
    "Earn 5000 rupees per day from home",
    "Exclusive deal buy now get 90 percent off",
    "You won a gift card claim your prize",
    "Cheap loans approved instantly apply now",
    "Lowest price guaranteed offer expires tonight",
    "Winner selected send your bank details to claim",
    "Get rich quick investment double your money",
    "Free entry to win a car text WIN now",
    "Act now limited time free bonus credit",
]
ham = [
    "Call me when you reach home",
    "Can we meet tomorrow for the project discussion",
    "Please submit the assignment before Friday",
    "Your class starts at 10 AM in room 204",
    "Let's have lunch today at the canteen",
    "The lab exam is scheduled for next Monday",
    "Please review the attached report and send feedback",
    "Happy birthday have a great day",
    "Meeting moved to 3 PM in the conference room",
    "Can you share the notes from today's lecture",
    "Mom asked you to buy vegetables on the way",
    "The team will present the demo on Thursday",
    "Reminder to pay the hostel fees this week",
    "Are you coming to the seminar tomorrow",
    "I have uploaded the code to the shared folder",
]
texts = spam + ham
labels = [1] * len(spam) + [0] * len(ham)
X_text = CountVectorizer().fit_transform(texts)
evaluate("SMS Spam (text)", MultinomialNB(alpha=0.1), X_text, labels)

print(f"{'Dataset':<18}{'Samples':>8}{'Accuracy':>10}{'Precision':>11}{'Recall':>8}{'F1':>7}")
print("-" * 62)
for n, s, a, p, r, f in results:
    print(f"{n:<18}{s:>8}{a:>10.3f}{p:>11.3f}{r:>8.3f}{f:>7.3f}")
print("\nGaussianNB assumes each feature is normally distributed within a class;")
print("MultinomialNB uses word counts, which suits text classification.")
