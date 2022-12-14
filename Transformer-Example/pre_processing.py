import pandas as pd
# this is to extract the data from that .tgz file
import tarfile
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# get all of the data out of that .tgz
yelp_reviews = tarfile.open('data/yelp_review_polarity_csv.tgz')
yelp_reviews.extractall('data')
yelp_reviews.close()

# check out what the data looks like before you get started
# look at the training data set
train_df = pd.read_csv('data/yelp_review_polarity_csv/train.csv', header=None)
print(train_df.head())

# look at the test data set
test_df = pd.read_csv('data/yelp_review_polarity_csv/test.csv', header=None)
print(test_df.head())