from sklearn.datasets import load_iris
import pandas as pd

# Load the dataset
iris = load_iris()

# Create a DataFrame
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['target'] = iris.target

print(data.head())
from sklearn.datasets import load_iris
import pandas as pd

# Load the dataset
iris = load_iris()

# Create a DataFrame
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['target'] = iris.target

print(data.head())
