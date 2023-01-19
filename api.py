from httpx import post
from sys import argv

# https://beta.openai.com/account/api-keys

api_key = "Your api Key"
url = "https://api.openai.com/v1/engines/text-davinci-003/completions"

def main(prompt):
    re = post(url, json={
        "prompt": prompt,
        "max_tokens": 150,
        "stop" : [" Human:", " AI:"],
        "temperature" : 0.9,
        "top_p" : 1,
        "frequency_penalty" : 0,
        "presence_penalty" : 0.6,
    }, headers={
        "Authorization": f"Bearer {api_key}"
    })
    print(re.json()["choices"][0]["text"])

if __name__ == '__main__':
    try:
        main(argv[1])
    except:
        print("Usage : python3 api.py 'Hello bro !'")