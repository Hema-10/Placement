responses = {
    "hi": "Hello!",
    "how are you": "I'm good, thank you!",
    "bye": "Goodbye!"
}

while True:
    msg = input("You: ").lower()
    if msg == "exit":
        break
    print("Bot:", responses.get(msg, "I don't understand."))
