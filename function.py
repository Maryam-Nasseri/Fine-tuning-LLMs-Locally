# just a quick function to analyse sentiment of a text/tweet with 3 labels; you can modify this function for any other type of text
# check video tutorial for implementation
def sentiment_analysis(text):

    input_text = tokeniser(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    pred = model(**input_text)
    pred_class = torch.argmax(pred.logits, dim=1)
    class_labels = {0: "negative", 1: "neutral", 2: "positive"}
    sentiment = class_labels[pred_class.item()]
    return sentiment
  
print("The sentiment for 'how on earth can I analyse this?' is: ", sentiment_analysis("how on earth can I analyse this?"))
