import pandas as pd

# Loading the preprocessed train, validation and test dataset
train_data = pd.read_csv("../preprocessed_data/train.csv")
valid_data = pd.read_csv("../preprocessed_data/valid.csv")
test_data = pd.read_csv("../preprocessed_data/test.csv")


# Iterating through each dataset
for dataset in [ train_data, valid_data, test_data]:
    # Computing the total number of articles in the dataset
    total = dataset.shape[0]
    # Computing the number of articles generated by each author in the dataset
    class_count = dataset.groupby('label').size()
    # Computing the proportion of the articles generated by each author in the dataset
    class_proportion  = class_count / total
    print(f"Total : {total}, Class Count : {class_count}, Class Proportion : {class_proportion}", "\n\n")


    
