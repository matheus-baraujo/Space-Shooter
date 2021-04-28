# the front of the spaceship shape will always be the vertex1
# spaceship shape 1
def shape1(center_x, center_y):

    vertex1 = [center_x, center_y + 15]
    vertex2 = [center_x - 10, center_y - 15]
    vertex3 = [center_x + 10, center_y - 15]
    return [vertex1, vertex2, vertex3]

# spaceship shape 2
def shape2(center_x, center_y):

    vertex1 = [center_x, center_y+5]
    vertex2 = [center_x-5, center_y+5]
    vertex3 = [center_x-5, center_y+10]
    vertex4 = [center_x-15, center_y+10]
    vertex5 = [center_x-15, center_y-10]
    vertex6 = [center_x-5, center_y-10]
    vertex7 = [center_x-5, center_y-5]
    vertex8 = [center_x+5, center_y-5]
    vertex9 = [center_x+5, center_y-10]
    vertex10 = [center_x+15, center_y-10]
    vertex11 = [center_x+15, center_y+10]
    vertex12 = [center_x+5, center_y+10]
    vertex13 = [center_x+5, center_y+5]
    return [vertex1, vertex2, vertex3, vertex4, vertex5, vertex6, vertex7, vertex8, vertex9, vertex10, vertex11, vertex12, vertex13]

def shape3(center_x, center_y):

    vertex1 = [center_x, center_y+15]
    vertex2 = [center_x+10, center_y+7.5]
    vertex3 = [center_x, center_y]
    vertex4 = [center_x+10, center_y-15]
    vertex5 = [center_x-10, center_y-15]
    vertex6 = [center_x, center_y]
    vertex7 = [center_x-10, center_y+7.5]
    return [vertex1, vertex2, vertex3, vertex4, vertex5, vertex6, vertex7]
