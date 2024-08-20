# Fine-tuning-LLMs-Locally
The process for fine-tuning LLMs Locally without third-party APIs and platform fees. Before starting to fine-tune a model, make sure you actually need to! Fine-tuning LLMs can be a lengthy process and computationally expensive. It is a good idea to test the model's performance on your task-specific data and try other less-demanding methods such as In-Context-Learning (ICL). It is also a good practice to fine-tune with smaller batches of data and record the improvement (i.e., output accuracy and validation loss) at each step, before increasing the number of training data examples.

## The process for fine-tuning LLMs locally 

1. Select a pre-trained model with fewer parameters, preferably a lightweight one that is easier to load and train.
2. Model specifications including model name, tokeniser, and sequence classifier (for classification tasks), as in `model spec`.
3. 
