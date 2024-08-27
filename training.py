# check this link for all training arguments: https://huggingface.co/docs/transformers/en/main_classes/trainer#transformers.TrainingArguments.adam_beta2
# check the video tutorial for the implementation: 

from transformers import Trainer, TrainingArguments

training_args = TrainingArguments(
    output_dir='ModelOutput', 
    evaluation_strategy="epoch",
    num_train_epochs=1,
    learning_rate=2e-5, 
    per_device_train_batch_size=8, 
    per_device_eval_batch_size=8, 
    weight_decay=0.01,
    adam_beta1=0.9,
    adam_beta2=0.999,
    no_cuda=True 
) 

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=training_dataset,
    eval_dataset=evaluation_dataset,
)

trainer.train()

