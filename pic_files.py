from skimage.io import imread
from skimage.transform import resize
from matplotlib import pyplot as plt
import matplotlib.cm as cm

przykladowy_plik= ("http://upload.wikimedia.org/wikipedia/commons/7/7d/Dog_face.png")
obrazek=imread(przykladowy_plik, as_grey=True )
plt.imshow(obrazek, cmap=cm.gray)
plt.show()