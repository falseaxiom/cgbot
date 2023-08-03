import response

# user inputs student's question and category
question = input("PASTE QUESTION HERE: ")
tag = input("ENTER CATEGORY: ")
print()

# generate response (printed to terminal)
generated_response, score_msg = response.generateResponse(question, tag)

# print everything
print(generated_response)
print()
print("----- FOR HUMAN TA REVIEW - DO NOT COPY BELOW -----")
print()
print(score_msg)