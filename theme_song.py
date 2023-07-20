import tensorflow as tf
from tensorflow import io
from tensorflow import image
from matplotlib import pyplot as plt
 
tf_img = io.read_file("cars.jpg")
tf_img = image.decode_png(tf_img, channels=3)
print(tf_img.dtype)
plt.imshow(tf_img)
plt.show()

l = 'left'
r = 'right'
print('turn ' + l + ' to go ' + r + ' right')
