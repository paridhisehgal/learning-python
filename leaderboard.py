names = []
scores = []

for i in range(6):
    name = input("Enter player name: ")
    score = int(input("Enter player score: "))

    names.append(name)
    scores.append(score)

for i in range(len(scores)):
    for j in range(i + 1, len(scores)):
        if scores[i] < scores[j]:
            scores[i], scores[j] = scores[j], scores[i]
            names[i], names[j] = names[j], names[i]

print("\nLeaderboard:")

for i in range(6):
    print(f"#{i + 1} {names[i]} - {scores[i]}")