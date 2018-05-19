'''
Created on 2018年5月19日

@author: fany
'''
import gensim


# model1 = gensim.models.Word2Vec.load('zhwiki_2017_03.clean'  )  
# model2 = gensim.models.Word2Vec.load('zhwiki_2017_03.sg_50d.word2vec' )  
# model = gensim.models.KeyedVectors.load_word2vec_format("zhwiki_2017_03.sg_50d.word2vec", binary=False)

f = open("zhwiki_2017_03.sg_50d.word2vec" ,encoding = "utf-8")
for index, line in enumerate(f):
#     print(index)
    print(line)