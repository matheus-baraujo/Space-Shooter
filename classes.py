class PlayerObject():


    def __init__(self, width, height):

        initial_vertex1 = [width/2, height/2]
        initial_vertex2 = [width/2 - 10,height/2 + 20]
        initial_vertex3 = [width/2 + 10,height/2 + 20]
        self.vertices = [initial_vertex1, initial_vertex2, initial_vertex3]
        self.life = 5

    def is_dead(self):

        if self.life < 1:

            return False
        
        else:

            return True

    def get_vertices(self):

        return self.vertices

    def update_vertices(self, new_vertices):

        self.vertices = new_vertices