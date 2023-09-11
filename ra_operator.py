
#########################################################
###  Implementing Relational Algebra Operators        ###
#########################################################


# Implement an operator to merge two lists with duplicated allowed
def union(lst1, lst2):
    """Relational algebra project set union
    """ 
     ## IMPLEMENT HERE THE UNION OF TWO LISTS

    return 

# mplement an operator to merge two lists with no duplicated allowed
def union2(lst1, lst2):
    """Relational algebra project set union with no duplicates
    """ 
    ###IMPLEMENT HERE THE INTERSECTION OF TWO LISTS
    return 

# Implement an operator to perform the intersection of two lists
def intersection(lst1, lst2):
    """Relational algebra project set intersection
    """ 
    ###IMPLEMENT HERE THE INTERSECTION OF TWO LISTS
    return 


# Implement an operator to perform the set difference of two lists
def set_difference(lst1, lst2):
    """Relational algebra project set difference
    """ 
    ## IMPLEMENT HERE THE SET DIFFERENT BETWEEN TWO LISTS
    return 

## RA SELECTIOn

def selection(relation, column, predicate, mode):
    """Relational algebra project selection
    """ 
    ## IMPLEMENT HERE THE SELECTION OPERATOR valid modes are ['<', '<=', '>', '>=', '==', '!=']
    return 

#RA PROJECTION

def project(relation, columns):
    """Relational algebra project operator
    
       relation: list of rows
       columns: list with columns index
    """
    # IMPLEMENT HERE THE PROJECT OPERATOR. THE FUNCTION CCEPTS A LIST OF COLUMNS INDEXES AND RETURN THE VALUES OF THOSE COLUMNS 
    
    return 

## CROSS PRODUCT
# The cross product pairs each row of a relation with every row of another relation to create 
# a new relation that contains every possible combination of the input relations tuples.

def crossproduct(relation_a, relation_b):
    """Relational algebra cross product operator
    """
    ## IMPLEMENT CROSS PRODUCT HERE
    return 