#We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.

#Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.

#To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)
twitter_data = open("project_twitter_data.csv", "r")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
#Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents a one or more sentences, and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurances there are of positive words in the text.
def get_pos(sentences):
    count_pos = 0
    sentences = strip_punctuation(sentences)
    lst_sentences = sentences.split()

    for words in lst_sentences:
        for pos in positive_words:
            if words == pos:
                count_pos += 1
    return count_pos
#Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter, a string which represents a one or more sentences, and calculates how many words in the string are considered negative words. Use the list, negative_words to determine what words will count as negative. The function should return a positive integer - how many occurances there are of negative words in the text.
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
#Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet). Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. Copy the code from the code windows above, and put that in the top of this code window. Now, you will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in that order. Remember that there is another component to this project. You will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets. Check Coursera for that portion of the assignment, if you’re accessing this textbook from Coursera.

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
#By Saksham Bejwani
