# ============================================================
# NAIVE BAYES - CLASSIFY EMAILS AS SPAM / NOT SPAM
# Evaluates accuracy, precision, recall, F1 and confusion matrix.
# Bayes rule: P(spam | words) ∝ P(spam) * Π P(word | spam)
# Run: python 01_naive_bayes_spam_email.txt
# (needs: pip install scikit-learn)
# ============================================================
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, confusion_matrix, classification_report)

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
X = spam + ham
y = [1] * len(spam) + [0] * len(ham)          # 1 = spam, 0 = not spam

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)

vec = CountVectorizer(lowercase=True)
Xtr = vec.fit_transform(X_train)
Xte = vec.transform(X_test)

model = MultinomialNB(alpha=0.1)              # additive (Laplace-type) smoothing
model.fit(Xtr, y_train)
y_pred = model.predict(Xte)

print("Prior P(spam) =", round(model.class_count_[1] / sum(model.class_count_), 2))
print("Accuracy :", round(accuracy_score(y_test, y_pred), 3))
print("Precision:", round(precision_score(y_test, y_pred), 3))
print("Recall   :", round(recall_score(y_test, y_pred), 3))
print("F1 score :", round(f1_score(y_test, y_pred), 3))
print("Confusion matrix [[TN FP] [FN TP]]:\n", confusion_matrix(y_test, y_pred))
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
cv = cross_val_score(make_pipeline(CountVectorizer(), MultinomialNB(alpha=0.1)), X, y, cv=5)
print("5-fold cross-validation accuracy:", round(cv.mean(), 3))
print("\n", classification_report(y_test, y_pred, target_names=["Not Spam", "Spam"]))

for msg in ["Congratulations! You won a free prize, claim now",
            "Can we discuss the lab record tomorrow"]:
    p = model.predict_proba(vec.transform([msg]))[0]
    label = "SPAM" if p[1] > 0.5 else "NOT SPAM"
    print(f"'{msg}' -> {label}  (P(spam) = {p[1]:.2f})")
