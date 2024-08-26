# 
# use the map functionality for batch processing
tokenised_datasets = tweet_dataset.map(tokenise_them, batched=True)
training_dataset = tokenised_datasets["train"].shuffle(seed=124).select(range(100))  #increase the range for higher quality model output
evaluation_dataset = tokenised_datasets["test"].shuffle(seed=124).select(range(100))
