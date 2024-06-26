def borders(first_edge, second_edge, point):
    if (point[0] < first_edge[0] or point[0] > second_edge[0] or 
            point[1] > first_edge[1] or point[1] < second_edge[1]):
        print("OUTSIDE")
    elif (point[0] == first_edge[0] or point[0] == second_edge[0] or 
            point[1] == first_edge[1] or point[1] == second_edge[1]):
        print('AT THE EDGE')
    elif (point[0] > first_edge[0] and point[0] < second_edge[0] or 
            point[1] > second_edge[1] and point[1] < first_edge[1]):
        print("INSIDE")