import os
import openai
import math
import embed
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# add your own OpenAI API key to your env variables as OPENAI_API_KEY
# OR just type it in here directly (but DO NOT publish anywhere!!!)
openai.api_key = ""   # os.environ["OPENAI_API_KEY"]

# generates response to student's question using GPT playground
def generateResponse(course, tag, question):
    # import system prompt from /data/playground
    file = open('./data/playground/prompt.txt', 'r')
    system_prompt = file.read()

    # get user prompt using findSimilar()
    user_prompt, confidence_score = embed.findSimilar(course, tag, question)

    print("Generating response...")

    # add both prompts to messages
    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]

    # pasted playground settings
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=messages,
        temperature=0.8,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # generate CGTA response
    generated_text = response.choices[0].message.content.strip()

    print("Generated!")
    print()
    print("CGTA's ANSWER: ")
    print()
    
    # add extra info for human TA reviewer
    # color rating and recommendation depending on confidence score
    confidence_score = float(confidence_score)
    rating = "🟢"
    rec = ""
    if (confidence_score < 0.5):
        rating = "🟡"
        rec = "It is suggested that the human TA modify this answer to better suit the student's needs."
    elif (confidence_score < 0.2):
        rating = "🔴"
        rec = "There are no archived posts that closely match this student's question, so the human TA should write their own answer."
    # score report
    report = " My answer has a confidence score of " + str(math.floor(confidence_score*100)) + "%, based on similarity to previous posts in my archive. "
    # concatenate everything
    score_msg = rating + report + rec

    return generated_text, score_msg

