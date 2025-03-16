import requests
import matplotlib.pyplot as plt
import numpy as np

BASE_URL = 'https://olimp.miet.ru/ppo_it/api'

data = []
x = range(64)
y = range(64)


maping = []
minimap = [0, 0, 0, 0]
res = []
imgs = []

for i in range(4):
    for j in range(4):
        img = requests.get(f"{BASE_URL}").json().get('message').get('data')
        while [i for i, x in enumerate(imgs) if x == img]:
            img = requests.get(f"{BASE_URL}").json().get('message').get('data')
        minimap[j]= img
        imgs.append(img)

    res.append(np.concatenate((minimap[0], minimap[1], minimap[2], minimap[3]), axis=0))

maping = np.concatenate((np.array(res[0]), np.array(res[1]), np.array(res[2]),np.array(res[3])), axis=1)

print(len(imgs))
for i in range(16):
    sorting = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    count_left = 0
    count_ri = 0

    if imgs[i][0][31] >= 250 and imgs[i][31][0] >= 250:
        print('Top left ', i)
        sorting[0][0] = imgs[i]
    elif imgs[i][0][31] >= 250 and imgs[i][31][62] >= 250:
        print('Top righ ', i)
        sorting[0][3] = imgs[i]
    elif imgs[i][62][31] >= 250 and imgs[i][31][0] >= 250:
        print('Bot left ', i)
        sorting[3][0] = imgs[i]
    elif imgs[i][62][31] >= 250 and imgs[i][31][62] >= 250:
        print('Bot righ ', i)
        sorting[3][3] = imgs[i]

    elif imgs[i][60][60] == 0:
        print('Top left center', i)
        sorting[1][1] = imgs[i]
    elif imgs[i][60][15] == 0:
        print('Top right center', i)
        sorting[2][1] = imgs[i]
    elif imgs[i][15][60] == 0:
        print('Bot left center', i)
        sorting[1][2] = imgs[i]
    elif imgs[i][15][15] == 0:
        print('Bot righ center', i)
        sorting[2][2] = imgs[i]
    
    elif imgs[i][32][0] >= 250:
        print('Left ' + str(count_left+1), i)
        if (count_left == 0):
            sorting[1][0]
            count_left = 1
        else:
            sorting[2][0]

    elif imgs[i][32][64] >= 250:
        print('righ ' + str(count_ri+1), i)
        if (count_ri == 0):
            sorting[1][3]
            count_ri = 1
        else:
            sorting[2][3]

    


x, y = np.meshgrid(range(np.array(maping).shape[0]), range(np.array(maping).shape[1]))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
ax.set_zlabel('Z-Axis')

ax.plot_surface(np.array(x), np.array(y), np.array(maping))
plt.title('z as 3d height map')
plt.show()

plt.figure()
plt.title('z as 2d heat map')
p = plt.imshow(np.array(maping))
plt.colorbar(p)
plt.show()