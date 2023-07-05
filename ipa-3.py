#!/usr/bin/env python
# coding: utf-8

# In[3]:


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
                    return "follower"   

            else:
                if from_member in z:
                    return "followed by"
                else:
                    return "no relationship"
        else:
            w = social_graph[from_member]
            x = w['following']
            if to_member in x:
                    return "follower"
            else:
                return "no relationship"
            
    else:
               
        if to_member in social_graph:
            y = social_graph[to_member]
            z = y['following']
            
            if from_member in z:
                return "followed by"
            else:
                return "no relationship"
        
        else:
            return "no relationship"  


# In[158]:


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
        
        #doing this the hard way :"D
        if len(board) == 3:
            x = board[0][0] + board[1][1] + board [2][2] 
            y = board[0][2] + board[1][1] + board [2][0]
            if x.find("XXX") != -1:
                return "X"
            elif y.find("XXX") != -1:
                return "X"
        
        if len(board) == 4:
            x = board[0][0] + board[1][1] + board [2][2] + board[3][3] 
            y = board[0][3] + board[1][2] + board [2][1] + board[3][0]
            upper_y = board[0][2] + board[1][1] + board[2][0]
            lower_y = board[1][3] + board[2][2] + board[3][1]
            upper_x = board[0][1] + board[1][2] + board[2][3]
            lower_x = board[1][0] + board[2][1] + board[3][2]
            if x.find("XXX") != -1:
                return "X"
            if upper_x.find("XXX")!= -1:
                return "X"
            if lower_x.find("XXX")!= -1:
                return "X"
            
            if y.find("XXX") != -1:
                return "X"
            if upper_y.find("XXX")!= -1:
                return "X"
            if lower_y.find("XXX")!= -1:
                return "X"
            
            if x.find("OOO") != -1:
                return "O"
            if upper_x.find("OOO")!= -1:
                return "O"
            if lower_x.find("OOO")!= -1:
                return "O"
            
            if y.find("OOO") != -1:
                return "O"
            if upper_y.find("OOO")!= -1:
                return "O"
            if lower_y.find("OOO")!= -1:
                return "O"
            
            
        if len(board) == 5:
            x = board[0][0] + board[1][1] + board[2][2] + board[3][3] + board[4][4]
            y = board[0][4] + board[1][3] + board[2][2] + board[3][1] + board[4][0]
            
            upper_y = board[0][2] + board[1][1] + board[2][0]
            second_upper_y = board[0][3] + board[1][2] + board[2][1] + board[3][0]
            
            lower_y = board[2][4] + board[3][3] + board[4][2]
            second_lower_y = board[1][4] + board[2][3] + board[3][2] + board[4][1]
            
            upper_x = board[0][2] + board[1][3] + board[2][4]
            second_upper_x = board[0][1] + board[1][2] + board[2][3] + board[3][4]
            
            lower_x = board[2][0] + board[3][1] + board[4][2]
            second_lower_x = board[1][0] + board[2][1] + board[3][2] + board[4][3]
            
            if x.find("XXX") != -1:
                return "X"
            if upper_x.find("XXX")!= -1:
                return "X"
            if lower_x.find("XXX")!= -1:
                return "X"
            if second_lower_x.find("XXX")!= -1:
                return "X"
            
            if y.find("XXX") != -1:
                return "X"
            if upper_y.find("XXX")!= -1:
                return "X"
            if second_upper_y.find("XXX")!= -1:
                return "X"
            if lower_y.find("XXX")!= -1:
                return "X"
            if second_lower_y.find("XXX")!= -1:
                return "X"
            
            if x.find("OOO") != -1:
                return "O"
            if upper_x.find("OOO")!= -1:
                return "O"
            if second_upper_x.find("OOO")!= -1:
                return "O"
            if lower_x.find("OOO")!= -1:
                return "O"
            if second_lower_x.find("OOO")!= -1:
                return "O"
            
            if y.find("OOO") != -1:
                return "O"
            if upper_y.find("OOO")!= -1:
                return "O"
            if second_upper_y.find("OOO")!= -1:
                return "O"
            if lower_y.find("OOO")!= -1:
                return "O"
            if second_lower_y.find("OOO")!= -1:
                return "O"
            
        if len(board) == 6:
            x = board[0][0] + board[1][1] + board[2][2] + board[3][3] + board[4][4] + board[5][5]
            y = board[0][5] + board[1][4] + board[2][3] + board[3][2] + board[4][1] + board[5][0]

            upper_y = board[0][3] + board[1][2] + board[2][1] + board[3][2] + board[4][3] + board[5][4]
            second_upper_y = board[0][4] + board[1][3] + board[2][2] + board[3][1] + board[4][2] + board[5][3]
            third_upper_y = board[0][2] + board[1][1] + board[2][0]

            lower_y = board[2][5] + board[3][4] + board[4][3] + board[5][2]
            second_lower_y = board[1][5] + board[2][4] + board[3][3] + board[4][2] + board[5][1]
            third_lower_y = board[3][5] + board[4][4] + board[5][3]

            upper_x = board[0][2] + board[1][3] + board[2][4] + board[3][5]
            second_upper_x = board[0][1] + board[1][2] + board[2][3] + board[3][4] + board[4][5]
            third_upper_x = board[0][3] + board[1][4] + board[2][5]

            lower_x = board[2][0] + board[3][1] + board[4][2] + board[5][3]
            second_lower_x = board[1][0] + board[2][1] + board[3][2] + board[4][3] + board[5][4]
            third_lower_x = board[3][0] + board[4][1] + board[5][2]
            
            if x.find("XXX") != -1:
                return "X"
            if upper_x.find("XXX")!= -1:
                return "X"
            if second_upper_x.find("XXX")!= -1:
                return "X"
            if third_upper_x.find("XXX")!= -1:
                return "X"
            if lower_x.find("XXX")!= -1:
                return "X"
            if second_lower_x.find("XXX")!= -1:
                return "X"
            if third_lower_x.find("XXX")!= -1:
                return "X"
            
            if y.find("XXX") != -1:
                return "X"
            if upper_y.find("XXX")!= -1:
                return "X"
            if second_upper_y.find("XXX")!= -1:
                return "X"
            if third_upper_y.find("XXX")!= -1:
                return "X"
            if lower_y.find("XXX")!= -1:
                return "X"
            if second_lower_y.find("XXX")!= -1:
                return "X"
            if third_lower_y.find("XXX")!= -1:
                return "X"
            
            if x.find("OOO") != -1:
                return "O"
            if upper_x.find("OOO")!= -1:
                return "O"
            if second_upper_x.find("OOO")!= -1:
                return "O"
            if third_upper_x.find("OOO")!= -1:
                return "O"
            if lower_x.find("OOO")!= -1:
                return "O"
            if second_lower_x.find("OOO")!= -1:
                return "O"
            if third_lower_x.find("OOO")!= -1:
                return "O"
            
            if y.find("OOO") != -1:
                return "O"
            if upper_y.find("OOO")!= -1:
                return "O"
            if second_upper_y.find("OOO")!= -1:
                return "O"
            if third_upper_y.find("OOO")!= -1:
                return "O"
            if lower_y.find("OOO")!= -1:
                return "O"
            if second_lower_y.find("OOO")!= -1:
                return "O"
            if third_lower_y.find("OOO")!= -1:
                return "O"

    return "NO WINNER"   


# In[164]:


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
    
    if first_stop == second_stop:
        return 0

    else:
        time = 0
        current_stop = first_stop

        while True:
            if (current_stop, second_stop) in route_map:
                time += route_map[(current_stop, second_stop)]["travel_time_mins"]
                break

            next_stops = [key[1] for key in route_map.keys() if key[0] == current_stop]
            if len(next_stops) > 0:
                next_stop = next_stops[0]
                time += route_map[(current_stop, next_stop)]["travel_time_mins"]
                current_stop = next_stop

        return time


# In[ ]:




