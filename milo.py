import openai

openai.api_key = ''

# Define a function to get the response from OpenAI
def get_response(prompt):
    parameters = {
        "model": 'text-davinci-002',
        "prompt": prompt,
        "temperature": 0.5,
        "max_tokens": 100,
        "n": 1,
        "stop": None,
    }

    # Generate text using OpenAI API
    response = openai.Completion.create(**parameters)

    # Return the generated text
    return response.choices[0].text.strip()

# Define a function to check if the user's input is programming-related
def is_programming_related(user_input):
    programming_keywords = ["programming", "coding", "program", "code", "developer",
                            "software", "development", "computer science"
                            "web development" "app development", "api", "web", "app",
                            "javascript", "python", "java", "C++", "C#" "php"
                            "ruby", "html", "css", "sql", "swift", "kotlin", "go",
                            "rust", "scala", "bash", "c", "r", "matlab", "perl",
                            "haskell", "lua", "clojure", "erlang", "elixir", "dart",
                            "assembly" "fortran", "lisp", "prolog", "scheme cobol",
                            "error", "bug", "debug", "fix", "issue", "problem", "crash",
                            "compile", "compile error", "syntax error", "runtime error",
                            "exception", "exception error", "stack trace", "stack overflow",
                            "memory", "memory error", "memory 1eak", "memory overflow"]

    # Check if the user's input contains any programming keywords
    for keyword in programming_keywords:
        if keyword in user_input.lower():
            return True
    return False

# Main loop for chatbot
print ("Welcome to the programming Chat Assistant. Type 'exit' to quit.")
while True:
    # Get the user input
    user_input = input("You : ")

    # Check if user wants to exit
    if user_input.lower() == 'exit':
        print("Chatbot: GoodBye !!")
        break

    # Check if the user's input is programming-related
    if is_programming_related(user_input):

        # Generate response
        prompt = f"Programming Question: {user_input} \nChatbot Response: "
        response = get_response(prompt)

        # Print the response
        print("Chatbot:", response)

    else:

        # Print error message
        print("Chatbot : Sorry,I only answer to programming-related questions")
s
