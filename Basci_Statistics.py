import pandas as pd

# The URL of the Iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# Import the dataset as a Pandas DataFrame
df = pd.read_csv(url)

# Print the first few rows of the DataFrame
print(df.head())