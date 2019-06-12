import json
from app.models import ZhiDaoDoc, ZhiDaoAnswer, ZhiDaoPicture
from app import db
import os
import re


def single():
    f = open('zhidao/11085.json', 'r')
    content = json.loads(f.readline())
    print(content)
    question = content['question']
    title = question['title']
    title = re.sub('\s[\d]*$', '', title)
    print(title)
    description = question['content']
    print(description)
    time = question['time']
    print(time)

    if 'best_answer' in content:
        best = content['best_answer']
        name = best['name']
        time = best['time']
        likes = best['likes']
        bad_likes = best['bad_likes']
        answer = best['content']
        answer = re.sub(r'"https.*.jpg"[\s]*', '', answer)
        print(answer)
        pics = best['pics']
        for pic in pics:
            print(pic)
        print(name, time, likes, bad_likes, answer)

    for other in content['other_answers']:
        name = other['name']
        time = other['time']
        likes = other['likes']
        bad_likes = other['bad_likes']
        answer = other['content']
        answer = re.sub(r'"https.*.jpg"[\s]*', '', answer)
        pics = other['pics']
        for pic in pics:
            print(pic)
        print(name, time, likes, bad_likes, answer)


def add_one(json_path, id, answer_id):
    f = open(json_path, 'r')
    content = json.loads(f.readline())
    question = content['question']

    title = question['title']
    title = re.sub('\s[\d]*$', '', title)
    description = question['content']
    time = question['time']
    doc = ZhiDaoDoc(
        doc_id=id,
        question=title,
        description=description,
        ask_time=time,
    )
    db.session.add(doc)

    if 'best_answer' in content:
        best = content['best_answer']
        name = best['name']
        time = best['time']
        likes = best['likes']
        bad_likes = best['bad_likes']
        answer = best['content']
        answer = re.sub(r'"https.*.jpg"[\s]*', '', answer)

        ans = ZhiDaoAnswer(
            answer_id=answer_id,
            question_id=id,
            answer=answer,
            user_name=name,
            likes=likes,
            dislikes=bad_likes,
            accepted=True,
            answer_time=time
        )
        db.session.add(ans)

        pics = best['pics']
        for pic in pics:
            pic = ZhiDaoPicture(
                answer_id=answer_id,
                picture_url=pic
            )
            db.session.add(pic)

        answer_id += 1

    # sort by counts of 'likes'
    other_answers = content['other_answers']
    other_answers = sorted(other_answers, key=lambda x: int(x['likes']), reverse=True)
    for other in other_answers:
        name = other['name']
        time = other['time']
        likes = other['likes']
        bad_likes = other['bad_likes']
        answer = other['content']
        answer = re.sub(r'"https.*.jpg"[\s]*', '', answer)
        ans = ZhiDaoAnswer(
            answer_id=answer_id,
            question_id=id,
            answer=answer,
            user_name=name,
            likes=likes,
            dislikes=bad_likes,
            accepted=False,
            answer_time=time
        )
        db.session.add(ans)

        pics = other['pics']
        for pic in pics:
            pic = ZhiDaoPicture(
                answer_id=answer_id,
                picture_url=pic
            )
            db.session.add(pic)

        answer_id += 1

    try:
        db.session.commit()
    except Exception as e:
        print(e)
        print(json_path)
        db.session.rollback()

    return answer_id


def add_all():
    files = os.listdir('zhidao')
    answer_id = 0
    for file in files:
        if file.endswith('.json'):
            id_cnt = int(file.split('.')[0])
            json_path = os.path.join('zhidao', file)
            answer_id = add_one(json_path, id_cnt, answer_id)


if __name__ == '__main__':
    add_all()
    #single()
