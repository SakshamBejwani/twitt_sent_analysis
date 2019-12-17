twitter_data = open("project_twitter_data.csv", "r")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(sentences):
    count_pos = 0
    sentences = strip_punctuation(sentences)
    lst_sentences = sentences.split()

    for words in lst_sentences:
        for pos in positive_words:
            if words == pos:
                count_pos += 1
    return count_pos

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(sentences2):
    count_neg = 0
    sentences2 = strip_punctuation(sentences2)
    lst_sentences2 = sentences2.split()

    for words in lst_sentences2:
        for neg in negative_words:
            if words == neg:
                count_neg += 1
    return count_neg

def strip_punctuation(words):
    for word in punctuation_chars:
        words = words.replace(word, "")
    return words

resulting_data = open("resulting_data.csv", "w")
twitter_data = twitter_data.readlines()
resulting_data.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
resulting_data.write("\n")

retweet = 0
reply = 0
pos_score = 0 
neg_score = 0
net_score = 0

for x in twitter_data[1:]:
    pos_score = get_pos(x)
    neg_score = get_neg(x)
    net_score = get_pos(x) - get_neg(x)
    lst = list(x.split(","))
    resulting_data.write("{},{},{},{},{}".format(int(lst[-2]),int(lst[-1]),pos_score,neg_score,net_score))
    resulting_data.write('\n')
