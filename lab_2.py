x=[i**2 for i in range (2,21)if i%2==0] 
print (x)
text ="Hello World"
task=[text[i] for i in range (len(text)) if text[i] not in "aeiou"]
print ("".join(task))