import ra_operator as RA;
import os
import csv

# Data source: https://relational.fit.cvut.cz/dataset/IMDb
# Information courtesy of IMDb (http://www.imdb.com). Used with permission.
# Notice: The data can only be used for personal and non-commercial use and must not
# be altered/republished/resold/repurposed to create any kind of online/offline
# database of movie information (except for individual personal use).


import os

print('basename:    ', os.path.basename(__file__))
print('dirname:     ', os.path.dirname(__file__))


filepath = os.path.dirname(__file__)+ '/data/IMDb_sample'  
print(filepath)

def open_file(filename):
    with open(filename, 'r', newline = '') as f:
        reader = csv.reader(f, delimiter='\t')
        data = list(reader)
        return data[1:]

    
def main():

    # Creating another table with actors for testing purposes
    extra_actors = [['109100', 'Renata', 'Dividino', 'F'], ['481290', 'Burnell', 'Tucker', 'M'], ['10963', 'Chris', 'Anastasio', 'M']]

    # create a list of all files in that directory that end with "*.csv":
    actors = open_file(filepath + '/actors.csv')
    directors_genres = open_file(filepath + '/directors_genres.csv')
    directors = open_file(filepath + '/directors.csv')
    movies_directors = open_file(filepath + '/movies_directors.csv')
    movies_genres = open_file(filepath + '/movies_genres.csv')
    movies = open_file(filepath + '/movies.csv')
    roles = open_file(filepath + '/roles.csv')

    # 1- Perform the union between the actors and extra_actors relation
    # This operation should returns all of the rows of actor and extra_actors unioned in to a single list. 

    ##ADD YOUR CODE HERE

    # 2- Show all tuples from actors that first name is Chris
    
    ##ADD YOUR CODE HERE

    # 3 - Show all tuples from movies that were made after 1998 
    
    ##ADD YOUR CODE HERE

    # 4 - Show all tuples from actors that are female AND id is bigger than 200000
    
    ##ADD YOUR CODE HERE

    # 5 - Find the last name of all actors named Chris
    
    ##ADD YOUR CODE HERE


    # 6 - Find the names of the movies that were made after 1998 
    
    ##ADD YOUR CODE HERE
    
    # 7 - Find the name of actors that are female AND id is bigger than 200000
    
    ##ADD YOUR CODE HERE
    
    # 8 -  Take the cross product of actors and movies
    
    ##ADD YOUR CODE HERE

    # 8 -  Print the name of actors and the name of movies they have had a role in it.
    ##ADD YOUR CODE HERE

main()