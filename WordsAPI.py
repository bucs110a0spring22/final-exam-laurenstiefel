import requests
response = requests.get("http://numbersapi.com/random/year?json")
#self.url=("")

fact=response.json()
word_list=fact['text'].split(" ")[1:]
