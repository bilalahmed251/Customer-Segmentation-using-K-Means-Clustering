# Customer Segmentation using K-Means Clustering

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Unsupervised Learning](https://img.shields.io/badge/ML-Unsupervised-purple)

An advanced unsupervised machine learning project that analyzes customer purchasing behavior and groups them into distinct segments for targeted marketing.

## Features
- **Optimal Cluster Detection:** Programmatically determines the best number of clusters (k) using the Silhouette Score optimization loop.
- **Dimensionality Reduction:** Employs Principal Component Analysis (PCA) to reduce complex multi-dimensional data down to 2 components.
- **Data Visualization:** Automatically generates and saves a beautiful 2D scatter plot projection (customer_segments_pca.png) of the customer clusters using Seaborn.
- **Model Export:** Exports the final KMeans model for future inferences.

## Tech Stack
- **Language:** Python
- **Libraries:** Scikit-Learn (KMeans, PCA), Seaborn, Matplotlib, Pandas
