import ra_operator as RA;
import os
import csv
import test_operators

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


    #Test cases:
    test_operators.test_union_0()
    test_operators.test_union_1()
    test_operators.test_union2_0()
    test_operators.test_union2_1()
    test_operators.test_union2_2()
    test_operators.test_intersection_0()
    test_operators.test_intersection_1()
    test_operators.test_intersection_2()
    test_operators.test_set_diff_0()
    test_operators.test_set_diff_1()
    test_operators.test_set_diff_2()
    test_operators.test_selection_0()
    test_operators.test_project_0()
    test_operators.test_project_1()
    test_operators.test_project_2()

    # 1- Perform the union between the actors and extra_actors relation
    # This operation should returns all of the rows of actor and extra_actors unioned in to a single list. 

    ##ADD YOUR CODE HERE
    unioned_list = RA.union(actors, extra_actors)
    print(unioned_list)

    # 2- Show all tuples from actors that first name is Chris
    
    ##ADD YOUR CODE HERE
    chris_list = RA.selection(actors, 1, "Chris", "==")
    print(chris_list)

    # 3 - Show all tuples from movies that were made after 1998 
    
    ##ADD YOUR CODE HERE
    movies_list_1998 = RA.selection(movies, 2, "1998", ">")
    print(movies_list_1998)

    # 4 - Show all tuples from actors that are female AND id is bigger than 200000
    
    ##ADD YOUR CODE HERE
    female_actors = RA.intersection(RA.selection(actors, 3, "F", "=="), RA.selection(actors, 0, "200000", ">"))
    print(female_actors)

    # 5 - Find the last name of all actors named Chris
    
    ##ADD YOUR CODE HERE
    last_name = RA.project(chris_list, [2])
    print(last_name)


    # 6 - Find the names of the movies that were made after 1998 
    
    ##ADD YOUR CODE HERE
    movies_name = RA.project(movies_list_1998, [1])
    print(movies_name)
    
    # 7 - Find the name of actors that are female AND id is bigger than 200000
    
    ##ADD YOUR CODE HERE
    female_actors_names = RA.project(female_actors, [1, 2])
    print(female_actors_names)
    
    # 8 -  Take the cross product of actors and movies
    
    ##ADD YOUR CODE HERE
    actor_movie_cross = RA.crossproduct(actors, movies)
    for row in actor_movie_cross:
        print(row)

    # 8 -  Print the name of actors and the name of movies they have had a role in it.
    ##ADD YOUR CODE HERE
    actor_movie_role_cross = RA.crossproduct(actor_movie_cross, roles)
    for row in actor_movie_role_cross:
        if(row[0]==row[8] and row[4]==row[9]):
           print(row[1]+", "+row[2]+", "+row[5])

main()