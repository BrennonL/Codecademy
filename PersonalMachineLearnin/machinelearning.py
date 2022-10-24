'''
Brennon Laney
Machine learning project
10/17/22
'''
import matplotlib.pyplot as plt
from statistics import mean


def main():
    # These are lists that I will sort my data into
    ages = []
    restingHBs  = []
    male_or_females = []
    has_heartdiseases = []

    # These lists are for the number of times restingHB, male_or_females, or age has a coorisponding heart disease 
    restingHB_hasHD = []
    restingHB_types = []
    restingHB_count = []



    # Here I am opening the heart.csv file and iterating through each line except the first one
    with open('PersonalMachineLearnin/heart.csv') as heart_file:
        i = 0
        for line in heart_file:
            if i > 0:

                new_line = line.split(',')

                # Here I am adding all my datat to a list  
                ages.append(int(new_line[0].strip()))
                restingHBs.append(int(new_line[3].strip()))
                male_or_females.append(new_line[1].strip())

                # Here I am adding all the yes or no to my has_heartdisease list
                has_heartdiseases.append(new_line[11].strip())


            i = i + 1
        

        for i in range(len(has_heartdiseases) - 1):
            if has_heartdiseases[i] == "1":
                restingHB_hasHD.append(restingHBs[i])

        for restingHB in restingHB_hasHD:
            count_restingHB = restingHB_hasHD.count(restingHB)
            restingHB_types.append(restingHB)
            restingHB_count.append(count_restingHB)
            for i in range(count_restingHB):
                restingHB_hasHD.remove(restingHB)


        # print statements for testing purposes
        print(restingHB_types)
        print(restingHB_count)

        m = find_best_fit_m(restingHB_types, restingHB_count)
        b = find_best_fit_b(restingHB_types, restingHB_count, m)

        # Getting all of the y values for the coorisponding x points using the slope and intercept. 
        y = [m * x + b for x in restingHB_types]

        # Print statements for testing purposes
        print(m)
        print(b)
        print(y)
        print(restingHB_count)
        print(restingHB_types)

        graph_points(restingHB_types, restingHB_count, y)



def graph_points(x, y, y_for_best_fit):
    '''
    Inpurts: x points, y points, and the y_for_best_fit, which are all the points to the best fit line
    Takes the points and graphs them. Creates a graph where the x coordinates are 90-210 and the y are 0-100
    Returns: Nothing
    '''
    plt.scatter(x, y)
    plt.plot(x, y_for_best_fit)
    plt.xlim(90, 210)
    plt.ylim(0, 100)

    plt.show()


def find_best_fit_m(xs, ys):
    '''
    Inputs: xs (list), ys (list)
    This takes the xs list and the ys (the x and y coordinates for the diferent points on the graph)
    list and it calculates the best slope for the data. 
    Returns: m (float)
    '''
    print(mean(ys))
    print(mean(xs))
    multiplied_lists = multiply_lists(xs, ys)
    squared_lists = square_lists(xs)
    m = ((mean(xs) * mean(ys)) - mean(multiplied_lists)) / ((mean(xs) ** 2) - mean(squared_lists))
    return m

def find_best_fit_b(xs, ys, m):
    '''
    Inputs: xs (list), ys (list), m (float)
    This uses the xs and ys lists and uses the sloap to find the y intecept of the best fit line
    Returns: b (float)
    '''
    b = mean(ys) - m * mean(xs)
    return b

def multiply_lists(first, second):
    '''
    Inputs: first (list), second (list)
    This will take the two lists and multiply each coorisponding index number to eachother and then
    it will add those new values to new_list which it will return.
    Returns: new_list (list)
    '''
    new_list = []
    for i in range(len(first)):
        new_list.append(first[i] * second[i])

    return new_list

def square_lists(list):
    '''
    Inputs: list (list)
    This will take list (list) and it will square each value and add it to new_list (list) which it will return
    Returns: new_list (list)
    '''
    new_list = []
    for i in range(len(list)):
        new_list.append(list[i] ** 2)
    return new_list


if __name__ == '__main__':
    main()