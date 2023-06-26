#!/usr/bin/env python
# coding: utf-8

# In[806]:


def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}
    if from_member in social_graph:
        if to_member in social_graph:
            w = social_graph[from_member]
            x = w['following']

            y = social_graph[to_member]
            z = y['following']

            if to_member in x:
                if from_member in z:
                    return "friends"
                else:
                    return "following"   

            else:
                if from_member in z:
                    return "followed by"
                else:
                    return "no relationship"
        else:
            w = social_graph[from_member]
            x = w['following']
            if to_member in x:
                    return "following"
            else:
                return "no relationship"
            
    else:
        y = social_graph[to_member]
        z = y['following']
        
        if from_member in z:
            return "followed by"
        
        else:
            return "no relationship"      


# In[83]:


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
       
    for i in range(len(board)):
        # Checking rows
        row = ""
        for j in range(len(board[i])):
            mark = board[i][j]
            row += mark

        if row.find("XXX") != -1:
            return "X"

        if row.find("OOO") != -1:
            return "O"
        
        # Checking columns
        column = ""
        for j in range(len(board[i])):
            letter = board[j][i]
            column += letter

        if column.find("XXX") != -1:
            return "X"

        if column.find("OOO") != -1:
            return "O" 
        
    # Checking diagonals
    size = len(board)
       
    diagonal1 = [board[i][i] for i in range(size)]
    if len(set(diagonal1)) == 1 and diagonal1[0] != "":
        return diagonal1[0]

    diagonal2 = [board[i][size - 1 - i] for i in range(size)]
    if len(set(diagonal2)) == 1 and diagonal2[0] != "":
        return diagonal2[0]

    for i in range(1, size):
        diagonal = [board[j][j+i] for j in range(size-i)]
        if len(set(diagonal)) == 1 and diagonal[0] != "":
            return diagonal[0]

    diagonal = [board[j+i][j] for j in range(size-i)]
    if len(set(diagonal)) == 1 and diagonal[0] != "":
        return diagonal[0]
        
    return "NO WINNER"   



# In[356]:


def eta(first_stop, second_stop, route_map):
    
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    stops = list(legs)
    
    if first_stop==second_stop:
        return 0
    else:
    
        for i in range(len(stops)):

            x = list(stops[i])

            

            y = x[0]

            if y == first_stop:
                start = stops[i]
                initial = int(legs[start]["travel_time_mins"])
                if list(start)[1] == second_stop:
                    time = initial
                    
            else: 
                z = x[1]

                if z == second_stop:
                    going = stops[i]
                    current = int(legs[going]["travel_time_mins"])
                    time = initial + current

        return time

