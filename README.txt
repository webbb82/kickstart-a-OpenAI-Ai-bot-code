README
IMPORTANT------IMPORTANT------IMPORTANT READ ME!!!!!!
This iS NOT a product. I started this as a project for my personal use. I am posting this code to help others that was to try ouy OpenAI but don't know how or just dont want to mess with coding. So you are on your own with this. 

^		^		^		^		^		^		^
---------------------------------------------------------

THis code writen in Python will spawn a helpful AI chatbot. It can learn and be trained to match your personal needs. This starter AI specialises in coding help. 

Prerequisits:
Need to download and install OpenAI
Signup at OpenAI and get a api key


Install open AI enter in terminal
~ ❯ pip install openai

Sign-up at OpenAI and get yourself a shiny new API key
https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/

    - Go to OpenAI's website at "platform.openai.com" and sign in with an OpenAI account.
    
    - Click your profile icon at the top-right corner of the page and select "View API Keys."
    
    - Click "Create New Secret Key" to generate a new API key.

    Once you have the API key open up your python document milo.py and at the top put your key in like this 

---
    import openai
                    V  V  V---key goes here
    openai.api_key =        < <  <  

    # Define a function to get the response from OpenAI
    def get_response(prompt):
        parameters = {
            "model": 'text-davinci-002',
            "prompt": prompt,
---

Thats it. Open up your IDE open this file Milo.py and start chatting
