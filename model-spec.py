#example with Google Bert
from transformers import BertForSequenceClassification, BertTokenizer, AdamW

model_name = 'google-bert/bert-base-uncased'
 
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=3)  

tokeniser = BertTokenizer.from_pretrained(model_name)
