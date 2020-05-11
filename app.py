import random, csv, math
from os import path

# This is the code we use to read the files from the system
def get_file_content(file_name):
    if path.exists("data/"+file_name) is False:
        print("File data/"+file_name+" does not exist")
        return []
    else:
        file = open("./data/"+file_name, "r") 
        file_content = csv.reader(file)
        aux = []
        for row in file_content:
            aux = aux + row
        print("Found following items: "+str(aux))
        return aux

# we re-use the function get_file_content to get all the file sources
articles = get_file_content('article.csv')
adj = get_file_content('adjectives.csv')
noun = get_file_content('noun.csv')
action = get_file_content('action.csv')
possetion = get_file_content('possetion.csv')
where = get_file_content('where.csv')

# if no file is empty
if len(articles) > 0 and len(adj) > 0 and len(noun) > 0  and len(action) > 0  and len(possetion) > 0 and len(where) > 0:
    # get a random word from the list we got from each file
    rdm0 = int(math.floor(random.randint(1, len(articles))))
    rdm1 = int(math.floor(random.randint(1, len(adj))))
    rdm2 = int(math.floor(random.randint(1, len(noun))))
    rdm3 = int(math.floor(random.randint(1, len(action))))
    rdm4 = int(math.floor(random.randint(1, len(possetion))))
    rdm5 = int(math.floor(random.randint(1, len(where))))

    print("")
    print("This is the generated excuse: \n ")
    print("\x1b[6;30;42m → "+"Es tan grande que duele pero quiero más"+ "\x1b[0m\n\n")
    print("https://www.google.com/search?q=joda+frases&oq=joda+frases&aqs=chrome..69i57.2444j0j4&sourceid=chrome&ie=UTF-8")
    print("YODA: El miedo es el camino hacia el Lado Oscuro; el miedo lleva a la ira, la ira lleva al odio, el odio lleva al sufrimiento")
else:
    # we can't continue, throw error to the user
    print("Missing some data from the files")