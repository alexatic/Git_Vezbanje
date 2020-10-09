def range (start,end):
    current = start
    while current < end:
        yield current
        current +=1
def sentence(sentence):
    for word in sentence.split():
        yield word


my_sentence = sentence ('This is a test fuck me')
for word in my_sentence:
    print(word )

brojevi = range(1,100)

for i in brojevi:
    print(i)

input()
