# FaceTrackLinking
# Problem:
Facetrackers like those included in the dlib library often employ no face recognition, this leads to multiple trackers being created for the same face. Hence it is desirable to cluster these tracks suitably. This helps in better storage, retrieval and analysis of these tracks. 

# Pipeline

![image](https://user-images.githubusercontent.com/14922339/142993802-4f38f3b9-41d7-42de-af72-b72897fd8ee1.png)

## Generating Dataset: 
The dataset can be created on any mkv or mp4 file using Script/script.py with commandline argument of the video in the Data folder
Example:

`` python3 Script/script.py Friends.mp4 ``

This dataset is generated using Haar Cascades.
## Generate Embeddings
The bounding boxes have the faces in them, but we need to create feature vectors out of these. 
There are different techniques to create these embeddings:
1. SIFT / ORB
2. VGG Neural Network
3. Facenet 

## Clustering Embeddings
We can cluster the embeddings using different techniques:
1. K-means - is an unsupervised centroid based algorithm where one chooses K centroids and assigns each object into a particular cluster depending on the distance of the object from each centroid. The object is assigned to the cluster whose centroid has minimum distance to the object.
2. DBSCAN - Density Based Spatial Clustering of Applications with Noise is a density based non-parametric algorithm which classifies densely packed points together and marking low density regions as outlier points.
3. Agglomerative - follows a bottom up clustering approach where we start with singleton clusters (initial objects) and at each iteration two closest clusters merge to form a node and this process continues building a dendrogram until we reach one final node or we stop the clustering process based on a particular threshold. 

and using different metrics:
1.  Euclidean Distance
2.  Cosine Distance

## Results
Results are gauged based on clips extracted from YouTube
This data is not labelled and their are three main results we considering:
1.Dendrogram from Agglomerative Clustering
2. Histogram of new clustering labels
3. Some sample images from new clusters
![image](https://user-images.githubusercontent.com/14922339/142995156-17ffa8af-b230-45b2-87be-56bcdf56b47f.png)

### Running the code
Ensure all requirements are installed and run the Jupyter Notebook in the Notebooks folder

### Future Work:
Testing on large number of tracks and large number of people and coming up with better ways to generate embeddings since it takes a lot of time.
