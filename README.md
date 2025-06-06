# f1-data-analysis

#**🏎️ Formula 1 Driver Behavior Profiler**
This project analyzes Formula 1 driver behavior using telemetry and lap data from multiple races in a given season (e.g., 2025). The goal is to cluster drivers based on driving style , such as "Aggressive Overtakers", "Consistent Pacers", or "Strategic Long-Stinters". We use FastF1 API , Principal Component Analysis (PCA) , and KMeans Clustering to visualize and categorize driver performance across races.

**🧠 Project Overview**
Extracts lap and position data for all races in a specified year.
Computes key behavioral features like average lap time, overtaking score, and stint length.
Applies feature scaling, PCA for dimensionality reduction, and KMeans clustering.
Visualizes clusters using scatter plots.
Aggregates results across the entire season to identify consistent driver behavior patterns.
