import tiktoken


text = "The dog chased the cat."

encoding = tiktoken.get_encoding("gpt2")

token_ids = encoding.encode(text)

# print("Original text:")
# print(text)

# print("\nToken IDs:")
# print(token_ids)

# print("\nTokens:")
# for token_id in token_ids:
#     token = encoding.decode([token_id])
#     print(f"{token_id} -> {repr(token)}")