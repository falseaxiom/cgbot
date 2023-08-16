import response

# tag index
TAGS = {
    "cis4600": ["hw0","hw1","hw2","hw3","hw4","hw5","hw6","hw7","minecraft","general"],
    "cis4620": ["general","hw1","hw2","hw3","hw4","hw5","hw6","hw7",]
}

# intro
print("GREETINGS! I am CGTA, an assistive tool that auto-generates answers to CG@Penn questions.")
print()

# user inputs student's course
print("If you are a TA for CIS 4600/5600: INTERACTIVE COMPUTER GRAPHICS, type ' 1 '.")
print("If you are a TA for CIS 4620/5620: COMPUTER ANIMATION, type ' 2 '.")
print("If you would like to quit CGTA, press CTRL + C.")
c = input("ENTER COURSE: ")
while (c.strip() != '1' and c.strip() != '2'):
    print("Invalid input. Please enter '1' or '2' according to instructions above, or quit using CTRL + C.")
    c = input("ENTER COURSE: ")

# give category choice based on course
if (c.strip() == '1'):
    course = 'cis4600'
    print()
    print("Please enter a number according to the category of the student's question:")
    print("0: hw0")
    print("1: hw1")
    print("2: hw2")
    print("3: hw3")
    print("4: hw4")
    print("5: hw5")
    print("6: hw6")
    print("7: hw7")
    print("8: minecraft")
    print("9: general")
    t = input("ENTER CATEGORY: ")
elif(c.strip() == '2'):
    course = 'cis4620'
    print()
    print("Please enter a number according to the category of the student's question:")
    print("0: general")
    print("1: hw1")
    print("2: hw2")
    print("3: hw3")
    print("4: hw4")
    print("5: hw5")
    print("6: hw6")
    print("7: hw7")
    t = input("ENTER CATEGORY: ")

# get tag based on course & tag number
tag = TAGS[course][int(t)]
print()

# question loop
while (True):
    question = input("PASTE QUESTION HERE: ")
    print()

    # generate response (printed to terminal)
    generated_response, score_msg = response.generateResponse(course, tag, question)

    # print everything
    print(generated_response)
    print()
    print("----- FOR HUMAN TA REVIEW - DO NOT COPY BELOW -----")
    print()
    print(score_msg)
    print()
    print("---------------------------------------------------")
    print()

    # next question
    print("If you would like an answer to a new question in the same course and category, type your question below.")
    print("If you would like to quit CGTA, press CTRL + C.")
    print()