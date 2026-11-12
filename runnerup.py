# Task 3: Runner-up Score
# Name: Akash Sivanandan
# URN: 2481026

n = int(input())
scores = list(map(int, input().split()))

scores = sorted(set(scores))

print(scores[-2])
