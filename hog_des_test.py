from skimage.feature import hog


def hog_des_test(X_test):
  HOG_des_test = []

  for image in X_test: 
    des, hog_image = hog(image, orientations=8, pixels_per_cell=(8, 8), cells_per_block=(1, 1), visualize=True, multichannel=True)
    HOG_des_test.append(des)
  
  del hog_image

  return HOG_des_test