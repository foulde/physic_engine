from model import *
import glm
from collision_detection import *


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        # skybox
        self.skybox = AdvancedSkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        # floor
        n, s = 20, 2
        for x in range(-n, n, s):
            for z in range(-n, n, s):
                add(Cube(app, pos=(x, -s, z)))

        # columns
        for i in range(5):
            add(Cube(app, pos=(15, i * s, -9 + i), tex_id=2))
            add(Cube(app, pos=(15, i * s, 5 - i), tex_id=2))

        # cat
        # add(Cat(app, pos=(0, -1, -10)))

        # moving cube
        self.moving_cube = MovingCube(app, pos=(0, 6, 8), scale=(3, 3, 3), tex_id=1)
        add(self.moving_cube)

        #cube with speed and acceleration 
        # add(Cube(app, pos=(-5, 2, -50), tex_id=2 , velocity = glm.vec3(1,10,0), acceleration = glm.vec3(0,-9.8,0)))
        add(Cube(app, pos=(-5, 6, -50), tex_id=2 , velocity = glm.vec3(0,2,0), acceleration = glm.vec3(0,-9.8,0)))
        add(Cube(app, pos=(-5, 2, -50), tex_id=2 , velocity = glm.vec3(0,0,0), acceleration = glm.vec3(0,0,0)))
        # add(Cube(app, pos=(-5, 2, -50), tex_id=2 , velocity = glm.vec3(1,10,0), acceleration = glm.vec3(0,-9.8,0)))

    def update(self):

        # self.moving_cube.rot.xyz = self.app.time

        # print(self.objects[-1].pos)

        a = self.objects[-1]
        b= self.objects[-2]
        print(test_aabb_overlap(a,b))
        # collision_detection()
        # print(f'this the time {self.app.time} \nthis is the rot { self.moving_cube.rot.xyz }\n')

        # self.moving_cube.rot.x = self.app.time



    # def update(self):
    #     pass
    #     # self.moving_cube.rot.xyz = self.app.time
    #     # self.moving_cube.rot.xyz = self.app.time