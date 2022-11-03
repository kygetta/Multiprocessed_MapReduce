import json
import random

data = []
movies = ['Top Gun','War Dogs','Step Brothers']
rng = 1000
# maxRng = 10000000

for i in range(rng):
	if i < rng / 5:
		rating = random.randint(1,5)
	elif i < rng / 2:
		rating = random.randint(3,5)
	else:
		rating = random.randint(4,5)

	movie = random.choice(movies)


	val = {
		'user_id':i,
		'movie': movie,
		'rating':rating
	}

	data.append(val)

with open("data.json", "w") as f:
    f.write(json.dumps(data))