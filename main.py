import argparse
import json
from src.core import InContextLearning

def main():
    parser = argparse.ArgumentParser(description='In-Context Learning with Transformers')
    parser.add_argument('--model', type=str, default='bert-base-uncased', help='Transformer model to use')
    parser.add_argument('--prompt', type=str, required=True, help='Input prompt for the model')
    args = parser.parse_args()
    
    model = InContextLearning(args.model)
    output = model.generate(args.prompt)
    print(output)

if __name__ == '__main__':
    main()
