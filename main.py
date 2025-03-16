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

    if imgs[i][0][31] >= 250 and imgs[i][31][0] >= 250:
        print('Top left ', i)
        sorting[0][0] = imgs[i]
    if imgs[i][0][31] >= 250 and imgs[i][31][62] >= 250:
        print('Top righ ', i)
        sorting[0][3] = imgs[i]
    if imgs[i][31][62] >= 250 and imgs[i][0][31] >= 250:
        print('Bot left ', i)
        sorting[0][3] = imgs[i]
        

    # if imgs[i][31][0] >= 250:
    #     print('Top ', i)
    #     up_str.append(imgs[i])
    # if imgs[i][31][62] >= 250:
    #     print('Botom ', i)
    #     lower_str.append(imgs[i])
    # if imgs[i][31][0] <= 250 and imgs[i][1][31] >= 250:
    #     print('Left1 ', i)
    #     l1 = imgs[i]
    # if imgs[i][31][62] <= 250 and imgs[i][1][31] >= 250:
    #     print('Left2 ', i)
    #     l1 = imgs[i]


    


x, y = np.meshgrid(range(np.array(maping).shape[0]), range(np.array(maping).shape[1]))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X-Axis')
ax.set_ylabel('Y-Axis')
ax.set_zlabel('Z-Axis')

# ax.plot_surface(np.array(x), np.array(y), np.array(maping))
plt.title('z as 3d height map')
plt.show()

plt.figure()
plt.title('z as 2d heat map')
p = plt.imshow(np.array(maping))
plt.colorbar(p)
plt.show()