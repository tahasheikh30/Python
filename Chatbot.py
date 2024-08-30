import google.generativeai as genai

# Configure the API key and model
genai.configure(api_key="AIzaSyAuHZ_WQU62nQIU9lFXmMmjbnz60WztrRQ")

# Set up the model and configuration
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config={
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 0,
        "max_output_tokens": 8192,
    },
    safety_settings=[
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    ],
)

# Start conversation
print("Start chatting with Emma (type 'exit' to end the conversation):")
conversation = model.start_chat(history=[])

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Send user input to the model and print the response
    conversation.send_message(user_input)
    response = conversation.last.text
    print("Emma:", response)
