import requests
import colorama
from colorama import Fore, Back, Style
import sys
import os
from collections import Counter
from datetime import datetime
import re
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
        if guess.lower() == word.lower():
            print(f'{Fore.GREEN}{guess}')
            print(f'you guessed!{Fore.RESET}')
            guesses.append(Fore.GREEN + guess.lower())
            pattern = re.compile(r'(\x1b\[[0-9;]*m)|([A-Za-z])')

            def replace_letters_keep_colors(text, replacement="██"):
                def replacer(match):
                    if match.group(1):
                        return match.group(1) 
                    elif match.group(2):
                        return replacement 

                return pattern.sub(replacer, text)

            for guess in guesses:
                print(replace_letters_keep_colors(guess))
            input('')
            sys.exit()
        else:
            fguess = ''
            word_counter = Counter(word)
            used_letters = Counter()
            for index, char in enumerate(guess):
                if char.lower() in word and char.lower() == word[index]:
                    fguess += Fore.GREEN + char.lower() + Fore.RESET
                    used_letters[char] += 1
                elif char in word and used_letters[char] < word_counter[char]:
                    fguess += Fore.YELLOW + char.lower() + Fore.RESET
                    used_letters[char] += 1
                else: 
                    fguess += char.lower()
            guesses.append(fguess.lower())
print(f"""
        {Fore.YELLOW}██████  ██    ██ {Fore.RESET}██████  ██████  ██      ███████ 
        {Fore.YELLOW}██   ██  ██  ██  {Fore.RESET}██   ██ ██   ██ ██      ██      
        {Fore.YELLOW}██████    ████   {Fore.RESET}██████  ██   ██ ██      █████   
        {Fore.YELLOW}██         ██    {Fore.RESET}██   ██ ██   ██ ██      ██      
        {Fore.YELLOW}██         ██    {Fore.RESET}██   ██ ██████  ███████ ███████ 
                                            
                                            """)
print(f'{Fore.RED}You couldn\'t guess it! The word was {word}')
input('')
            
