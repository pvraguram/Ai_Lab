
data = []

n = int(input("Enter number of training words: "))

for i in range(n):
    word = input("Enter word: ").lower()
    label = input("Enter class (spam/not spam): ").lower()
    data.append((word, label))

spam = [x for x, y in data if y == "spam"]
ham = [x for x, y in data if y == "not spam"]

word = input("Enter a word to classify: ").lower()

# Prior probabilities
p_spam = len(spam) / len(data)
p_ham = len(ham) / len(data)

# Likelihood with Laplace smoothing
p_word_spam = (spam.count(word) + 1) / (len(spam) + 2)
p_word_ham = (ham.count(word) + 1) / (len(ham) + 2)

# Bayes scores (the common denominator is omitted)
score_spam = p_word_spam * p_spam
score_ham = p_word_ham * p_ham

if score_spam > score_ham:
    print("Spam")
else:
    print("Not Spam")
