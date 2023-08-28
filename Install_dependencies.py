import os

libraries = [
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "missingno",
    "tqdm",
    "scikit-learn",
    "scipy",
    "statsmodels",
    "nltk",
    "ipython"
]

for lib in libraries:
    os.system(f"pip install {lib}")
