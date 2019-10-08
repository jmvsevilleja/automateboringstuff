import random


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'


print(getAnswer(random.randint(1, 9)))

isNone = print('test')

print(None == isNone)

print('Hello', 'Jess', end='-', sep=' ')
print('World')

print('cats', 'dogs', 'mice')


def spam():
    # print(eggs)
    global eggs
    print(eggs)
    eggs = 'spam local'
    print(eggs)


eggs = 'global'
spam()
print(eggs)
