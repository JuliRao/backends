from app.models import WordIndex, BaiKeDoc, ZhiDaoDoc
from app.process import process
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
    :param region: select from ['baike_title', 'baike_section', 'zhidao_question', 'zhidao_answer', 'picture'], 'all' represents all places
    :return:
    '''
    words = process(text)
    if region == 'all':
        return tf_idf(words, ['baike_title', 'baike_section', 'zhidao_question', 'zhidao_answer'])
    elif region in ['baike_title', 'baike_section', 'zhidao_question', 'zhidao_answer']:
        return tf_idf(words, [region])
    else:
        url_list = []
        doc_list = tf_idf(words, ['baike_title', 'baike_section', 'zhidao_question', 'zhidao_answer'])
        for doc in doc_list:
            if isinstance(doc, BaiKeDoc):
                for pic in doc.pictures:
                    url_list.append(pic.picture_url)
            else:
                for answer in doc.answers:
                    for pic in answer.pictures:
                        url_list.append(pic.picture_url)
        return url_list


def get_page(id):
    if id >= 100000:
        return BaiKeDoc.query.filter_by(doc_id = id).first()
    else:
        return ZhiDaoDoc.query.filter_by(doc_id = id).first()


if __name__ == '__main__':
    result = search('中国', region='picture')
    print(result[0])
    # for item in result:
    #     if isinstance(item, BaiKeDoc):
    #         print(item.title, item.description)
    #     else:
    #         print(item.question, item.description)

