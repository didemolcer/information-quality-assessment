# -*- coding: utf-8 -*-
"""
@author: didem
"""

import string
import re
from nltk import word_tokenize

from nltk.stem import WordNetLemmatizer 
lmtzr=WordNetLemmatizer()
exclude = set(string.punctuation)

weird=70
websiteNum=61 #number of websites+1

while(1):
    if weird>690:
        break;
    else:
        f=open("C:\\...\\matrix %s.txt"%(weird),"w",encoding="utf8")
        total=[]    
        
        h= open("C:\\...\\query %s.txt"%(weird),encoding="utf8") 
        terms = ''.join(h.readlines())
        terms = [x.rstrip().split('*') for x in terms.split('\n')[: -1]]
        
        for y in range (1,websiteNum):
                 tokensC=sentsC=0
                 print(y)
           
                 textt=open("C:\\...\\%d.txt"%(y), encoding="utf8")
                 text=textt.read()
                 
                 text=text.lower()
                 
                 document = re.sub('[^A-Za-z0-9 .-]+', ' ', text)
                 document = document.replace('-', '')
                 document = document.replace('...', '')
                 document = document.replace(':', '')
            
                
                 tokens = word_tokenize(document)  
                 
                 lmtz_tokens = [lmtzr.lemmatize(i) for i in tokens]
            
                 full=' '.join(lmtz_tokens)
                 
                 
                 for total in terms:
#                   
                   x=count=0
                   for gram in total:
                         r = re.compile(r'\b%s\b' % gram, re.I)
                         m = r.search(full)
                         
                         if m:
                             count+=1
         
                   score=count/len(total)*100
                   f.write(str(score))
                   f.write(" ")     
                 f.write('\n')
                 f.flush()
        f.close()    
        
        weird=weird+70

