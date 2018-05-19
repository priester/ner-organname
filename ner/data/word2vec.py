# -*- coding: utf-8 -*-
import logging
import time

import gensim.models
from gensim.models.word2vec import LineSentence

def trainModel(inputfile):

    sentences = LineSentence(inputfile);
    modelbase = gensim.models.Word2Vec(size=300,
                     min_count=5,
                     window=5,
                     workers=2,
                     iter=100)
    modelbase.build_vocab(sentences)
    modelbase.train(sentences) 
    # model save
#     modelbase.save_word2vec_format(outVectorFile)  # 存为词向量
    # model using

if __name__ == "__main__":
    inputfile = "XXX.txt"
    trainModel()
    # train and save model
#     trainModel(inputfile,outVectorFile)

