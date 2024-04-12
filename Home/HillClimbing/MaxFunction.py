import random

def objective_function(x):
    return x**2

def hill_climbing(starting_point,step_size,max_iteration):
    current_point=starting_point
    current_value=objective_function(current_point)

    for i in range(max_iteration):
        neighbour_point=current_point+step_size*(random.random()*2-1)
        neighbour_value=objective_function(neighbour_point)
        if(neighbour_value>current_value):
            current_point=neighbour_point
            current_value=neighbour_value
        
    
    return current_point, current_value

result=hill_climbing(8,0.00001,60000)
print(result)