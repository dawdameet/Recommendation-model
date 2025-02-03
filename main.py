import math

def cosine(userProfile, fi):
    magUs = 0
    magPs = 0
    dot = 0
    for i in range(3):
        magUs += math.pow(userProfile[i], 2)
        magPs += math.pow(fi[i], 2)
        dot += userProfile[i] * fi[i]
    magU = math.sqrt(magUs)
    magP = math.sqrt(magPs)
    return dot / (magU * magP)

f = [
    [1, 1, 1],
    [1, 1, 2],
    [1, 2, 3],
    [2, 3, 1],
    [1, 2, 2],
    [2, 1, 3],
    [1, 3, 2],
    [1, 2, 1]
]

l = [0, 2, 4]
d = [3, 5]

w_L = 0.6
w_D = 1 - w_L

likedPi = []
dislikedPi = []

for i in range(len(l)):
    likedPi.append(f[l[i]])
for i in range(len(d)):
    dislikedPi.append(f[d[i]])

userProfileLiked = []
userProfileDisiked = []

for i in range(3):
    sm_liked = 0
    sm_disliked = 0
    for j in likedPi:
        sm_liked += j[i]
    for k in dislikedPi:
        sm_disliked += k[i]
    userProfileLiked.append(w_L * (sm_liked / len(likedPi)))
    userProfileDisiked.append(w_D * (sm_disliked / len(dislikedPi)))

userProfile = []
for i in range(3):
    userProfile.append(userProfileLiked[i] - userProfileDisiked[i])

item_to_test = f[3]
prob = cosine(userProfile, item_to_test)

if prob < 0:
    print("User might not like this product")
elif prob > 0 and prob < 0.5:
    print("User might like this product (low chances)")
else:
    print("User will like this product (high chances)")
print("Cosine Similarity:", prob)
