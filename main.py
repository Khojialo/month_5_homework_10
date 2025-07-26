import asyncio

# Question 1

async def remove_digit(password):
    await asyncio.sleep(0.01)
    result = ""
    i = 0

    while i <len(password):
        if not password[i].isdigit():
            result +=password[i]
        i += 1
    print(f"Answer for Question 1:{result}")

asyncio.run(remove_digit("Pa55ss"))

# Question 2

async def first_10(text:str):
    await asyncio.sleep(0.01)
    result = ""
    i = 0
    while i < 10 and i <len(text):
        result += text[i]
        i += 1
    print(f"Answer for Question 2:{result}")
asyncio.run(first_10("Salom Python"))

# Question 3

async def clear_name(name:str):
    await asyncio.sleep(0.01)
    result = ""
    i = 0

    while i <len(name):
        if not name[i].isdigit():
            result +=name[i]
        i += 1
    print(f"Answer for Question 3:{result}")
asyncio.run(clear_name("Anna123"))

# Question 4
async def lower_text(text:str):
    await asyncio.sleep(0.01)
    i = 0
    result = ""
    while i < len(text):
        if text[i].isupper():
            result += text[i].lower()
        else:
            result +=text[i]
        i += 1
    print(f"Answer for Question 4:{result}")
asyncio.run(lower_text("SALOM PYTHON"))

# Question 5

async def print_vowels(text: str):
    await asyncio.sleep(0.01)
    result = ""
    vowels = "aeiouAEIOU"
    i = 0
    while i < len(text):
        if text[i] in vowels:
            result +=text[i]
        i += 1
    print(f"Answer for Question 5:{result}")
asyncio.run(print_vowels("description"))

# Question 6
async def a_and_b(text:str):
    await asyncio.sleep(0.01)
    i = 0
    result = ""
    while i <len(text):
        if i +1 <len(text) and text[i].lower() =="a" and text[i+1].lower() =="b":
            result += "#"
            i+=2
        else:
            result +=text[i]
            i+=1
    print(f"Answer for Question 6:{result}")
asyncio.run(a_and_b("Abba"))

# Question 7

async def reversed_digits(text:str):
    await asyncio.sleep(0.01)
    i = len(text) - 1
    result = ""
    while i >= 0:
        if text[i].isdigit():
            result +=text[i]
        i -= 1
    print(f"Answer for Question 7:{result}")
asyncio.run(reversed_digits("Anna12345"))

# Question 8

async def remove_middle(word: str):
    await asyncio.sleep(0.01)
    result = ""
    i = 0
    middle = len(word) // 2
    while i < len(word):
        if i != middle:
            result += word[i]
        i += 1
    print(f"Answer for Question 8:{result}")

asyncio.run(remove_middle("salom"))

# Question 9
async def lower_with_a(text:str):
    await asyncio.sleep(0.01)
    words = text.split()
    result = []
    i = 0
    while i < len(words):
        word = words[i]
        if word.endswith("a") or word.endswith("A"):
            result.append(word.lower())
        else:
            result.append(word)
        i +=1
    print(f"Answer for Question 9:{' '.join(result)}")
asyncio.run(lower_with_a("Aziza"))

# Question 10

async def remove_repeat(text:str):
    await asyncio.sleep(0.01)
    seen = ""
    result = ""
    i = 0
    while i < len(text):
        if text[i] not in seen:
            result +=text[i]
            seen += text[i]
        i +=1
    print(f"Answer for Question 10:{result}")
asyncio.run(remove_repeat("antonina"))

# Question 11
async def check_only_vowels(word:str):
    await asyncio.sleep(0.01)
    vowels = "aeiouAEIOU"
    only_vowels = True

    for letter in word:
        if letter not in vowels:
            only_vowels = False
            break
    if only_vowels:
        print(f"Answer for Question 11:{word.upper()}")
    else:
        print("The word contains other letters")

asyncio.run(check_only_vowels("AIO"))
