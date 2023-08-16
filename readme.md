# CGTA: An OpenAI-Powered Virtual Course Assistant 🧬

## Introduction

The purpose of this project is to utilize past CG@Penn class Piazza/Ed archives and ChatGPT Playground to make future TAs' lives easier by partially automating answers to Ed posts.

## Components
There are several components that come together to make CGTA work:

### 1. Post archive
I transcribed the Fall 2022 Piazza and Spring 2023 Ed archives for CIS 4600/5600: Interactive Computer Graphics, as well as the Fall 2022 Piazza archive for CIS 4620: Computer Animation, and stored them in .txt files organized by class > category > semester under the `data` folder. For the most part, you don't have to worry about these, and you definitely shouldn't edit them, but you can look at them if you're curious.

If you're a TA looking to add new questions and answers to the archive, please refer to the section entitled **Expanding the Archive**.

### 2. System prompt
There's another file in the `data` folder that isn't strictly data--rather, it's the system prompt for the OpenAI API to use (in the `playground` subfolder). Instead of asking plain vanilla ChatGPT to answer the students' questions, this system prompt is necessary to ensuring the answer only contains information relevant to the scope of the course. As with the post archive, you can take a look, but don't touch!

### 3. Python files
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

## General Use Instructions

In order to use CGTA, you'll need Visual Studio Code and an OpenAI account with credits on it*. Then, follow thse steps:

1. Download this repository and open in VS Code.
2. In VS Code, start a virtual environment.
   1. Go to the Command Palette and type ">Python: Create Environment...".
   2. Select "Venv".
   3. Select whatever Python installation you have on your computer (I'm using Python 3.9.6 64-bit, so this version or similarly recent will probably work best).
   4. When prompted for dependencies to install, select `requirements.txt`.
3. Open `response.py` and paste an OpenAI API key from your account as the value of `openai.api_key`. If you don't have one and don't know how to get one, do the following:
   1. Log into your OpenAI account in your browser.
   2. Click on your profile in the top-right corner and select "View API Key" from the drop-down menu that appears.
   3. Select "+ Create new secret key" and (optionally) give it a relevant name.
   4. Copy the secret key and save it somewhere.
   5. Paste it as the value of `openai.api_key`, as mentioned above.
4. Open `main.py` and run the Python script.
5. When prompted `ENTER COURSE:`, type the number corresponding to the course whose question(s) you would like to answer and press `Enter`.
6. When prompted `ENTER CATEGORY:`, type the number corresponding to the category/tag the post falls under in Piazza/Ed and press `Enter`. Some notes on how the posts are organized:
7. In the terminal, when prompted `PASTE QUESTION HERE:`, paste the student's question and press `Enter`.
8. The generated answer will print directly to the terminal. Paste this into Piazza/Ed and edit/rewrite as you see fit.
9.  To generate further answers for questions, repeat steps 7-8. To quit, simply press `Ctrl+C`.

*Note: If you don't have an OpenAI account with credits or some sort of way to pay for usage, just let me know and I'll find a way to send you my key securely.

## Known Limitations

Some things to consider while using CGTA:
- **Wonky confidence scoring:** The confidence score is just the similarity score of the archive post that is most similar to the student's question. Due to the nature of embeddings, the similarity score is calculated via similarity in wording, so a question with very similar concept, but worded differently, could potentially have a low similarity score, resulting in a low confidence score, even if the generated answer fits the question very well. I have yet to find a better way to calculate a more, ahem, *confident* confident score...
- **Convoluted setup:** The fact that it can only be run in VS Code with a virtual environment, and that input/output takes place entirely in the terminal, kind of sucks. I wanted to make this into a webapp or, even better, integrate it directly into Piazza/Ed so that CGTA could answer students' questions immediately as they come in, but a lack of understanding of how to integrate OpenAI API into a website (much less a Piazza/Ed extension...!) designated this luxury a timesink that I could not afford to pursue. Hopefully, whoever works on CGTA next will be able to take it further in that direction.
- **No follow-ups:** Unfortunately, the most recent version of GPT is incapable of handling follow-up questions in custom models--or at least, not reliably, and not without a very complex setup. Due to the nature of how CGTA can be used in its current state--namely, human TAs manually entering questions, vetting/editing answers, and posting them to Piazza as they are available--I do not foresee a situation in which CGTA would need to immediately answer a follow-up question in a single session, as there is an extremely low chance that the TA will see the first question within seconds/minutes of it being posted, answer it, have the student see the answer, and then have the student add to the thread within a few more seconds/minutes. Therefore, the feature is unnecessary for now.