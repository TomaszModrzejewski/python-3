# coding=UTF-8
import nltk
from nltk.corpus import brown
import os

# This is a fast and simple noun phrase extractor (based on NLTK)
# Feel free to use it, just keep a link back to this post
# http://thetokenizer.com/2013/05/09/efficient-way-to-extract-the-main-topics-of-a-sentence/
# http://www.sharejs.com/codes/
# Create by Shlomi Babluki
# May, 2013


# This is our fast Part of Speech tagger
#############################################################################
brown_train = brown.tagged_sents(categories='news')
regexp_tagger = nltk.RegexpTagger(
    [(r'^-?[0-9]+(.[0-9]+)?$', 'CD'),
     (r'(-|:|;)$', ':'),
     (r'\'*$', 'MD'),
     (r'(The|the|A|a|An|an)$', 'AT'),
     (r'.*able$', 'JJ'),
     (r'^[A-Z].*$', 'NNP'),
     (r'.*ness$', 'NN'),
     (r'.*ly$', 'RB'),
     (r'.*s$', 'NNS'),
     (r'.*ing$', 'VBG'),
     (r'.*ed$', 'VBD'),
     (r'.*', 'NN')
     ])
unigram_tagger = nltk.UnigramTagger(brown_train, backoff=regexp_tagger)
bigram_tagger = nltk.BigramTagger(brown_train, backoff=unigram_tagger)
#############################################################################


# This is our semi-CFG; Extend it according to your own needs
#############################################################################
cfg = {
    "NNP+NNP": "NNP",
    "NN+NN": "NNI",
    "NNI+NN": "NNI",
    "JJ+JJ": "JJ",
    "JJ+NN": "NNI",
}
#############################################################################


class NPExtractor(object):

    def __init__(self, sentence):
        self.sentence = sentence

    # Split the sentence into singlw words/tokens
    def tokenize_sentence(self, sentence):
        return nltk.word_tokenize(sentence)

    # Normalize brown corpus' tags ("NN", "NN-PL", "NNS" > "NN")
    def normalize_tags(self, tagged):
        n_tagged = []
        for t in tagged:
            if t[1] in ["NP-TL", "NP"]:
                n_tagged.append((t[0], "NNP"))
                continue
            if t[1].endswith("-TL"):
                n_tagged.append((t[0], t[1][:-3]))
                continue
            if t[1].endswith("S"):
                n_tagged.append((t[0], t[1][:-1]))
                continue
            n_tagged.append((t[0], t[1]))
        return n_tagged

    # Extract the main topics from the sentence
    def extract(self):

        tokens = self.tokenize_sentence(self.sentence)
        tags = self.normalize_tags(bigram_tagger.tag(tokens))

        merge = True
        while merge:
            merge = False
            for x in range(len(tags) - 1):
                t1 = tags[x]
                t2 = tags[x + 1]
                key = f"{t1[1]}+{t2[1]}"
                if value := cfg.get(key, ''):
                    merge = True
                    tags.pop(x)
                    tags.pop(x)
                    match = f"{t1[0]} {t2[0]}"
                    pos = value
                    tags.insert(x, (match, pos))
                    break

        return [t[0] for t in tags if t[1] in ["NNP", "NNI"]]


# Main method, just run "python np_extractor.py"
def main():
    path = '.'
    for file in os.listdir(path):
        if file.endswith('.txt'):
            text = []
            with open(file, 'rt') as f:
                for line in f:
                    words = line.split()
                    text += words
            str_text=' '.join(text)
            np_extractor = NPExtractor(str_text)
            result = np_extractor.extract()
            print(f'This file is about: {", ".join(result)}')
if __name__ == '__main__':
    main()
