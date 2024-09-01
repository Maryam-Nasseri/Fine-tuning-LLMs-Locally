# Fine-tuning-LLMs-Locally
The process for fine-tuning LLMs Locally without third-party APIs and platform fees. Before starting to fine-tune a model, make sure you actually need to! Fine-tuning LLMs can be a lengthy process and computationally expensive. It is a good idea to test the model's performance on your task-specific data and try other less-demanding methods such as In-Context-Learning (ICL). It is also a good practice to fine-tune with smaller batches of data and record the improvement (i.e., output accuracy and validation loss) at each step, before increasing the number of training data examples.

## Testing the LLM on the task

-- Install dependencies as in `dependencies.py` for the sentiment analysis task.

-- Select a pre-trained model with fewer parameters, preferably a lightweight one that is easier to load and train.

-- Model specifications including model name, tokeniser, and sequence classifier (for classification tasks), as in `model-spec`.

--  Set the parameters for the main task function, e.g., sentiment analysis as in `function`(e.g., padding, truncation, prediction labels, etc). Specify the number of examples to provide to the LLM from the external data source; the dataset format should follow the LLM's training template.

## The process for fine-tuning LLMs locally 

-- Load the dataset you want to fine-tune your model on; you can use Pandas `DataFrame` to sort/select a portion of the training dataset, as in `load_data`.

 -- Tokenisation: tokenise the training and evaluation sets of the data (specify the number of examples). Similar to `model spec` except we use the dataset for tokenisation as in `specify_data`.

 -- Initialise the model with the 'function` as before with tokenised training and evaluation sets.

 -- Training or fine-tuning the model using the `Trainer` module from the `Transformers` library as in `training`.  Check the extended set of arguments at [the Trainer class of TRansformers](https://huggingface.co/docs/transformers/en/main_classes/trainer)

 ## Tutorial video: step-by-step guide to fine-tuning a large language model

This video tutorial is easiest way to fine-tune a large language model 100% free and locally without using any API or third-party platform.

Terms and concepts discussed: Bidirectional Encoder Representations from Transformers, tokenisation, embedding, encoding, task head, encoder-only Transformer models, sequence classification

[![Easiest tutorial to fine-tune LLMs locally in just 20 minutes!](https://img.youtube.com/vi/oG0jsMVTg9w/maxresdefault.jpg)](https://youtu.be/oG0jsMVTg9w) 
