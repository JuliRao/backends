from app.models import WordIndex, BaiKeDoc, ZhiDaoDoc
from app.process import process, stopWords
from math import log10


def tf_idf(words, regions):
    weight = {}
    tf = {}
    for term in words:
        try:
            index = WordIndex.query.filter_by(word=term).first().index
        except Exception as e:
            print(e)
            tf[term] = {}
            continue

        for region in regions:
            indexes = index[region]
            if term not in tf:
                tf[term] = indexes
            else:
                tf[term].update(indexes)

        for docid in tf[term]:
            weight[docid] = 0

    N = len(weight)
    for term in words:
        dic = tf[term]
        for docid, freq in dic.items():
            w = (1+log10(freq)) * (log10(N/len(dic)))
            if term in stopWords:
                w *= 0.3
            weight[docid] += w

    doc_list = []
    ids = sorted(weight, key=lambda k: weight[k], reverse=True)
    for id in ids:
        id = int(id)
        if id >= 100000:
            doc_list.append(BaiKeDoc.query.filter_by(doc_id = id).first())
        else:
            doc_list.append(ZhiDaoDoc.query.filter_by(doc_id = id).first())
    return doc_list


def search(text, region='all'):
    '''
    :param text:
    :param region: select from ['baike_title', 'baike_section', 'zhidao_question', 'zhidao_answer', 'url'], 'all' represents all places
    :return:
    '''
    words = process(text)
    if region == 'all':
        return tf_idf(words, ['baike_title', 'baike_section', 'zhidao_question', 'zhidao_answer'])
    elif region != 'picture':
        return tf_idf(words, [region])
    else:
        # TODO
        doc_list = tf_idf(words, ['baike_title', 'baike_section', 'zhidao_question', 'zhidao_answer'])
        url_list = []
        return url_list


def get_page(id):
    if id >= 100000:
        return BaiKeDoc.query.filter_by(doc_id = id).first()
    else:
        return ZhiDaoDoc.query.filter_by(doc_id = id).first()


if __name__ == '__main__':
    result = search('皇帝')
    for item in result:
        if isinstance(item, BaiKeDoc):
            print(item.description)
        else:
            print(item.question)
