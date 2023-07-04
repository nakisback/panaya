import random, display

SUBJECTS = {'article': ['a ', 'an ', 'the ', ''],
            'animal': ['dog', 'cat', 'bird','iguana', 'panda', 'shark', 'rabbit', 'fish', 'monkey', 'snake', 'elephant', 'buffalo', 'cayman']}

ADJECTIVES = {'color': ['red','orange','yellow','green','blue','purple','black','white','pink'],
              'size': ['big', 'huge', 'large', 'little', 'small','short']}

PREDICATES = {'verb': ['run','climb', 'jump','slither', 'play', 'eat', 'bark', 'meow', 'dance','drink','listen','wait','sleep','smell', 'smile', 'walk', 'jog','swim']}

THAI_NAMES = {}

def main():
    #print(SUBJECTS)
    
    sentences = []
    #response = int(input('How many sentences? '))

    '''for i in range(response):
        sentence = generateSentence()
        sentences.append(sentence)'''

    sentence, subject = generateSentence()

    display.displayString(sentence)
    print("Complete Subject:  ", end='')
    input()
    print('   ' + subject.capitalize())

    #print(sentence)
    #print(sentence)

def generateSentence():
    subject = generateSubject()
    predicate = generatePredicate(subject)
    sentence = subject + ' ' + predicate
    sentence = fixGrammar(sentence)

    
    return sentence, subject

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
    predicate = random.choice(PREDICATES['verb'])
    if subject.endswith('s') == False and subject != 'fish':
        predicate += 's'

    return predicate

def fixGrammar(sentence):

    sentence = sentence.capitalize()
    sentence += '.'

    return sentence
    
if __name__ == "__main__":
    main()