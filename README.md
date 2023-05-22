# Song-Recommender-System
A repository of the machine learning models trained and used in my PBL 2023 project. 

This recommender system was inspired by the research paper 'Improvement of k-nearest neighbor algorithm based on double filtering - Chun Jie Ma, Zheng Sheng Ding'. It uses a 2 step approach to help filter songs to be recommended to users.

PBLkmeansFinal-model.pkl is clustering model trained on the dataset. It is an object of SpKmeans class, and uses cosine similarity metric. The normalised data is divided into 10 clusters and stored in 'pbldat.npy' (dimension 1 - cluster number, dim2 = row, dim3 = column). PBLKNN.pkl is a numpy object array of 10 K-Nearest Neighbour (cosine distance) models each fitted to respective cluster. It returns 5 nearest songs to the user vector from the nearest cluster.

The user vector is updated in the backend using an exponential weighted average, depending on the user response. KnowBased.csv is a collection of 5 popular songs from each cluster to construct new user vector. 'API.py' is a module I made to handle API calls to the Spotify API. The project is meant for educational purposes only. The model is being deployed and will soon be ready to use on the domain nornirx.com
