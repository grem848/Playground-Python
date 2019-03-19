import webget2
import random


surnames_txt = 'http://www2.census.gov/topics/genealogy/1990surnames/dist.all.last'
female_names_txt = 'http://www2.census.gov/topics/genealogy/1990surnames/dist.female.first'
male_names_txt = 'http://www2.census.gov/topics/genealogy/1990surnames/dist.male.first'

webget2.download(surnames_txt, to='./last_names.txt')
webget2.download(female_names_txt, to='./female_names.txt')
webget2.download(male_names_txt, to='./male_names.txt')

# %%bash
# ls -ltr *names.txt

def get_names_from(file):
    with open(file, 'r') as fp:
        return [x.split()[0] for x in fp]

names = get_names_from('./last_names.txt')
female_names = get_names_from('./female_names.txt')
male_names = get_names_from('./male_names.txt')
print(len(names), len(female_names), len(male_names))




def random_combination(list_a, list_b):
    # return list_a[random.randint(0, len(list_a))] + ' ' + list_b[random.randint(0, len(list_b))]
    return random.choice(list_a) + ' ' + random.choice(list_b)
print(random_combination(female_names, names))


def generate_random_names(amount=1, gender='female'):
    random_names = []
    for i in range(amount):
        if gender == 'female':
            name = random_combination(female_names, names)
        elif gender == 'male':
            name = random_combination(male_names, names)
        else:
            name = random_combination(female_names + male_names, names)
        random_names.append(name)
    return random_names
    
print(generate_random_names(10, 'female'))
