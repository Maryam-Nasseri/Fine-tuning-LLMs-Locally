# Fine-tuning-LLMs-Locally
The process for fine-tuning LLMs Locally without third-party APIs and platform fees. Before starting to fine-tune a model, make sure you actually need to! Fine-tuning LLMs can be a lengthy process and computationally expensive. It is a good idea to test the model's performance on your task-specific data and try other less-demanding methods such as In-Context-Learning (ICL). It is also a good practice to fine-tune with smaller batches of data and record the improvement (i.e., output accuracy and validation loss) at each step, before increasing the number of training data examples.

## Testing the LLM on the task

-- Install dependencies as in `dependencies.py` for the sentiment analysis task.

-- Select a pre-trained model with fewer parameters, preferably a lightweight one that is easier to load and train.

-- Model specifications including model name, tokeniser, and sequence classifier (for classification tasks), as in `model-spec`.

--  Set the parameters for the main task function, e.g., sentiment analysis as in `sentiment-analysis`(e.g., padding, truncation, prediction labels, etc).

## The process for fine-tuning LLMs locally 

 The external data source format should follow the LLM's training template.
