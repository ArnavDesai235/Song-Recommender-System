#SpKMeans in a KMeans implementation that uses cosine similarity as a metric instead of Euclidean distance for better performance on high dimensional spaces.
#It is a child class of KMeams from Sklearn library

import numpy as np
from sklearn.cluster import KMeans

class SpKMeans(KMeans):
    weight = None
    def __init__(
        self,
        n_clusters=8,
        *,
        init="k-means++",
        n_init=10,
        max_iter=300,
        tol=1e-4,
        verbose=0,
        random_state=None,
        copy_x=True,
        algorithm="lloyd",
        weight = None
    ):
        super().__init__(
            n_clusters=n_clusters,
            init=init,
            n_init=n_init,
            max_iter=max_iter,
            tol=tol,
            verbose=verbose,
            random_state=random_state,
            copy_x=copy_x,
            algorithm=algorithm
        )

    def _transform(self, X):
        return  sklearn.metrics.pairwise.cosine_similarity(X, self,self.weight)
