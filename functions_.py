def greet():
    message = "hello"
    new_message = message.capitalize()
    return new_message

greetings = greet()
print(greetings)

print(new_message)  # problem of scope