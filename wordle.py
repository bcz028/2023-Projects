def wordle(word):
    guess=input("What word do you think it is?")
    count=0
    if len(guess)!=len(word):
        return "Guess is not the correct length"
    word_freq={}
    possible_repeats=[]
    final_progress=""
    correct_placement=[]
    wrong_placement=[]
    wrong_letter=[]
    for letter in word:
        if letter not in word_freq:
            word_freq[letter]=1
        else:
            word_freq[letter]+=1
    for index in range(len(guess)):
        if guess[index]==word[index]:
            word_freq[guess[index]]-=1
            count+=1
            final_progress+=str(guess[index]) + " "
            correct_placement+=[str(guess[index])]
        elif guess[index] in word_freq and word_freq[guess[index]]>0:
            possible_repeats+=[guess[index]]
            final_progress+="_ "
            wrong_placement+=[str(guess[index])]
        else:
            final_progress+="_ "
            if guess[index] not in guess[:index]:#accounts for repeated letters not in word
                wrong_letter+=[str(guess[index])]
    if count==5:
        print(word + " " + "is correct: You win!")
        return
    print("Letters in the correct place:")
    for message in correct_placement:
        print(message)
    if len(correct_placement)==0:
        print("None")
    print("\nProgress:")
    print(final_progress)
    print("\nLetters in the word, but wrong place:")
    for message in wrong_placement:
        print(message)
    if len(wrong_placement)==0:
        print("None")
    print("\nThese letters are not in the word:")
    for message in wrong_letter:
        print(message)
    if len(wrong_letter)==0:
        print("None")
    return wordle(word)


word=input("What is the secret word?")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nDo not scroll above this")
wordle(word)



