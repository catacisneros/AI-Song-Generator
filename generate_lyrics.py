from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained model and tokenizer
model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Function to generate song lyrics
def generate_lyrics(prompt, max_length=150):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1)
    lyrics = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return lyrics

# Generate lyrics with a prompt
prompt = "Once upon a time in the rain"
print(generate_lyrics(prompt))
