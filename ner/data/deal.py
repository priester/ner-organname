# -*- coding: utf-8 -*-
'''
Created on 2018年5月19日

@author: fany
'''
import re

f = open ("词性标注@人民日报199801.txt" , encoding="utf-8")
# f = open ("test.txt" , encoding="utf-8")
w = open ("words.txt", "w+",encoding="utf-8",)
w2 = open ("sign.txt", "w+",encoding="utf-8")  

p = re.compile('[0-9]{8}-[0-9]{2}-[0-9]{3}-[0-9]{3}/m  ')
p2 = re.compile('/[a-zA-Z]{1,2}');
p3 = re.compile('.*[^\[]/nt')
p4 = re.compile('\[.*')
p5 = re.compile('.*\]nt')
p6 = re.compile('.*\]ns')

for line in f :
    line = p.sub("", line)
    terms = line.split()

    words = []  
    sign = []

    for i in range(len(terms)) :
        term = terms[i]
        #   多个词构成的机构开头  
        if (p4.match(term) and (p2.sub("", term) != "[")):
            for j in range(i,len(terms)):
                
#                 print (terms[j])
            
                if(p5.match(terms[j]) ) :
                    term = p2.sub("", term)
                    term = term.replace("[", "")
                    words.append(term)
                    sign.append("B-ORG") 
                    break
                
                if(re.compile('.*\]ns').match(terms[j]) or re.compile('.*\]nz').match(terms[j]) or re.compile('.*\]i').match(terms[j]) or re.compile('.*\]l').match(terms[j])  ) :
                    term = p2.sub("", term)
                    term = term.replace("[", "")
                    words.append(term)
                    sign.append("O") 
                    break
        
#     单个词构成机构
        elif p3.match(term):
            term = p2.sub("", term)
            words.append(term)
            sign.append("S-ORG") 
        
    
                
    #   多个词构成的机构结尾        
        elif(p5.match(term)):
            term = term.replace("]nt", "")
            term = p2.sub("", term)
            words.append(term)
            sign.append("I-ORG")
         
    #   多个词构成的机构结尾        
        elif(re.compile('.*\]ns').match(term)):
            term = term.replace("]ns", "")
            term = p2.sub("", term)
            words.append(term)
            sign.append("O") 
             
        
        # 机构名称中间的词        
        elif (i > 0 and (sign[i - 1] == "I-ORG"  or sign[i - 1] == "B-ORG")): 
            if(p5.match(terms[i - 1]) ): 
                term = p2.sub("", term)
                words.append(term)
                sign.append("O")
            else:
                term = p2.sub("", term)
                words.append(term)
                sign.append("I-ORG") 
        
    #     其他词        
        else:
            term = p2.sub("", term)
            words.append(term)
            sign.append("O")
#         print (words);
#         print (sign);
            
    w.write(' '.join(words) + '\n')
#     print(words) 
    w2.write(' '.join(sign) + '\n')
#     print(sign) 
    