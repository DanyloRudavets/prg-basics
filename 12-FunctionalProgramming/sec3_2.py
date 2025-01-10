sentence = 'I completely agree with you'
k=sentence.split()
result = list(map(lambda k: len(k) , k))
print(result)