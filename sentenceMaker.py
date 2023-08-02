#TODO: (4/7/23): Call random students, assign to sentence
#TODO: Make USED_WORDS list
#TODO: Assign students to sentences

#TODO: Fix "Fish eats."


import random, display, helpers

SUBJECTS = {'article': ['a ', 'an ', 'the ',''],
            'animal': ['alligator', 'ant', 
                       'bird', 'buffalo', 
                       'cat', 'cayman',
                       'dinosaur', 'dog', 'dolphin', 'dragon',
                       'elephant',
                       'flamingo', 'frog',
                       'hedgehog', 'hippo',
                       'iguana',
                       'lion',
                       'monkey',
                       'panda', 'parrot',
                       'rabbit',
                       'sea urchin', 'shark', 'sloth', 'snake', 'squid', 'squirrel',
                       'tiger', 'turtle',
                       'whale']}

ADJECTIVES = {'color': ['red','orange','yellow','green','blue','purple','black','white','pink'],
              'size': ['big', 'huge', 'large', 'little', 'small','short']}

#TODO: Add -y words

PREDICATES = {'verb': ['bark', 
                       'climb', 
                       'dance', 'draw', 'drink', 
                       'eat', 
                       'fight', 
                       'jump', 'jog', 
                       'listen', 
                       'meow', 
                       'play', 
                       'run', 
                       'sit', 'sleep', 'slither', 'smell', 'smile', 'swim', 
                       'think', 
                       'wait', 'walk']}

ADVERBS = {'sound': ['loudly','quietly'],
           'speed': ['quickly', 'slowly']}

THAI_NAMES = {}


def main():
    #print(SUBJECTS)
    
    sentences = []
    #response = int(input('How many sentences? '))

    '''for i in range(response):
        sentence = generateSentence()
        sentences.append(sentence)

    
    for i in range(10):
        sentence, subject = generateSentence()
        print(f"{i+1}. {sentence}")'''
    
    #className = 'G2-5.csv'
    #callQueue = helpers.getCallQueue()

    sentence, subject, predicate = generateSentence()
    #stringBox = [sentence, '', '', 'Complete Predicate:  _____________________']
    stringBox = [sentence, '', 'Complete Subject:  _____________________', 'Complete Predicate:  _____________________']
    display.displaySentence(stringBox)
    input("Press ENTER to see the Complete Subject. . . ")
    stringBox[2] = "Complete Subject:  " + subject
    display.displaySentence(stringBox)
    input("Press ENTER to see the Complete Predicate. . . ")
    stringBox[3] = "Complete Predicate:  " + predicate
    display.displaySentence(stringBox)

    #print(sentence)
    #print(sentence)

def generateSentence():
    subject = generateSubject().capitalize()
    predicate = generatePredicate(subject) + '.'
    sentence = subject + ' ' + predicate

    
    return sentence, subject, predicate

def generateSubject():
    subject = ''
    noun = ''
    plural = False
    if random.random() > 0.5:
        plural = True
    if random.random() > 0.5:
        adjList = random.choice(list(ADJECTIVES.values()))
        adj = random.choice(adjList)
        noun = adj + ' '

    noun += random.choice(SUBJECTS['animal'])
    if plural == True:
        article = random.choice(SUBJECTS['article'][2:])
        if not noun.endswith('fish'):
            noun += 's'
    else:
        if noun[0] in ['a','e','i','o','u']:
            article = 'an '
        else:
            if random.random() > 0.5:
                article = 'a '
            else:
                article = 'the '
    subject = article +  noun
    return subject
    
def generatePredicate(subject):
    adv = ''
    verb = random.choice(PREDICATES['verb'])

    if subject.endswith('s') == False and subject != 'fish':
        verb += 's'

    if random.random() > 0.5:
        advList = random.choice(list(ADVERBS.values()))
        if random.random() > 0.5:
            adv = random.choice(advList) + ' '
            predicate = adv + verb
        else:
            adv = ' ' + random.choice(advList)
            predicate = verb + adv
    else:
        predicate = verb

    return predicate

def fixGrammar(sentence):

    sentence = sentence.capitalize()
    sentence += '.'

    return sentence
    
if __name__ == "__main__":
    main()