weights = [10.0, 9.9, 10.1, 10.05]
print(weights)

total = 0
largest = 0
for weight in weights:
    total+=weight
    if weight > largest:
        largest = weight
average = total/len(weights)
print(average)
print(largest)


