import sys
import string
import re
import json

def senti_scor(text_parsed,sentiment_dict):
    tot_sentiment = 0.0
    for word in text_parsed:
        try:
            tot_sentiment += sentiment_dict[word]
        except KeyError:
            tot_sentiment += 0.0
    return tot_sentiment

def senti_dic(sentiment_file_path):
    sentiment_file = open(sentiment_file_path,'r')
    sentiment_dict = dict()
    for line in sentiment_file.readlines():
        line_sp =  line[:-1].split("\t")
        try:
            sentiment_dict[line_sp[0]] = int(line_sp[1])
        except ValueError:
            sentiment_dict[line_sp[0]] = 0
    return sentiment_dict

def twit_txt(line):
    tweet = json.loads(line[:-1],encoding='utf-8')
    try:
        tweet_text = tweet['text']
    except KeyError:
        tweet_text = ""    
    text_parsed = re.sub('[^A-Za-z0-9 @]+','',tweet_text).split(" ")
    return text_parsed

def twit_scor(tweet_file_path, sentiment_dict):
    tweets_scored = []
    data = open(tweet_file_path,'r')
    for line in data.readlines():
        text_parsed = twit_txt(line)
        for word in text_parsed:
            score = senti_scor(text_parsed,sentiment_dict)   
        tweets_scored.append( (text_parsed, score) )
    return tweets_scored

def tms_us(tweets):
    terms_all = []
    try:
        terms_all.remove("")
    except ValueError:
        pass
    for tweet in tweets:
        for word in tweet[0]:
            terms_all.append(word)
    terms_used = set(terms_all)
    return terms_used

def old_tms(terms,sentiment_dict):
    terms_old = [key for key in sentiment_dict]
    terms_new = terms.difference(terms_old)
    return terms_new   

def scor_tms(terms,tweets_scored):
    terms_observed = { item: [0,0] for item in terms if len(item) > 2} 
    for tweet in tweets_scored:
        for word in tweet[0]:
            try:
                terms_observed[word][0] += tweet[1]
                terms_observed[word][1] += 1
            except KeyError:
                pass
    terms_scored = { key:  terms_observed[key][0]/terms_observed[key][1] for key in terms_observed }
    return terms_scored
    
def main():
    sent_file_path = (sys.argv[1])
    tweet_file_path = (sys.argv[2])

    sentiment_dict = senti_dic(sent_file_path)
    tweets_scored = twit_scor(tweet_file_path, sentiment_dict)

    terms_all = tms_us(tweets_scored)
    terms_new = old_tms(terms_all,sentiment_dict)
    res = scor_tms(terms_new, tweets_scored)

    for key in res:
        print key, res[key]
                     
if __name__ == '__main__':
    main()

