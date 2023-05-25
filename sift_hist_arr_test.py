import numpy as np
from skimage import img_as_ubyte, color
import cv2

def hist_list(X_test, y_test, kmeans):
  sift = cv2.SIFT_create()
  hist_list_test = []
  # Number of centroids/codewords: good rule of thumb is 10*num_classes
  k = 7*10
  for i in range(len(X_test)):
      img = img_as_ubyte(color.rgb2gray(X_test[i]))
      kp, des = sift.detectAndCompute(img, None)

      if des is not None:
          hist = np.zeros(k)

          idx = kmeans.predict(des)

          for j in idx:
              hist[j] = hist[j] + (1 / len(des))

          # hist = scale.transform(hist.reshape(1, -1))
          hist_list_test.append(hist)

      else:
          hist_list_test.append(None)

  del img, kp, des # delete variables that we won't be using to preserve RAM memory

  # Remove potential cases of images with no descriptors
  idx_not_empty = [i for i, x in enumerate(hist_list_test) if x is not None]
  hist_list_test = [hist_list_test[i] for i in idx_not_empty]
  y_test = [y_test[i] for i in idx_not_empty]
  hist_array_test = np.vstack(hist_list_test)
  return hist_array_test, y_test

