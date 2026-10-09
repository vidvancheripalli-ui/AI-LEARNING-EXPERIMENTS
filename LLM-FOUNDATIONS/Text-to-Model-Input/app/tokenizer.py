import tiktoken
class Tokenizer:
    def __init__(self):
        self.encoding = tiktoken.get_encoding("gpt2")

    def tokenize(self, text: str):
        token_ids = self.encoding.encode(text)
        tokens = [self.encoding.decode([token_id]) for token_id in token_ids]
        return tokens

    def encode(self, text: str):
        return self.encoding.encode(text)

    def decode(self, token_ids):
        return self.encoding.decode(token_ids)

# tokenizer = Tokenizer()
# text = input("Enter text to tokenize: ")
# tokens = tokenizer.tokenize(text)
# print("Original text:")
# print(text)
# ids = tokenizer.encode(text)
# print("\nToken IDs:")
# print(ids)  
# print("\nTokens:")
# print(tokens)
# decoded_text = tokenizer.decode(ids)
# print("\nDecoded text:")        
# print(decoded_text)