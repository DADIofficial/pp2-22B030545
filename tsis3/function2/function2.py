# Dictionary of movies

movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#task1
def checkmore55(x):
    for i in movies:
        if i['name'] == x and i['imdb'] > 5.5:
            return True
    return False

print(checkmore55(input()))

#task2
def allmore55():
    newmovies = []
    for i in movies:
        if i['imdb'] > 5.5:
            newmovies.append(i);
    return newmovies
print(allmore55())

#task3
def samecategory(x):
    allfilms = []
    for i in movies:
        if i['category'] == x:
            allfilms.append(i['name']);
    return allfilms
print(samecategory(input()))

#task4
def averageball_fromfilms(x):
    averageball = 0
    for i in movies:
        if i['name'] in x:
            averageball += i['imdb'];
    return averageball/len(x)
print(averageball_fromfilms(["Detective", "We Two", "What is the name"]))

#task5
def averageball_fromcategory(x):
    averageball = 0
    for i in movies:
        if i['category'] == x:
            averageball += i['imdb'];
    return averageball
print(averageball_fromcategory(input()))