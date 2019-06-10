# coding: utf-8

from app.models import ZhiDaoDoc, ZhiDaoAnswer, BaiKeDoc, BaiKeSection
from app import db


bafanglvren = BaiKeDoc(
    doc_id=100000,
    title='八方旅人',
    description='角色扮演游戏《八方旅人》（Octopath Traveler）2018年7月13日登陆任天堂NS平台。 [1-3]  由任天堂公司负责国际发行， Square Enix 负责日本发行。 [4]  本作由Square Enix、Acquire，及制作TRPG的FarEast Amusement Research共同制作。 [5]  游戏采用虚幻4引擎打造，画面采用结合复古像素点阵与3DCG的风格。 [6]  《八方旅人》IGN评分9.3。 [6]  故事发生在名为奥斯泰拉的大陆，主人公是8名旅行者，玩家扮演其中之一在世界各地自由旅行。'
)

bafanglvren_0 = BaiKeSection(
    baike_id=100000,
    section_title='中文化',
    text='香港任天堂宣布在19年6月7日发布《八方旅人》中文版，定名《歧路旅人》。 [8] 本次更新方式是在线补丁更新，将更新简体中文版、繁体中文版这两个版本。更新时间为北京时间6月7日10：00。 [8] ',
)

bafanglvren_1 = BaiKeSection(
    baike_id=100000,
    section_title='故事背景',
    text='本作的故事发生在名为奥斯泰拉（オルステラ）的大陆，主人公是8名旅行者，玩家扮演其中之一在世界各地自由旅行，包括出生的地方也将成为旅行的目的地。',
)

bafanglvren_2 = BaiKeSection(
    baike_id=100000,
    section_title='角色设定',
    text='游戏中可选八名角色分别为神官Ophilia、学者Cyrus、商人Tressa、剑士Olberic、舞女Primrose、药师Alfyn、盗贼Therion、猎人Haanit。 [9]\n 他们每人都有自己的技能和天赋，其中技能分为“正道”和“邪道”两种。游戏中使用“正道”技能不会失败，但会有着诸如等级之类的限制，需角色满足一定条件能发动；而“邪道”技能可对任何人使用，却有一定失败的几率，失败后玩家会与NPC关系变差，需在酒馆里使用金钱来改善关系。 [9] '
)


nuoruo = ZhiDaoDoc(
    doc_id=0,
    question='性格懦弱没有主见该怎样改变？',
)

nuoruo_0 = ZhiDaoAnswer(
    question_id=0,
    answer='我以我自身为例，介绍一下吧懦弱而没有主见，即使有主意也只是躲在别人后面，表示同意，这样的情况下不容易改变自己；每次下定决心，却又在心里犹豫，最后还是从了别人的意愿；'
           '改变都是有外界因素的情况下，慢慢的改变了；或是遭到了社会的铁拳，或是舍友的教育课，同事的欺负，朋友的利用...'
           '这个时候就慢慢硬气起来，慢慢变得坦诚，有什么想法就说，有什么要求就提，不要不好意思去拒绝。'
           '丑话说在前面是最好的，如果开头说甜言蜜语，可能最后只是吃亏。比如，某些公司先谈情怀，不谈工资，满满的理想；你对对对，是是是，听着没营养的话语只是点头；最后加班是你，拿不着工资也是你。'
           '不管什么事，不愿意就直说，哪怕是领导安排的事情，不然就只能默默接受后承担苦果，或者中途不支留下坏名。'
           '另外，我支持最佳答案'
)

nuoruo_1 = ZhiDaoAnswer(
    question_id=0,
    answer='两种情况：'
           '如果你不是没主见，而是因为性格软弱放弃自己的主见。那经历一些事情以后你会发现，就算你忍让，别人也不领这份情。生活是你的，自己开心最重要。'
           '如果你真的觉得没有主见，或者说对一件事没有自己的判断，那就多读书，没事看看辩论赛。角度多了观点就多了。'
)

nuoruo_2 = ZhiDaoAnswer(
    question_id=0,
    answer='要学会独立分析判断问题，不要人云亦云。别人的话可以作为参考，但是不是所有的话一定都是真的，因为一个人的观点不可能全部都是对的。听到别人的意见不要马上采纳，要给自己留出一些思考的时间，甚至需要自己独自去调查分析判断，也就是自己去求证，意见的辨别真伪。'
)


ziyiweishi = ZhiDaoDoc(
    doc_id=1,
    question='如何对待生活中自以为是的人？',
)

ziyiweishi_0 = ZhiDaoAnswer(
    question_id=1,
    answer='惯着他，顺着他，把他捧到天上。这样就不会得罪人。然后坐等他从天上掉下来摔的血肉模糊。'
)

ziyiweishi_1 = ZhiDaoAnswer(
    question_id=1,
    answer='为什么我觉得我就是这样的人，我总觉得这个人应该是这样的，然而接触下来不是我想象中的样子，和我心里面有落差、我就很难 自我调节。自己给自己过不去。说话说嗨起来的话，还会大声说，口无遮拦。改不掉呀，控制不住自己的情绪，我有时都想去哪学习学习培养锻炼自己，不能这样'
)



if __name__ == '__main__':
    db.session.query(ZhiDaoAnswer).delete()
    db.session.query(BaiKeSection).delete()
    db.session.commit()
    db.session.query(ZhiDaoDoc).delete()
    db.session.query(BaiKeDoc).delete()
    db.session.commit()

    db.session.add(ziyiweishi)
    db.session.commit()
    db.session.add_all([ziyiweishi_0, ziyiweishi_1])
    db.session.commit()

    db.session.add(bafanglvren)
    db.session.commit()
    db.session.add_all([bafanglvren_0, bafanglvren_1, bafanglvren_2])
    db.session.commit()

    db.session.add(nuoruo)
    db.session.commit()
    db.session.add_all([nuoruo_0, nuoruo_1, nuoruo_2])
    db.session.commit()

    doc = BaiKeDoc.query.filter(BaiKeDoc.title == '八方旅人').first()
    result = doc.sections
    for section in result:
        print('-' * 10)
        print(section.section_title)

    ques = ZhiDaoDoc.query.filter(ZhiDaoDoc.doc_id == 0).first()
    for answer in ques.answers:
        print('-' * 10)
        print(answer.answer)
