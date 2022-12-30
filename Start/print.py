import openai

# Set the model API key
openai.api_key = "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"

# Set the model to use
model_engine = "text-davinci-002"

def generate_response(prompt):
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
       stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

# Test the model
prompt = "Hello, how are you today?"
response = generate_response(prompt)
print(response)
