import random 
from WordsAPI import word_list
from WordsAPI import fact

#from numberAPI import number
from NumberAPI import number

def get_word():
  word=random.choice(word_list)
  print(fact)
  instructions = 'Instructions: This game is a game of hangman that picks one word from a random fact based on a historical event that happened in a random year.That fact is displayed to allow you to guess words based on the displayed words. The number of guesses allowed is the number next to "Number is:" and that is based on a randomly performed mathamatical calculation between 2 numbers between 1 and 10. Enjoy!!'
  print(instructions)
  #print(f'Word list is: {word_list}\n')
  #print(f'Random word is: {word}')
  return word.upper()

def play(word):
  word_completion="_"* len(word)
  guessed=False
  guessed_letters=[]
  guessed_words=[]
  tries=number
  print("Let's play Hangman!")
  print (word_completion)
  print("\n")
  while not guessed and tries > 0:
    guess = input("Please guess a letter or word: ").upper()
    word_as_list=list(word_completion)
    if len(guess)==1 and guess.isalpha():
     
      if guess in guessed_letters:
        print ("You already guesseed the letter", guess)
      elif guess not in word:
        print(guess, "is not in the word.")
        tries -=1
        guessed_letters.append(guess)
      else:
        print("Good job,", guess, "is in the word")
        guessed_letters.append(guess)
        word_as_list=list(word_completion)
        indices=[i for i, letter in enumerate(word) if letter==guess]
        for index in indices:
          word_as_list[index]=guess
        word_completion="".join(word_as_list)
        
        if "_" not in word_completion:
          guessed=True
    elif len(guess)==len(word) and guess.isalpha():
        if guess in guessed_words:
          print("You already guessed the word", guess)
        elif guess !=word:
          print(guess, "is not the word.")
          tries-=1
          guessed_words.append(guess)
        else:
          guessed=True
          word_completion=word
   
    else:
      print("Not a valid guess.")
    
    if not guessed:
      print(word_completion)
    
  if guessed:
    print("Congrats, you guessed the word! You win!")
    print (word_completion)
    
  else:
    print("Sorry, you ran out of tries. The word was " +word + ". Maybe next time")
    

def main():
  #napi=NumberAPI.NumberAPI()
  #response=r.json()["answer"]
  #print(f'Number is: {number}\n')
  #number=napi.get()
  word=get_word()
  play(word)
 
if __name__=="__main__":
  main()
