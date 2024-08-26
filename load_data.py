#Check the video tutorial for implementation: I'm using Hugging Face datasets

dataset_name = "INSERT_DATASET_NAME"

import pandas as pd
from datasets import load_dataset
my_dataset = load_dataset(dataset_name)

print(my_dataset)

df = pd.DataFrame(my_dataset["train"])
