# the front of the spaceship shape will always be the vertex1
# spaceship shape 1
def shape1(center_x, center_y):

    vertex1 = [center_x, center_y + 10]
    vertex2 = [center_x - 5, center_y - 10]
    vertex3 = [center_x + 5, center_y - 10]
    return [vertex1, vertex2, vertex3]

# spaceship shape 2
def shape2(center_x, center_y):
    vertex1 = [center_x, center_y + 10]
    vertex2 = [center_x + 1, center_y + 4]
    vertex3 = [center_x + 6, center_y + 2]
    vertex4 = [center_x + 6, center_y + 6]
    vertex5 = [center_x + 10, center_y]
    vertex6 = [center_x + 6, center_y - 6]
    vertex7 = [center_x + 6, center_y - 4]
    vertex8 = [center_x + 4, center_y - 4]
    vertex9 = [center_x, center_y - 6]
    vertex10 = [center_x - 4, center_y - 4]
    vertex11 = [center_x - 6, center_y - 4]
    vertex12 = [center_x - 6, center_y - 6]
    vertex13 = [center_x - 10, center_y]
    vertex14 = [center_x - 6, center_y + 6]
    vertex15 = [center_x - 6, center_y + 2]
    vertex16 = [center_x - 1, center_y + 4]
    return [vertex1, vertex2, vertex3, vertex4, vertex5, vertex6, vertex7, vertex8, vertex9, vertex10, vertex11, vertex12, vertex13, vertex14, vertex15, vertex16]

# spaceship shape 3
#def shape3(center_x, center_y):


# stars shape
def star_shape(center_x, center_y):
    vertex1 = [center_x, center_y + 5]
    vertex2 = [center_x + 2, center_y + 2]
    vertex3 = [center_x + 5, center_y]
    vertex4 = [center_x + 2, center_y - 2]
    vertex5 = [center_x, center_y - 5]
    vertex6 = [center_x - 2, center_y - 2]
    vertex7 = [center_x - 5, center_y]
    vertex8 = [center_x - 2, center_y + 2]
    return [vertex1, vertex2, vertex3, vertex4, vertex5, vertex6, vertex7, vertex8]