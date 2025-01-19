import random, streamlit as st


def sortfile(fliee):            # makes a list form the text files
    
    content = []
    for i in open(fliee, encoding = "ISO-8859-1"):
        i = i.replace('\n', '')
        try:

            for i2 in content: # removes duplicate items
                if i == i2:
                    print(i, ' was repeated in ', fliee)
                    print (0/0)

            content.append(str(i)) # adds non repeated items to the list
        except:
            i = ''

    content.sort()   # sorts the list
    scores.close()
    
    return content

def getcard(types):

    games1 = types[0][random.randint(0, len(types[0]) - 2)]    # gets a random item from the lists
    school1 = types[2][random.randint(0, len(types[2]) - 2)]   # i dont care that i could ahve done it with a for loop and a list
    people1 = types[3][random.randint(0, len(types[3]) - 2)]
    shows1 = types[4][random.randint(0, len(types[4]) - 2)]

    temp = [games1, school1, people1, shows1]

    while True:   # gets an item for the misc list and makes shore that it is not on the card 
        count = 0
        misc2 = types[1][random.randint(0, len(types[1]) -1)]
        for i in temp:
            if misc2 == i:
                count += 1
        
        if count < 1:
            break

    card = [                                      # makes the card in a 2d array
        f'games                 :   {games1}',
        f'misc                  :   {misc2}',
        f'school                :   {school1}',
        f'people + characters   :   {people1}',
        f'shows + tv            :   {shows1}'
    ]

    return card


games = sortfile('gaming.txt')          # gets all the files onto lists
misc1 = sortfile('misc.txt')
school = sortfile('school.txt')
people = sortfile('people and characters.txt')
shows = sortfile('shows + tv.txt')

misc = misc1 + school + people + shows    # puts all the values in misc list


misc = list(dict.fromkeys(misc))    # removes the duplicate items form misc


types = [games, misc, school, people, shows] # makes a 2d array with all the lists on it

# generates the card
card = getcard(types)

cardReload = st.button('new card')

for i in card:
    st.subheader(f'{i}', divider=True)


