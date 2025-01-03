import pandas as pd

# Showing functions that you could augment to load data

def load_listings():
    return pd.read_csv('listings.csv')

def load_reviews():
    return pd.read_csv('reviews.csv')