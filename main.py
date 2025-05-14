import requests
import colorama
from colorama import Fore, Back, Style
import sys
import os
from collections import Counter
from datetime import datetime
colorama.init()
word = requests.get(url=f"https://www.nytimes.com/svc/wordle/v2/{datetime.today().strftime('%Y-%m-%d')}.json").json()['solution']
guesses = []
os.system('cls' if os.name == 'nt' else 'clear')
while len(guesses) < 6:
    print(f"""
        {Fore.YELLOW}██████  ██    ██ {Fore.RESET}██████  ██████  ██      ███████ 
        {Fore.YELLOW}██   ██  ██  ██  {Fore.RESET}██   ██ ██   ██ ██      ██      
        {Fore.YELLOW}██████    ████   {Fore.RESET}██████  ██   ██ ██      █████   
        {Fore.YELLOW}██         ██    {Fore.RESET}██   ██ ██   ██ ██      ██      
        {Fore.YELLOW}██         ██    {Fore.RESET}██   ██ ██████  ███████ ███████ 
                                            
                                            """)
    for guess in guesses:
        print(guess)
    guess = str(input('Type your guess:'))
    if len(guess) != 5:
        print("Guess has to be 5 letters!")
    elif not guess.isalpha:
        print("Guess can't contain numbers or symbols!")
    elif len(guess) == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        if guess == word:
            print(f'{Fore.GREEN}{guess}')
            print('you guessed!')
            input('')
            sys.exit()
        else:
            fguess = ''
            word_counter = Counter(word)
            used_letters = Counter()
            for index, char in enumerate(guess):
                if char in word and char == word[index]:
                    fguess += Fore.GREEN + char + Fore.RESET
                    used_letters[char] += 1
                elif char in word and used_letters[char] < word_counter[char]:
                    fguess += Fore.YELLOW + char + Fore.RESET
                    used_letters[char] += 1
                else: 
                    fguess += char
            guesses.append(fguess)
print(f"""
        {Fore.YELLOW}██████  ██    ██ {Fore.RESET}██████  ██████  ██      ███████ 
        {Fore.YELLOW}██   ██  ██  ██  {Fore.RESET}██   ██ ██   ██ ██      ██      
        {Fore.YELLOW}██████    ████   {Fore.RESET}██████  ██   ██ ██      █████   
        {Fore.YELLOW}██         ██    {Fore.RESET}██   ██ ██   ██ ██      ██      
        {Fore.YELLOW}██         ██    {Fore.RESET}██   ██ ██████  ███████ ███████ 
                                            
                                            """)
print(f'{Fore.RED}You couldn\'t guess it! The word was {word}')
input('')
            
