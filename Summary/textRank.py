# -*- encoding:utf-8 -*-

from textrank4zh import TextRank4Sentence


def get_topk_sentence(psg, k):
    """摘取输入文本中最关键的k条句子，按重要性从高到低的顺序返回，同时返回它们在原段落中的编号。

        psg: 用于摘要的全文
        k: 选取最重要的k条语句
    """
    tr4s = TextRank4Sentence()
    tr4s.analyze(text=psg, lower=True, source="all_filters")
    indexes = []
    sentences = []
    for item in tr4s.get_key_sentences(num=k):
        indexes.append(item.index)
        sentences.append(item.sentence)

    return indexes, sentences
