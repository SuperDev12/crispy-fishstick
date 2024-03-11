import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.impute import SimpleImputer

# Read the dataset
codebook_df = pd.read_csv('/Users/superdev/Downloads/food_coded.csv')

# Select relevant features
relevant_features = ['cook', 'eating_out', 'employment', 'ethnic_food', 'exercise', 'fruit_day', 'income', 'on_off_campus', 'pay_meal_out', 'sports', 'veggies_day']
relevant_df = codebook_df[relevant_features]

# Handle missing values
imputer = SimpleImputer(strategy='mean')
relevant_df_imputed = pd.DataFrame(imputer.fit_transform(relevant_df), columns=relevant_df.columns)

# Perform k-means clustering
k = 7  # Number of clusters
kmeans = KMeans(n_clusters=k)
kmeans.fit(relevant_df_imputed)

# Add cluster labels to the DataFrame
relevant_df_imputed['cluster'] = kmeans.labels_

# Plot the clusters
plt.figure(figsize=(8, 6))
for cluster in range(k):
    cluster_data = relevant_df_imputed[relevant_df_imputed['cluster'] == cluster]
    plt.scatter(cluster_data['income'], cluster_data['exercise'], label=f'Cluster {cluster}')

plt.scatter(kmeans.cluster_centers_[:, 6], kmeans.cluster_centers_[:, 4], marker='*', s=200, color='black', label='Centroids')
plt.title('K-Means Clustering of Relevant Features')
plt.xlabel('Income')
plt.ylabel('Exercise')
plt.legend()
plt.grid(True)
plt.show()
