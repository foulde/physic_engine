from model import *
# from model_backup import *

import glm
# from collision_detection import *
from collision_intersection import *


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

        # # floor
        # n, s = 20, 2
        # for x in range(-n, n, s):
        #     for z in range(-n, n, s):
        #         add(Cube(app, pos=(x, -s, z)))

        # # columns
        # for i in range(5):
        #     add(Cube(app, pos=(15, i * s, -9 + i), tex_id=2))
        #     add(Cube(app, pos=(15, i * s, 5 - i), tex_id=2))

        # cat
        # add(Cat(app, pos=(0, -1, -10)))

        # moving cube
        # self.moving_cube = MovingCube(app, pos=(0, 6, 8), scale=(3, 3, 3), tex_id=1)
        # add(self.moving_cube)

        #cube with speed and acceleration 
        # add(Cube(app, pos=(-5, 6, -50), tex_id=2 , velocity = glm.vec3(0,2,0), acceleration = glm.vec3(0,-9.8,0)))
        # add(Cube(app, pos=(-5, 2, -50), tex_id=2 , velocity = glm.vec3(0,0,0), acceleration = glm.vec3(0,0,0)))
        # add(Cube(app, pos=glm.vec3(-5,-5,-25), scale=(1,1,1),tex_id=2 , id= "cube_ref",enable_extract_triangle=True))
        
        
        
        """
        add(Cube(app, pos=glm.vec3(0,-5,-20), scale=(10,1,10),tex_id=2 , id= "plateforme",enable_extract_triangle=True))

        #cube with rotation
        add(Cube(app, pos=glm.vec3(-5, 8, -20), tex_id=2 , velocity = glm.vec3(0,2,0),rot=(5, 2, 7)
                 , acceleration = glm.vec3(0,-2.8,0) , angular_velocity=(1,1,1),enable_extract_triangle=True, id= "falling_cube"))
        add(Cube(app, pos=glm.vec3(-5, 2, -20), tex_id=2 , velocity = glm.vec3(0,0,0), acceleration = glm.vec3(0,0,0),enable_extract_triangle=True , id= "no gravity cube"))
        """
        


        add(Cube(app, pos=glm.vec3(0,-5,-20), scale=(10,1,10),tex_id=2 ,enable_extract_triangle=True,mass=1000))

        #cube with rotation
        add(Cube(app, pos=glm.vec3(-5, 8, -20), tex_id=1 , velocity = glm.vec3(0,2,0),rot=(5, 2, 7)
                 , acceleration = glm.vec3(0,-2.8,0) , angular_velocity=(1,1,1),enable_extract_triangle=True , mass=0.1))
        # add(Cube(app, pos=glm.vec3(-5, 0, -20), tex_id=2 , velocity = glm.vec3(0,2,0), acceleration = glm.vec3(0,0,0),enable_extract_triangle=True,angular_velocity=(-1,-1,0.5) , mass=5))
        add(Cube(app, pos=glm.vec3(-5, 0, -20), tex_id=2 , velocity = glm.vec3(0,2,0), acceleration = glm.vec3(0,0,0),enable_extract_triangle=True, mass=5))
        
        # add(Cube(app, pos=(-5, 8, -20), tex_id=2 , velocity = glm.vec3(0,2,0),rot=(5, 2, 7), acceleration = glm.vec3(0,-2.8,0) , angular_velocity=(1,1,1),enable_extract_triangle=True))
        # add(Cube(app, pos=(-5, 2, -20), tex_id=2 , velocity = glm.vec3(0,0,0), acceleration = glm.vec3(0,0,0),enable_extract_triangle=True))
        # add(Cube(app, pos=(-5, 8, -20), tex_id=2 , velocity = glm.vec3(0,2,0),rot=(5, 2, 7), acceleration = glm.vec3(0,-2.8,0) , angular_velocity=(1,1,1),enable_extract_triangle=True))
        # add(Cube(app, pos=(-5, 2, -20), tex_id=2 , velocity = glm.vec3(0,0,0), acceleration = glm.vec3(0,0,0),enable_extract_triangle=True))

        # add(Cube(app, pos=(-5, 6, -50), tex_id=2 , velocity = glm.vec3(0,2,0),rot=glm.mat3(), acceleration = glm.vec3(0,-2.8,0) , angular_velocity=(1,1,1),enable_extract_triangle=True))
        # add(Cube(app, pos=(-5, 2, -50), tex_id=2 , velocity = glm.vec3(0,0,0), acceleration = glm.vec3(0,0,0),enable_extract_triangle=True))


    def update(self):

        # self.moving_cube.rot.xyz = self.app.time

        # print(self.objects[-1].pos)
        # if 3==2:
                
        a = self.objects[-1]

        # print(a.id)
        b= self.objects[-2]

        print(f'this is velocity of a {a.velocity} \nthis is velocity of b {b.velocity}')
        c = self.objects[-3]
        # c = self.objects[-3]
        # print(b.id)
        # print(test_aabb_overlap(a,b))
        # test_aabb_overlap(a,b)
        # print(c.pos)



        handle_collision(a,b)
        handle_collision(a,b)
        handle_collision(c,b)
        c.velocity = glm.vec3(0,0,0)
        c.acceleration = glm.vec3(0,0,0)
        c.angular_velocity = glm.vec3(0,0,0)
        # c.rotation_matrix = glm.mat3(1)
        c.rot_matrix = glm.mat3(1)





        # print()
        # a.velocity = glm.vec3(0,0,0)
        #             a.acceleration = glm.vec3(0,0,0)
        #             b.velocity = glm.vec3(0,0,0)
        #             b.acceleration = glm.vec3(0,0,0)
        #             a.angular_velocity = glm.vec3(0,0,0)
        #             a.angular_acceleration = glm.vec3(0,0,0)
        #             b.angular_velocity = glm.vec3(0,0,0)
        #             b.angular_acceleration = glm.vec3(0,0,0)
        
        
        # handle_collision(a,b)

        # for t1 in a.triangles:
        #     for t2 in b.triangles:
        #         result = triangle_triangle_intersection(np.array(t1), np.array(t2))

        #         if isinstance(result, bool):
        #             res = result
        #             vec1, vec2 = None, None  # Set vectors to None or some default values
        #         else:
        #                                     # result[0] is a boolean, unpack the rest of the tuple
        #             res, vec1, vec2 = result
        #         # print(triangle_triangle_intersection(np.array(t1), np.array(t2)))
        #         # result = triangle_triangle_intersection(np.array(t1), np.array(t2))
        #         # res ,vec1 ,vec2 = result
        #         print(f'this is the res {res} \nthis is the vec1 {vec1} \nthis is the vec2 {vec2}')
        #         # if triangle_triangle_intersection(np.array(t1), np.array(t2))[0]: 
        #         if res: 
        #             print("collision detected between triangles")
                    
        #             a.velocity = glm.vec3(0,0,0)
        #             a.acceleration = glm.vec3(0,0,0)
        #             b.velocity = glm.vec3(0,0,0)
        #             b.acceleration = glm.vec3(0,0,0)
        #             a.angular_velocity = glm.vec3(0,0,0)
        #             a.angular_acceleration = glm.vec3(0,0,0)
        #             b.angular_velocity = glm.vec3(0,0,0)
        #             b.angular_acceleration = glm.vec3(0,0,0)
                        
        #             # if triangle_triangle_intersection(np.array(t1), np.array(t2)):
        #             #     print("collision detected between triangles")
        #             #     a.velocity = glm.vec3(0,0,0)
        #             #     a.acceleration = glm.vec3(0,0,0)
        #             #     b.velocity = glm.vec3(0,0,0)
        #             #     b.acceleration = glm.vec3(0,0,0)
        #             #     a.angular_velocity = glm.vec3(0,0,0)
        #             #     a.angular_acceleration = glm.vec3(0,0,0)
        #             #     b.angular_velocity = glm.vec3(0,0,0)
        #             #     b.angular_acceleration = glm.vec3(0,0,0)

        
        # test_aabb_overlap(cube1,cube2)
        
        # collision_detection()
        # print(f'this the time {self.app.time} \nthis is the rot { self.moving_cube.rot.xyz }\n')

        # self.moving_cube.rot.x = self.app.time



    # def update(self):
    #     pass
    #     # self.moving_cube.rot.xyz = self.app.time
    #     # self.moving_cube.rot.xyz = self.app.time