import os
import sys
import torch
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('all-MiniLM-L6-v2')

# find the most similar posts to a given question in a given tag
# return as user prompt
def findSimilar(question, tag):
    # get all posts from same tag as question
    # with student's question as the first entry
    posts = []
    posts.append(question)

    # go thru files in tag folder to collect posts
    folder = './data/cis4600/' + tag + '/'
    for filename in os.listdir(folder):
        filepath = folder + filename
        file = open(filepath, 'r')
        po = file.read().split('###question ')
        po = po[1:]                     # get rid of empty first entry
        po = [p.strip() for p in po]    # get rid of trailing newlines
        posts.extend(po)

    # get only questions
    questions = []
    questions.append(question)
    questions.extend([p.split("#")[0] for p in posts[1:]])

    # encode all questions
    embeddings = model.encode(questions)

    # compute cosine similarity for all 
    cos_sim = util.cos_sim(embeddings[0], embeddings)

    # add all pairs to a list with their cosine similarity score
    most_similar_posts = []
    for i in range(len(cos_sim[0])):
        most_similar_posts.append([cos_sim[0][i], i])

    # sort list by the highest cosine similarity score
    most_similar_posts = sorted(most_similar_posts, key=lambda x: x[0], reverse=True)

    # delete question from most similar posts bc it's the same post
    most_similar_posts = most_similar_posts[1:]

    ### DEPRECATED CODE START: this used to just print out something to copypaste
    ### keeping for testing purposes
    # # print question
    # print("QUESTION:\n" + question + "\n")

    # # print top 5 most relevant posts
    # print("INFORMATION:")
    # for score, i in most_similar_posts[0:5]:
    #     #print("{} \t {:.4f}".format(posts[i], score))
    #     print(posts[i])
    #     print("confidence score: {:.3f}\n".format(score))
    ### DEPRECATED CODE END

    # create user prompt
    # question
    user_prompt = "QUESTION:\n" + question + "\n\n"
    # top 5 most relevant posts
    user_prompt += "INFORMATION:\n"
    for score, i in most_similar_posts[0:5]:
        user_prompt += posts[i] + "\n"
        user_prompt += "similarity score: {:.3f}\n\n".format(score)

    # also get confidence score based on similarity of most relevant post
    confidence_score = "{:.3f}\n\n".format(most_similar_posts[0][0])

    return user_prompt, confidence_score


# prompt input
# question = input("PASTE QUESTION HERE: ")
# tag = input("ENTER CATEGORY: ")
# print()

# findSimilar(question, tag)