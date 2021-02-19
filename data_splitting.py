#encoding=utf-8
from __future__ import print_function, unicode_literals
import sys
sys.path.append("../")
import jieba
jieba.load_userdict("userdict.txt")
import jieba.posseg as pseg

import json
with open('comments.json','r', encoding='utf-8') as fi:
    word = fi.read()
    data = json.loads(word)
test_sent=''
for i in data:
    test_sent += i["评论"]
words = jieba.cut(test_sent)
print('\n'.join(words))
print("="*40)
result = pseg.cut(test_sent)
with open('splitting.txt', 'a', encoding='UTF-8') as f:  # 将数据存入txt
    for w in result:
        f.write(w.word+ '\n')
