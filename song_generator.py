from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

prompt = "Write a song about love and heartbreak."
inputs = tokenizer.encode(prompt, return_tensors="pt")

outputs = model.generate(inputs, max_length=200, num_return_sequences=1)
generated_song = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(generated_song)
