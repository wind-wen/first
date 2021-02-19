
import jieba
from pyecharts.charts import WordCloud
# 从文本文件中生成词云
def Generator():
    with open('splitting.txt', 'r', encoding='utf-8') as f:
        text_body = f.read()
    f.close()

    # 使用jieba进行分词
    words_lst = jieba.cut(text_body.replace('\n', '').replace(' ', ''))

    # 统计词频
    total = {}
    for i in words_lst:
        total[i] = total.get(i, 0) + 1

    # 按词频进行排序，只选取包含两个或两个以上字的词
    data = dict(sorted({k: v for k, v in total.items() if len(k) >= 2}.items(), key=lambda x: x[1], reverse=True)[:200])

    # 构造一个词云对象，把所有的词放进去
    word_cloud = WordCloud()
    word_cloud.add("《在一起》视频评论数：", data.items(),shape="diamond")  # 用钻石的形状显示词云

    # 把词云显示到一个html网页中
    word_cloud.render('index.html')

Generator()