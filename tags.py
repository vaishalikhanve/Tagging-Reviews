import nltk
from rake_nltk import Rake
r=Rake()
f=open("reviews.txt","r",encoding="utf-8")
lines = (line.rstrip() for line in f)
lines = list(line for line in lines if line)
z=len(lines)
f.close()
f1=open("tags.txt","w",encoding="utf-8")
count=0
f2=open("not_matched_phrases.txt","w",encoding="utf-8")


        
for i in range(z):
    text1=lines[i]
    #tags=nltk.tag.pos_tag(text1.split())
    #sen=[word for word,tag in tags if tag!='NNP' and tag!='NNPS']
    #text=' '.join(sen)
    text=text1
    r.extract_keywords_from_text(text)
    list_phrase=r.get_ranked_phrases_with_scores()
    a=[]
    a1=a2=a3=a4=a5=a6=a7=a8=a9=0
    check=0
    num=len(list_phrase)
    list_check=0
    y=text1.split(' ')
    
    for j in range(num):
        #if x[0]>=4.0:
        x=list_phrase[j]
        b=x[1]
       
                             
                         
        if b in open("wrong_info.txt").read() :
            check=1
            if a1==0:
                f1.write("wrong_info , ")
                a1+=1
        
                
        
                    
                
        if b in open("performance.txt").read():
            check=1
            if a3==0:
                f1.write("performance , ")
                a3+=1
                    
                
        if b in open("security.txt").read():
            check=1
            if a4==0:
                f1.write("security , ")
                a4+=1
                    

        if b in open("updates.txt").read():
            check=1
            if a5==0:
                f1.write("updates , ")
                a5+=1

        if b in open("feature_request.txt").read():
            check=1
            if a6==0:
                f1.write("feature_request , ")
                a6+=1

        if b in open("functionality.txt").read():
            check=1
            if a7==0:
                f1.write("functionality , ")
                a7+=1
                
        if b in open("routing.txt").read():
            check=1
            if a8==0:
                f1.write("routing , ")
                a8+=1
                

        
            
        if check==0:
            if b in open("just_criticism.txt").read():
                check=1
                if a9==0:
                    f1.write("just_criticism , ")
                    a9+=1
            if b in open("appreciation.txt").read():
                check=1
                if a2==0:
                    f1.write("appreciation , ")
                    a2+=1
        if check==1:
            v=b.split(" ")
            list_check=1
        elif check==0:
            f2.write(b)
            f2.write("\n")
            
        #print(text1)
        #print(" ")
        #print(list_phrase)
        #print("")
        #print("")
    if list_check==0:
        
        #print(list_phrase)
        #print("")
        f1.write("NO MATCH")
        count+=1
    f1.write("\n")
    
                

f1.close()
f2.close()
print("total reviews : ",z)
print("total not matching : ",count)
print("matching numbers : ",z-count)
