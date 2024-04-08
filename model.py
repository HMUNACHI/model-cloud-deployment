from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_name = "SamLowe/roberta-base-go_emotions"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)