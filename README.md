# AI-CHATBOT-WITH-NLP

COMPANY : CODTECH IT SOLUTIONS

NAME : KUNCHARAPU VARUN REDDY

INTERN ID : CTO8SGE

DOMAIN : PYTHON PROGRAMMING

DURATION :4 WEEKS

*MENTOR* : NEELA SANTHOSH

## DESCRIPTION OF THE PROJECT  ##
This code is a simple chatbot program that uses natural language processing (NLP) techniques to interact with users.I have worked on google colab for this project and it was very challenging for me.I have taken help of online sources to make it happen.And the text_file i have taken is from wikipedia i.e about cinema . Below is a detailed explanation of the code.

Modules used :-
numpy (np): This module is used for numerical computations. In this code, it helps in handling arrays and mathematical operations.

nltk (Natural Language Toolkit): This is a powerful library for working with human language text. It provides tools for tokenization, lemmatization, and other NLP tasks.

string: This module contains useful string operations, such as handling punctuation.

random: This module is used to generate random responses, especially for greeting interactions.

sklearn.feature_extraction.text.TfidfVectorizer: This is used to convert text into numerical vectors using the TF-IDF method, which helps in understanding the importance of words in a document.

sklearn.metrics.pairwise.cosine_similarity: This function calculates the cosine similarity between vectors, which is used to find how similar two pieces of text are.

Here is how the code works:-
Loading and Preprocessing the Document:

The code opens a text file (codtech_task_3.txt) and reads its content. The text is converted to lowercase to avoid case sensitivity issues.

Downloading NLTK Data:

The code downloads necessary NLTK resources like punkt (for tokenization), wordnet (for lemmatization), and omw-1.4 (Open Multilingual WordNet). These resources are essential for text processing tasks.

Tokenization:

The text is split into sentences (sentence_tokens) and words (word_tokens) using NLTK's tokenization functions. Tokenization is the process of breaking text into smaller units like sentences or words.

Lemmatization:

Lemmatization reduces words to their base or root form (e.g., "leaves" becomes "leav"). The LemTokens function applies lemmatization to a list of tokens. Punctuation is removed using a translation table created with the string module.

Greeting Handling:

The chatbot recognizes common greetings like "hello" or "hi" and responds with a random greeting from a predefined list (greet_responses).

TF-IDF Vectorization:

The TfidfVectorizer converts the sentences into numerical vectors using the TF-IDF method. This helps in understanding the importance of words in the context of the document.

Response Generation:

The response function calculates the cosine similarity between the user's input and the sentences in the document. It finds the most similar sentence and returns it as the chatbot's response. If no similarity is found, it responds with "I am sorry! I don't understand you."

Main Conversation Loop:

The chatbot starts by introducing itself and waits for user input. If the user types "bye," the chatbot ends the conversation. If the user inputs a greeting, the chatbot responds with a random greeting. Otherwise, it processes the input, generates a response, and continues the conversation.
This chatbot uses NLP techniques like tokenization, lemmatization, and TF-IDF vectorization to understand and respond to user inputs. It can handle greetings and generate responses based on the similarity between the user's input and the preprocessed text. The code is designed to be simple and easy to understand, making it a good starting point for building more advanced chatbots.

# THIS IS THE INPUT FILE (i.e about cinema)

[codtech_task_3.txt](https://github.com/user-attachments/files/19143945/codtech_task_3.txt)


# HERE IS THE OUTPUT FOR THE CODE

![Image](https://github.com/user-attachments/assets/d2c32b79-03f3-4d35-8080-e79bd8f1d559)

# THANK YOU FOR READING #


