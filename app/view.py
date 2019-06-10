from .models import WordIndex, BaiKeDoc, ZhiDaoDoc
from .process import process, stopWords
from math import log10


def tf_idf(words, regions):
    weight = {}
    tf = {}
    for term in words:
        for region in regions:
            try:
                tf[term].update(WordIndex.query.filter_by(word=term).index[region])
            except Exception as e:
                print(e)
                tf[term]={}
                continue

            for docid in tf[term]:
                if docid in weight:
                    assert 0
                weight[docid] = 0

    N = len(weight)
    for term in words:
        dic = tf[term]
        for docid, freq in dic.items():
            w = (1+log10(freq)) * (log10(N/len(dic))) * words[term]
            if term in stopWords:
                w *= 0.3
            weight[docid]+=w
    return weight
    # ids = sorted(weight, key=lambda k:weight[k], reverse=True)
    # if len(ids)<8: pass #???
    # return [Doc.objects.get(id=int(i)).__dict__ for i in ids]


def search(text, region=''):
    words = process(text)
    if region == '':
        pass
    else:
        pass


if __name__ == '__main__':
    pass
