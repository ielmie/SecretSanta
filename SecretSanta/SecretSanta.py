import random
names=[]
matches=[]

#function to prevent self-matches
def prevent_self_gift(array):
    res_array=[]
    for i in array:
        res_array.append(i)
    j=0
    while j<len(res_array):
        if array[j]==j:
            temp = res_array[j]
            res_array[j]=res_array[(j-1)%len(res_array)]
            res_array[(j-1)%len(res_array)]=temp
        j+=1
    return res_array
    
#TEST CASE FOR PREVENT SELF-GIFT 
#a=[0,1,2,3,4]
#random.shuffle(a)
#print(a)
#b=prevent_self_gift(a)
#print(b)    
    

#open name file and adds the names to the names array
file = open('names.txt','r')
for line in file:
    names.append(line.strip())
file.close()

#create and populate the matches array
i=0
while i<len(names):
    matches.append(i)
    i+=1
#shuffle the array
random.shuffle(matches)
#prevents matching with yourself
final_matches=prevent_self_gift(matches)

#writes the matches to file
k=0
while k<len(names):
    santa=names[k]
    santee=names[matches[k]]
    filename= 'sample_output/'+santa+'.txt'
    f=open(filename, 'w')
    f.write('Hello '+santa+' you must buy a gift for '+santee+'.')
    f.close
    k+=1