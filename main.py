import numpy as np
import nltk
import string
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# reading the file contents
f = open(r'/content/codtech_task_3.txt', 'r', errors='ignore')
raw_doc = f.read()
raw_doc = raw_doc.lower()  # Convert entire text to lower case

# Download necessary NLTK data
nltk.download('punkt_tab')  
nltk.download('punkt')  
nltk.download('wordnet')  
nltk.download('omw-1.4')

# Tokenize the document
sentence_tokens = nltk.sent_tokenize(raw_doc)
word_tokens = nltk.word_tokenize(raw_doc)

# Lemmatization
lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Greetings
greet_inputs = ('hello', 'hi', 'greetings', 'sup', 'whatsup', 'hey')
greet_responses = ('hi', 'Hey', 'Hey There!', 'There there!')

def greet(sentence):
    for word in sentence.split():
        if word.lower() in greet_inputs:
            return random.choice(greet_responses)

# Initialize TF-IDF Vectorizer
TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
tfidf = TfidfVec.fit_transform(sentence_tokens)

def response(user_response):
    robo1_response = ''
    user_response_tfidf = TfidfVec.transform([user_response])
    vals = cosine_similarity(user_response_tfidf, tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        robo1_response = robo1_response + "I am sorry! I don't understand you"
        return robo1_response
    else:
        robo1_response = robo1_response + sentence_tokens[idx]
        return robo1_response

# Main conversation loop
flag = True
print("BOT: My name is Chinni. Let's have a conversation! Also, if you want to exit any time, just type Bye!")
while flag:
    user_response = input()
    user_response = user_response.lower()
    if user_response != 'bye':
        if user_response == 'thanks' or user_response == 'thank you':
            flag = False
            print("BOT: You are welcome..")
        else:
            if greet(user_response) is not None:
                print("BOT: " + greet(user_response))
            else:
                sentence_tokens.append(user_response)
                word_tokens = word_tokens + nltk.word_tokenize(user_response)
                final_words = list(set(word_tokens))
                print("CHINNI: ", end="")
                print(response(user_response))
                sentence_tokens.remove(user_response)
    else:
        flag = False
        print("BOT: Goodbye! Take care ")
