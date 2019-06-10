from collections import Counter as CT
from string import punctuation as eng_punc
from zhon.hanzi import punctuation as ch_punc
import jieba
import re

# https://github.com/goto456/stopwords/blob/master/百度停用词表.txt
stopWords = []
with open('stopwords.txt') as f:
    for line in f:
        stopWords.append(line.strip())

def tokenize(text, stop=False):
    text = re.sub('\s', '', text)
    text = list(jieba.cut_for_search(text))
    tokenized_text = []
    stop_list = []
    stop_list.extend(eng_punc)
    stop_list.extend(ch_punc)
    if stop:
        stop_list.extend(stopWords)
    for word in text:
        if word not in stop_list:
            tokenized_text.append(word)
    return tokenized_text

def process(text):
    words = tokenize(text)
    return CT(words)

if __name__=='__main__':
    text = '''
        我  是否 吃了米饭和米饭。
        你呢？
    	'''
    print(process(text))