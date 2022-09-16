import io

file = io.open('filtered_words.txt', 'r')
list = [word.strip('\n') for word in file.readlines()]
print(list)

def isValid(word):
    return all(word != x for x in list)

myword = input("please input a word:")
if isValid(myword):
    print('Human Rights')
else:
    print('Freedom')

file.close()
