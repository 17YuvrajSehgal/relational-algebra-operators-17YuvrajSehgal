
#########################################################
###  Implementing Relational Algebra Operators        ###
#########################################################


# Implement an operator to merge two lists with duplicated allowed
def union(lst1, lst2):
    """Relational algebra project set union
    """ 
     ## IMPLEMENT HERE THE UNION OF TWO LISTS

    return lst1 + lst2

# mplement an operator to merge two lists with no duplicated allowed
def union2(lst1, lst2):
    """Relational algebra project set union with no duplicates
    """ 
    ###IMPLEMENT HERE THE INTERSECTION OF TWO LISTS
    union_list = lst1 + lst2
    unique_actors_set = set()
    unique_actors_list = []

    for actor in union_list:
        actor_tuple = tuple(actor)
        if actor_tuple not in unique_actors_set:
            unique_actors_list.append(actor)
            unique_actors_set.add(actor_tuple)
    return unique_actors_list 

# Implement an operator to perform the intersection of two lists
def intersection(lst1, lst2):
    """Relational algebra project set intersection
    """ 
    ###IMPLEMENT HERE THE INTERSECTION OF TWO LISTS
    set_lst1 = {tuple(inner_list) for inner_list in lst1}
    set_lst2 = {tuple(inner_list) for inner_list in lst2}

    intersection_set = set_lst1.intersection(set_lst2)

    result_list = [list(inner_tuple) for inner_tuple in intersection_set]
    return result_list 


# Implement an operator to perform the set difference of two lists
def set_difference(lst1, lst2):
    """Relational algebra project set difference
    """ 
    ## IMPLEMENT HERE THE SET DIFFERENT BETWEEN TWO LISTS
    set_lst1 = {tuple(inner_list) for inner_list in lst1}
    set_lst2 = {tuple(inner_list) for inner_list in lst2}

    intersection_set = set_lst1.difference(set_lst2)

    result_list = [list(inner_tuple) for inner_tuple in intersection_set]
    return result_list 

## RA SELECTIOn

def selection(relation, column, predicate, mode):
    """Relational algebra project selection
    """ 
    ## IMPLEMENT HERE THE SELECTION OPERATOR valid modes are ['<', '<=', '>', '>=', '==', '!=']
    match mode:
        case '<':
            return_list = []
            for row in relation:
                if row[column] < predicate:
                    return_list.append(row)
            return return_list

        case '<=':
            return_list = []
            for row in relation:
                if row[column] <= predicate:
                    return_list.append(row)
            return return_list

        case '>':
            return_list = []
            for row in relation:
                if row[column] > predicate:
                    return_list.append(row)
            return return_list

        case '>=':
            return_list = []
            for row in relation:
                if row[column] >= predicate:
                    return_list.append(row)
            return return_list

        case '==':
            return_list = []
            for row in relation:
                if row[column] == predicate:
                    return_list.append(row)
            return return_list

        case '!=':
            return_list = []
            for row in relation:
                if row[column] != predicate:
                    return_list.append(row)
            return return_list 

#RA PROJECTION

def project(relation, columns):
    """Relational algebra project operator
    
       relation: list of rows
       columns: list with columns index
    """
    # IMPLEMENT HERE THE PROJECT OPERATOR. THE FUNCTION CCEPTS A LIST OF COLUMNS INDEXES AND RETURN THE VALUES OF THOSE COLUMNS 
    
    return_list = []
    for row in relation:
        rows_list = []
        for i in range(len(columns)):
            rows_list.append(row[columns[i]])
        return_list.append(rows_list)

    return return_list 

## CROSS PRODUCT
# The cross product pairs each row of a relation with every row of another relation to create 
# a new relation that contains every possible combination of the input relations tuples.

def crossproduct(relation_a, relation_b):
    """Relational algebra cross product operator
    """
    ## IMPLEMENT CROSS PRODUCT HERE
    return [a + b for a in relation_a for b in relation_b]
 