import response

# user inputs student's question and category
question = input("PASTE QUESTION HERE: ")
tag = input("ENTER CATEGORY: ")
print()

# generate response (printed to terminal)
response.generateResponse(question, tag)