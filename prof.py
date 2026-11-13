print("Welcome to prof's office.")
print("I am his assistant.")
print("First you will have to pass my quiz.")
print()

answer = input("Ok, please tell me what action words are called in English\n")

if answer.lower() == "verbs":
    print("Correct, But that was just a warm-up.")
else:
    print("Grrr ... Your chances of meeting the professor are very low.")

print()

word = input("Give me an 8 letter word with at least 3 vowels\n")

if len(word) == 8:
    print("Your word has 8 letters.")

    w = word.lower()
    count_vowels = w.count('a') + w.count('e') + w.count('i') + w.count('o') + w.count('u')

    if count_vowels > 3:
        print("You gave me more than 3 vowels.")
        print("You are wasting my time.")
    elif count_vowels < 3:
        print("You have less than 3 vowels.")
        print("You tried being sneaky but i caught you red-handed.")
    else:
        print("You gave me exactly 3 vowels.")
        print("Not even trying to put extra effort, but fine I accept this word.")
else:
    print("You seem to be struggling even with your brain cells.")
    print("If you check how many words you wrote I can prove that you only have 1 brain cell. Your word does not even have 8 letters.")

print()
# Please forgive me for that one. It was for comedy :)

sentence = input("Ok, now give me a sentence ending with the phrase Wise Assistant (no questions please)\n")

if sentence.endswith("Wise Assistant"):
    print("Have you not learned about punctuations??")
elif sentence.endswith("Wise Assistant."):
    print("You have a good sense of punctuation.")
    len_first = sentence.find(' ')
    if len_first < 7:
        print("The first word in your sentence was too short.")
else:
    print("You will make the professor furious, crazy anything which makes him mental.")

# appointment
print()
print("Ok, pick a time slot to meet the professor. You got 4 options.")
print("A. 8 Mins past midnight.\t\tB. 16 Mins before sunrise.")
print("C. 24 Mins past noon.\t\tD. 48 Mins after sunset.")

appointment = input("Please select your slot (A/B/C/D)\n").upper()

if appointment == "A":
    print("You have selected 8 Mins past midnight.")
    print("Be careful. The professor might be sleeping.")
elif appointment == "B":
    print("Be careful. The professor might be jogging.")
elif appointment == "C":
    print("Beware. The professor might be having his lunch.")
else:
    print("Caution. The professor might be tired after a lot of his appointments.")

print()
print("Good luck for your appointment, bye for now.")
