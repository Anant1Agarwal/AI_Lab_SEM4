import math

X = [1, 2, 3, 4, 5]
Y = [6, 7, 8, 9, 10]

distances = []
for i in range(len(X)):
    distance = math.sqrt((X[i] - Y[i])**2)
    distances.append(distance)

for i in range(len(distances)):
    for j in range(len(distances) - i - 1):
        if distances[j] > distances[j + 1]:
            distances[j], distances[j + 1] = distances[j + 1], distances[j]

print("The Euclidean distances between corresponding elements in X and Y are:")
print(distances)
