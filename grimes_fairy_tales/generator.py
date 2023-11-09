import random
possible_characters = ["Bear", "Lion", "Cat", "Dog", "Horse", "Mouse", "Rabbit"]

# Character Listing

villain = None
princess = None
hero = None

# Defining Characters

def characterChoosing(eligible_characters):
    chosen = random.choice(eligible_characters)
    eligible_characters.remove(chosen)
    return chosen

villain = characterChoosing(possible_characters)
princess = characterChoosing(possible_characters)
hero = characterChoosing(possible_characters)

# Story Elements (based on Propp)

preparation = 0
complication = 4
transference = 5
struggle = 7
recognition = 11


sentences = [f"A {hero} has been in trouble for a long time. ",
             f"A {villain} steals something that belongs to the {hero}. ",
             f"A {villain} hurts the {princess}. ",
             f"A {villain} kidnaps the {princess}. ",
             f"A {hero} hears about a {villain}'s crimes. ",
             f"The hero, {hero}, leaves home to go help. ",
             f"The hero, {hero}, kills the villain, {villain}, without a fight. ",
             f"The hero, {hero}, fights the villain, {villain}, and wins. ",
             f"The hero, {hero}, thus is able to get his possession back. ",
             f"The hero, {hero}, thus is able to get revenge for the princess, {princess}. ",
             f"The hero, {hero}, thus is able to rescue the princess, {princess}. ",
             f"The hero, {hero}, thus is able to bring the villain, {villain}, to justice. "]
section_boundaries = {"preparation":preparation,
                      "complication": complication,
                      "transference": transference,
                      "struggle": struggle,
                      "recognition": recognition} # gives indices of sentences at which we move to a different "domain"
topicless_sentences = [0,5,6,7] # sentences which do not rely on a specific topic
topics = [[1,8], [2,9], [3,10], [4,11]] # list of lists for related topics

story = ""
eligible_sentences = [0,1,2,3,4]
current_choice_index = 0
all_choice_indices = []
story_complete = False

def generateStory(eligible_sentences):
    completion = False
    current_choice_index = random.choice(eligible_sentences) # choosing sentence for this step
    all_choice_indices.append(current_choice_index)
    output = sentences[current_choice_index]
    eligible_sentences = []

    # generating possible next steps 

    for sentence in topicless_sentences:
        if sentence > current_choice_index:
            eligible_sentences.append(sentence)

    for topic in topics:
        for choice_index in all_choice_indices: # ensures consistency of topic
            if choice_index in topic:
                for sentence in topic:
                    if sentence > current_choice_index:
                        eligible_sentences.append(sentence)
                break
    

    if max(all_choice_indices) <= transference: # forces there to be a "struggle" element
        for i in range(struggle+1,len(sentences)+1):
            if i in eligible_sentences: eligible_sentences.remove(i)
    elif max(all_choice_indices) <= struggle: # only allows for one "struggle" element
         for i in range(transference,struggle+1):
            if i in eligible_sentences: eligible_sentences.remove(i)

    if eligible_sentences == []: # if no more sentences are possible, ends story
        completion = True 
    return (output, eligible_sentences, completion)

while not story_complete:
    generator_output = generateStory(eligible_sentences)
    story += generator_output[0]
    eligible_sentences = generator_output[1]
    story_complete = generator_output[2]

print(story)


                



