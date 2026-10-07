x=[i**2 for i in range (2,21)if i%2==0] 
print (x)
print("-"*50)
text ="Hello World"
task=[text[i] for i in range (len(text)) if text[i] not in "aeiou"]
print ("".join(task))
print("-"*50)

'''names =['Ahmed', 'Abdelrahman', 'Mona']
filtered_names = [name[:3] for name in names if len(name) > 4]
print (len(filtered_names)>4)
print (filtered_names)'''
Names = ['Ahmed', 'Abdelrahman', 'Mona']
filtered_Names = map(lambda name: name[:3], filter(lambda name: len(name) > 4, Names))
print(list(filtered_Names))

