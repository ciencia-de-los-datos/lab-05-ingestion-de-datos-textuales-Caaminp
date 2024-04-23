import os.path 
import pandas as pd 

def read(directory):
    phrases = []
    sentiments = []

    for subdir in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, subdir)):
            for file in os.listdir(os.path.join(directory, subdir)):
                if file.endswith(".txt"):
                    with open(os.path.join(directory, subdir, file)) as f:
                        phrases.append(f.read())
                        sentiments.append(subdir)
    return pd.DataFrame({"phrase": phrases, "sentiment": sentiments})

train_df=read("data/train")
test_df=read("data/test")

print(train_df)
print(test_df)

train_df.to_csv("train_dataset.csv",index=False)
test_df.to_csv("test_dataset.csv", index=False)

print(train_df['sentiment'].value_counts())
print(test_df['sentiment'].value_counts())
print(train_df.columns[0])
print(train_df.columns[1])
