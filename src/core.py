import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

class InContextLearning:
    def __init__(self, model_name):
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    def generate(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors='pt')
        output = self.model.generate(**inputs)
        return self.tokenizer.decode(output[0], skip_special_tokens=True)
