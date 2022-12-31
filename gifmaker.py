import imageio
images = []
filenames = [f"fig{k}.png" for k in range(200)]
for filename in filenames:
    images.append(imageio.imread(f"images/{filename}"))
imageio.mimsave('accuracy4.gif', images)