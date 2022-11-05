import operator

d = {'33': 4, '44': 2, '55':7}

#sorted_x = sorted(d.items(), key=operator.itemgetter(1))
#print(sorted_x)


def myFunc(e):
    return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)

print(cars)

for i in d:
    print(d[i])

s= sorted(d, reverse=True)
print(s)

print([str(i) for i in s])