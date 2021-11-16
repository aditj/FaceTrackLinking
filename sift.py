import cv2 
import matplotlib.pyplot as plt
import numpy

# read images

img1 = cv2.imread('img_0.jpeg')  
img2 = cv2.imread('img_1.jpeg') 
img3 = cv2.imread('img_20.jpeg') 

img4 = cv2.imread('img_42.jpeg')  
img5 = cv2.imread('img_63.jpeg') 

# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)


def sift1(img1,img2):
    
    #sift
    sift = cv2.SIFT_create()

    keypoints_1, descriptors_1 = sift.detectAndCompute(img1,None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(img2,None)

    #feature matching
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

    matches = bf.match(descriptors_1,descriptors_2)
    matches = sorted(matches, key = lambda x:x.distance)
    
    print(len(matches))

    img3 = cv2.drawMatches(img1, keypoints_1, img2, keypoints_2, matches[:50], img2, flags=2)
    plt.imshow(img3),plt.show()

def sift2(img1,img2):

    sift = cv2.SIFT_create()

    keypoints_1, descriptors_1 = sift.detectAndCompute(img1,None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(img2,None)

    bf = cv2.BFMatcher()
    matches = bf.knnMatch(descriptors_1,descriptors_2, k = 2)

    good = []
    for m,n in matches:
        if m.distance < 0.90*n.distance:
            good.append([m])

    print(len(good))

    img3 = cv2.drawMatchesKnn(img1,keypoints_1,img2,keypoints_2,good, None,flags=2)
    plt.imshow(img3),plt.show()

# sift1(img1,img2)
# sift2(img4,img3)

