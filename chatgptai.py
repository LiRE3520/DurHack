from together import Together

def getCities():
# Initialize the client with your API key
    client = Together(api_key="45433e26c5ee64c5e460981acf28b9d18b0f4df6060e14f35c29992bb7c9ddfd")

# Call the chat completion without the `_gl` parameter
    response = client.chat.completions.create(
        model="meta-llama/Llama-Vision-Free",
        messages = [{"role": "user", "content": "If I'm interrailing in Europe, what cities are good to visit if I like cheese? Put them in order I would visit, and in this format: city1, city2, city3,... -It is very essential you only list the cities in my given format, and include no other text in your response."}],  # Add your messages here
        max_tokens=None,  # Use Python's `None` if you don't want to limit tokens
        temperature=0.7,
        top_p=0.7,
        top_k=50,
        repetition_penalty=1,
        stop=["<|eot_id|>", "<|eom_id|>"],
        stream=True
    )

    cities = ""

# Stream the response tokens as they arrive
    for token in response:
    # Check if 'choices' and 'delta' are present and have content
        if hasattr(token, 'choices') and token.choices and hasattr(token.choices[0], 'delta'):
            if hasattr(token.choices[0].delta, 'content'):
                cities += token.choices[0].delta.content
    return cities
print(getCities())