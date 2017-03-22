# Madlib Game in Python
Noun = ["SUPERMAN","SPIDERMAN","BATMAN","LAWYER","LIBRARIAN","PILOT"]
Verb = ["PLAYING","STUDYING","DANCING","LAUGHING"]
Adverb = ["ACCIDENTALLY","HERIOCALLY","EMOTIONALLY","AMUSINGLY"]
Sentence = ["THE &&NOUN IS &&VERB &&ADVERB",
            "THE &&NOUN WAS &&VERB &&ADVERB",
            "LAST NIGHT IN MY DREAM, I SAW MYSELF AS &&NOUN &&VERB &&ADVERB",
            "THE &&NOUN WAS &&VERB &&ADVERB ACROSS THE FLOOR",
            "AFTER EXPOSURE TO SUN, &&NOUN STARTED &&VERB &&ADVERB"]

continue_playing = 'y'
madlib = []
while (continue_playing.lower() in ("y","yes")):
    choice = input(" Please enter a single integer between 0 and 8: ")
    if choice < 0 or not isinstance(choice,int):
        print ("Choice should be positive integer only")
    else:
        if choice == 0:
            sentence_index = choice
            noun_index  = choice
            verb_index  = choice
            adverb_index = choice
        else:
            sentence_index = choice % len(Sentence)
            noun_index  = choice % len(Noun)
            verb_index  = choice % len(Verb)
            adverb_index = choice % len(Adverb)
    
        tmp_sentence = Sentence[sentence_index]
        new_sentence = tmp_sentence.replace("&&NOUN",Noun[noun_index]).replace("&&VERB",Verb[verb_index]).replace("&&ADVERB",Adverb[adverb_index])
        if new_sentence not in madlib:
            madlib.append(new_sentence)
            print new_sentence," has been added in your madlib"
        else:
            print new_sentence," is already present in madlib"
       
        while True:
            continue_playing = raw_input("Enter 'y' to continue playing or 'n' to exit:")
            if continue_playing.lower() not in ("y","yes","n","no"):
                print "Please select appropriate choice"
            else:
                break

print "\n"        
print "Thank you for playing madlib; here are your ", len(madlib), " unique sentences:"
for each_sentence in madlib:
    print each_sentence




