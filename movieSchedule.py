# Using Dictionaries

current_movies = {'Toy Story': '2:00PM',
                  'Shrek 3': '3:15PM',
                  'Maleficient': '4:00PM',
                  'Rango': '5:45PM'}

print('Our Current Selection:')
for title in current_movies:
    print(title)

movie = input('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie)

if showtime:
    print(movie, 'is playing at', showtime)
else:
    print("No showtimes for", movie)