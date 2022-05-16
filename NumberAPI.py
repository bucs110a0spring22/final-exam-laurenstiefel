import requests


response = requests.get('https://x-math.herokuapp.com/api/random?max=10&min=1')
  
    
number=response.json()["answer"]
print(f'Number is: {number}\n')





