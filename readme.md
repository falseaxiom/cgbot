#CGTA Test Run 🧬

##Introduction

Hello! Thank you so much for testing my independent study project! :D

The purpose of this project is to utilize past CG@Penn class Piazza/Ed archives and ChatGPT Playground to make future TAs' lives easier by partially automating answers to Ed posts.

The name of this repository is `cgbot`, but Dr. Lane advised against referring to it as a bot (scary branding?), so I've elected to call this virtual assistant **CGTA**. If you have any better names, let me know!

##Components

####1. Post archive
I transcribed the Fall 2022 Piazza and Spring 2023 Ed archives for CIS 4600/5600: Interactive Computer Graphics, as well as the Fall 2022 Piazza archive for CIS 4620: Computer Animation, and stored them in .txt files organized by class > category > semester under the `data` folder. For the most part, you don't have to worry about these these, and you definitely shouldn't edit them, but you can look at them if you're curious.

####2. System prompt
There's another file in the `data` folder that isn't strictly data--rather, it's the system prompt for the OpenAI API to use (in the `playground` subfolder). Instead of asking plain vanilla ChatGPT to answer the students' questions, this system prompt is necessary to ensuring the answer only contains information relevant to the scope of the course.

####3. Python files
Then, there are three Python files that do most of the heavy lifting:
- `embed.py`: Contains the `findSimilar()` function, which takes the student's `question` and the `tag` it falls under, then looks through the post archive to find the five most similar posts.
  - What this returns:
    - The question and these posts as a `user_prompt` for ChatGPT.
    - The similarity score of the top post (which we will later interpret as a `confidence_score`).
- `response.py`: Contains the `generateResponse()` function, which takes the aforementioned `user_prompt` and a permanent `system_prompt`, then uses the OpenAI API to generate a response to the question.
  - What this returns:
    - The `generated_text` containing the response to the student's question.
    - A `score_msg`, containing the aforementioned `confidence_score`, a colored emoji indicating how good the score is (🟢🟡🔴), and a possible suggestion on whether the generated answer should be altered or rewritten.
- `main.py`: Where the user runs everything from. Doesn't return anything--basically just prints the `generated_text` and `score_msg`.

##General Use Instructions

In order to use CGTA, you'll need Visual Studio Code and an OpenAI account with credits on it*. Then, follow thse steps:

1. Download this repository and open in VS Code.
2. In VS Code, start a virtual environment.
   1. Go to the Command Palette and type ">Python: Create Environment...".
   2. Select "Venv".
   3. Select whatever Python installation you have on your computer (I'm using Python 3.9.6 64-bit, so this version or similarly recent will probably work best).
   4. When prompted for dependencies to install, select `requirements.txt`.
3. Open `response.py` and paste an OpenAI API key from you account as the value of `openai.api_key`. If you don't have one and don't know how to get one, do the following:
   1. Log into your OpenAI account in your browser.
   2. Click on your profile in the top-right corner and select "View API Key" from the drop-down menu that appears.
   3. Select "+ Create new secret key" and (optionally) give it a relevant name.
   4. Copy the secret key and save it somewhere.
   5. Paste it as the value of `openai.api_key`, as mentioned above.
4. Open `main.py` and run the Python script.
5. In the terminal, when prompted `PASTE QUESTION HERE:`, paste the student's question and press `Enter`.
6. When prompted `ENTER CATEGORY:`, type the category/tag the post falls under in Piazza/Ed. Some notes on how the posts are organized:
   1. Homework posts are tagged `hw1` or similar.
   2. All Minecraft posts, regardless of milestone, are tagged `minecraft`.
   3. Anything that is not related to homework or Minecraft are tagged `general`.
   4. All tags are case-sensitive and must be typed exactly as shown above. For example, `hw01`, `HW1`, `Minecraft`, and `GENERAL` would not be accepted.
7. The generated answer will print directly to the terminal. Paste this into Piazza/Ed and edit/rewrite as you see fit.
8. To generate further answers for questions, repeat steps 4-8.

*Note: If you don't have an OpenAI account with credits or some sort of way to pay for usage, just let me know and I'll find a way to send you my key securely.

##Testing Instructions

Once again, thank you so much for testing CGTA, and even more thanks for reading this far! This part should only take about 5-10 minutes, depending on how thorough you want to be. Here's what you need to do:

1. Following the general use instructions from the previous section, ask CGTA at least 3-5 questions that a CIS 4600/5600 student could plausibly ask. You can even just straight-up paste questions from Piazza posts from Spring 2022 or earlier, as I do not have access to these posts and as such did not add them to the archive.
2. Copy and paste these questions and CGTA's answers somewhere temporarily, like a Notes app.
3. Consider how you'd edit/rewrite these generated answers (or if you'd do so at all).
4. Send me a brief email with the following information (preferably organized and labeled in this order, but no big deal if not):
   1. Your questions and CGTA's answers
   2. Thoughts on the quality of CGTA's answers
   3. Thoughts on the human TA review stats and whether the confidence score is helpful/should be calculated some other way
   4. Thoughts on ease of use (including clarity of general instructions)
   5. Any general suggestions for improvement
   6. Your Venmo handle (If we don't see each other before I move out, I'll send you boba money!)

Thank you! You're the best! <3

## Known limitations

Some things to consider while using CGTA:
- **Single course support:** Despite containing a CIS 4620/5620 archive, CGTA currently only supports CIS 4600/5600. This is for simplicity's sake, since everyone testing it was previously a CIS 4600/5600 TA, and it would be annoying to have to select a class every time you paste a question if the class is always the same. This can be changed pretty easily after testing, but I still have to figure out a way to let the user enter the class just one time and get answers to a bunch of questions.
- **Wonky confidence scoring:** The confidence score is just the similarity score of the archive post that is most similar to the student's question. Due to the nature of embeddings, the similarity score is calculated via similarity in wording, so a question with very similar concept, but worded differently, could potentially have a low similarity score, resulting in a low confidence score, even if the generated answer fits the question very well. I have yet to find a better way to calculate a more, ahem, *confident* confident score...
- **Convoluted setup:** The fact that it can only be run in VS Code with a virtual environment, and that input/output takes place entirely in the terminal, kind of sucks. I wanted to make this into a webapp or, even better, integrate it directly into Piazza/Ed so that CGTA could answer students' questions immediately as they come in, but a lack of understanding of how to integrate OpenAI API into a website (much less a Piazza/Ed extension...!) designated this luxury a timesink that I could not afford to pursue. Hopefully, whoever works on CGTA next will be able to take it further in that direction.