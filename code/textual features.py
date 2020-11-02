import os,string,bs4

from textstat.textstat import textstat
from nltk import sent_tokenize, word_tokenize
from nltk.stem.porter import PorterStemmer 
from collections import Counter

from nltk.tag.stanford import StanfordPOSTagger as POS_Tag
from nltk.parse.stanford import StanfordParser
from nltk.parse.stanford import StanfordDependencyParser

current_dir = 'C:/Users/.../.spyder'

_path_to_model = current_dir+'/stanford-postagger/models/english-bidirectional-distsim.tagger' 
_path_to_jar = current_dir + '/stanford-postagger/stanford-postagger.jar'
st = POS_Tag(model_filename=_path_to_model, path_to_jar=_path_to_jar)

stanford_parser_dir = current_dir + "/stanford-parser-full-2017-06-09"
eng_model_path = stanford_parser_dir + "/englishRNN.ser.gz"
my_path_to_models_jar = stanford_parser_dir + "/stanford-parser-3.8.0-models.jar"
my_path_to_jar = stanford_parser_dir + "/stanford-parser.jar"

parser = StanfordParser(model_path = eng_model_path, path_to_models_jar = my_path_to_models_jar, path_to_jar = my_path_to_jar)
dependency_parser = StanfordDependencyParser(path_to_jar = my_path_to_jar, path_to_models_jar = my_path_to_models_jar)

java_path = "C:/Program Files (x86)/Java/jre1.8.0_231/bin/java.exe"
os.environ['JAVAHOME'] = java_path


###############################################################################

websiteNum=61 #number of websites+1
webpageNum=43 #max web page number of websites+1

for y in range (1,websiteNum):
    try:
        if(os.path.isfile("C:\\...\\%d.txt"%(y))):

            file=open("C:\\...\\%d.txt"%(y), encoding="utf8")
            text=file.read()
            file.close()
            
            text=text.lower()
#==============================================================================
#    Readability scores
#==============================================================================            

            flesch=textstat.flesch_kincaid_grade(text)
            smog=textstat.smog_index(text)

#==============================================================================
#   Text Length Features: sentence count, word count, character count
#==============================================================================
             
            sents = sent_tokenize(text)   
            sentsC=len(sents)

            tokens = word_tokenize(text)  
            charac=sum(len(word) for word in tokens)
          
            exclude = set(string.punctuation)
            text = ''.join(ch for ch in text if ch not in exclude)
                     
            tokens = word_tokenize(text)
            tokensC=len(tokens)
                                      
#==============================================================================
#    Lexical variety
#==============================================================================
                    
            p_stemmer = PorterStemmer()
     
            unique=[]
            stemmed_tokens = [p_stemmer.stem(i) for i in tokens]
            for word in stemmed_tokens:
                if word not in unique:
                    unique.append(word)
            
            lexicalVariety=len(unique)/len(tokens)
            
#==============================================================================
#       Text Style Features
#==============================================================================               
            
            #=======Number of uses of verb to be=============
            countToBe=0      
            for i in tokens :
                if(i=='am' or i=='is' or i=='are' or i=='was' or i=='were' or i=='being'or i=='been' or i=='be'):
                      countToBe=countToBe+1;
                  
            pronoun=passive=shortSent=0
            verbCount=adjCount=nounCount=modalCount=0
            prpnn=['PRP','PRP$','NN','NNP','NNS','NNPS']
            exdt={'DT','EX'}
            vrb=['VB','VBG','VBD','VBN','VBP','VBZ'] 
            imp=dec=ques=exc=existen=0  
            
            for sent in sents:
                    
                Stokens = word_tokenize(sent)
                Stagged_tokens = st.tag(Stokens)
                countPOS=Counter(tag for word,tag in Stagged_tokens)
                      
            #=======Number of sentences starting with a pronoun=============
     
                if(Stagged_tokens[0][1]=='PRP' or Stagged_tokens[0][1]=='PRP$'):
                       pronoun=pronoun+1
                       
            #=======Number of passive voice sentences=============
     
                result = dependency_parser.raw_parse(sent)
                dep = next(result)
                parsed_result = list(dep.triples())
                                         
                passive = passive + str(parsed_result).count("'nsubjpass'");
    
            #=======Number of nouns,verbs,adjectives, auxiliary verb=============
           
                nounCount= nounCount+countPOS['NN']+countPOS['NNP']+countPOS['NNPS']+countPOS['NNS']
                verbCount= verbCount+countPOS['VB']+countPOS['VBD']+countPOS['VBG']+countPOS['VBN']+countPOS['VBP']+countPOS['VBZ']
                adjCount= adjCount+countPOS['JJ']+countPOS['JJR']+countPOS['JJS']
                modalCount= modalCount+countPOS['MD']   
              
            #=======Short sentence rate=============
                                                                
                if (len(Stokens)<=15):
                    shortSent=shortSent+1;
            
                if len(sents)>0 and shortSent>0:
                    shortSentRate=shortSent*100/len(sents);        
                    
#==============================================================================
#       Sentence Type Features
#==============================================================================                       
                      
                if(Stagged_tokens[0][1]=='VB' or Stagged_tokens[0][1]=='VBP'):
                    imp=imp+1  #imperative sentences
                    
                elif(Stagged_tokens[0][1] in exdt):
                    existen=existen+1   #existential sentences
                    
                else:
                       
                       if('?' in Stokens):
                           ques=ques+1;  #interrogative sentences
                          
                       elif('!' in Stokens):
                           exc=exc+1;   #exclamatory sentences
                         
                       else:
                           dec=dec+1;  #declarative sentences
                           
    except:
            print("Error")                  
        
#==============================================================================
#       Text Structure Features (using HTML files)
#==============================================================================                       
                 
for y in range (1,websiteNum):
    totalSec=totalImg=totalBullet=totalPrg=totalPrgLen=totalSecLen=0
    for x in range (1,webpageNum):
     try:
        if(os.path.isfile("C:\\...\\%d\\%d (%d).html"%(y))):

            html=open("C:\\...\\%d (%d).html"%(y),encoding='utf8').read()
            soup=bs4.BeautifulSoup(html);
    
############delete script ve noscript 
          
            for txt in soup(["script","noscript","meta","style"]):
                txt.extract();
           
############delete special tags references ve other links 
            
            for i in soup.find_all('div'):
                if i.has_attr('class') and i['class'][0]=="ref":
                    i.extract();
            for i in soup.find_all('div'):
                if i.has_attr('class') and i['class'][0]=="links":
                    i.extract();

            sec=prg=bullet=img=0;
            
#=========Section Count, Avg Section Length, Shortest section length=========== 
   
            for header in soup.find_all('h1'):
                if (len(header.get_text().split())>0):
                    sec=sec+1
            for header in soup.find_all('h2'):
                if (len(header.get_text().split())>0):
                    sec=sec+1    
            for header in soup.find_all('h3'):
                if (len(header.get_text().split())>0):
                    sec=sec+1
            for header in soup.find_all('h4'):
                if (len(header.get_text().split())>0):
                    sec=sec+1
            for header in soup.find_all('h5'):
                if (len(header.get_text().split())>0):
                    sec=sec+1
            for header in soup.find_all('h6'):
                if (len(header.get_text().split())>0):
                    sec=sec+1
                        
            secLen=totaltokens=totalShortSecLen=0
            
            for section in soup.find_all('text'):
                if (len(section.get_text().split())>0):
                    secText=section.get_text()
                    text = ''.join(ch for ch in secText if ch not in exclude)
                    tokens = word_tokenize(text)  
                    tokensC=len(tokens)
                    secLen.append(tokensC)
                    totaltokens=totaltokens+tokensC

            if sec>0 and totaltokens>0:
                avgSecLen=totaltokens/sec    
   
            lenShort=min(secLen)
            totalShortSecLen.append(lenShort);
                                
#==========Bullet Count =====================================                                    
                             
            for bullet in soup.find_all('li'):
                if (len(bullet.get_text().split())>0):
                    bullet=bullet+1
                                                    
#===========Image Count==================================== 
            
            for image in soup.find_all('img'):
                img=img+1
                                           
#=========Paragraph Count, Avg Paragraph Length============= 
                                  
            totalLen=0
             
            for paragraph in soup.find_all('p'):
               if (len(paragraph.get_text().split())>0):
                    totalLen=totalLen+len(paragraph.get_text().split())
                    prg=prg+1
                    
            if prg>0:
                avgParagLen=totalLen/prg
                               
            totalSec+=sec
            totalSecLen+=totaltokens
            shortSec=min(totalShortSecLen)
            totalBullet+=bullet
            totalImg+=img
            totalPrg+=prg
            totalPrgLen+=totalLen
       
     except:
        print("Error")                  
    
    avgSec=totalSecLen/totalSec
    avgPrg=totalPrgLen/totalPrg            


            
         
                                              
    
