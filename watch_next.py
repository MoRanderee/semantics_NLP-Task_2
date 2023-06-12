import spacy  # importing spacy
nlp = spacy.load('en_core_web_md') # specifying the model we want to use. Remember to install this model by typing python -m spacy download en_core_web_md into your command line

def watch_next(movie):

    with open('movies.txt', 'r') as f:
        descriptions = f.readlines()
    
    token_1 = nlp(movie)
    sim_list = []

    for item in descriptions:
        token_2 = nlp(item[9::])
        
        sim_list.append(token_1.similarity(token_2))

    max_sim = max(sim_list)
    movie = descriptions[sim_list.index(max_sim)][0:9]
    print(movie, max_sim)


Planet_Hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

watch_next(Planet_Hulk)

