import io

file = io.open('filtered_words.txt', 'r')
list = [word.strip('\n') for word in file.readlines()]
print(list)

def isValid(mystr):
    result = mystr
    for x in list:
        if result.find(x) != -1:
            result = result.replace(x, '**')
    return result

mystr = input("please input a string:")
print (isValid(mystr))

file.close()
