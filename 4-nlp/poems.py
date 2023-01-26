import nltk
import string

# cat gutenberg.ndjson | shuf | head -n 10000 | tr "[A-Z]" "[a-z]" | sed -e 's/{"s": "\(.*\)",.*/\1/' -e 's/[[:punct:]]//g' > reduced-gutenberg.txt
with open("data/reduced-gutenberg.txt") as f:
    dataset = [nltk.word_tokenize(sentence) + ['$'] for sentence in f.readlines()]

ngrams = 3
train_data, vocab = nltk.lm.preprocessing.padded_everygram_pipeline(ngrams, dataset)
model = nltk.lm.MLE(ngrams)
model.fit(train_data, vocab)

samples = 3
total = 0
theme = 'life'
while samples != 0:
    total += 1
    text = [theme]
    while text[-1] != '$' and len(text) < 20:
        text.append(model.generate(1, text))
    if len(text) > 7 and text[-1] == '$':
        samples -= 1
        print(' '.join(text[0:-1]))

print("Total tries : ", total)
