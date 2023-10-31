import moderngl as mgl
import numpy as np
import glm























class BaseModel:
    def __init__(self, app, vao_name, tex_id, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.app = app
        self.pos = pos
        self.vao_name = vao_name
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        self.scale = scale
        self.m_model = self.get_model_matrix()
        self.tex_id = tex_id
        self.vao = app.mesh.vao.vaos[vao_name]
        self.program = self.vao.program
        self.camera = self.app.camera

        

    def update(self): ...

    def get_model_matrix(self):
        m_model = glm.mat4()
        # translate
        m_model = glm.translate(m_model, self.pos)
        # rotate

        m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))

        # m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
        # m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
        # m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
        # scale
        m_model = glm.scale(m_model, self.scale)
        return m_model

    def render(self):
        self.update()
        self.vao.render()


class ExtendedBaseModel(BaseModel):
    def __init__(self, app, vao_name, tex_id, pos, rot, scale):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.texture.use(location=0)
        self.program['camPos'].write(self.camera.position)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)

    def update_shadow(self):
        self.shadow_program['m_model'].write(self.m_model)

    def render_shadow(self):
        self.update_shadow()
        self.shadow_vao.render()

    def on_init(self):
        self.program['m_view_light'].write(self.app.light.m_view_light)
        # resolution
        self.program['u_resolution'].write(glm.vec2(self.app.WIN_SIZE))
        # depth texture
        self.depth_texture = self.app.mesh.texture.textures['depth_texture']
        self.program['shadowMap'] = 1
        self.depth_texture.use(location=1)
        # shadow
        self.shadow_vao = self.app.mesh.vao.vaos['shadow_' + self.vao_name]
        self.shadow_program = self.shadow_vao.program
        self.shadow_program['m_proj'].write(self.camera.m_proj)
        self.shadow_program['m_view_light'].write(self.app.light.m_view_light)
        self.shadow_program['m_model'].write(self.m_model)
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_0'] = 0
        self.texture.use(location=0)
        # mvp
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(self.camera.m_view)
        self.program['m_model'].write(self.m_model)
        # light
        self.program['light.position'].write(self.app.light.position)
        self.program['light.Ia'].write(self.app.light.Ia)
        self.program['light.Id'].write(self.app.light.Id)
        self.program['light.Is'].write(self.app.light.Is)


class Cube():
    def __init__(self, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1),
                  velocity = glm.vec3(0,0,0), acceleration = glm.vec3(0,0,0)):
        
        self.pos
        # self.velocity  = glm.vec3(5,0,0)
        # self.acceleration  = glm.vec3(0,-2.81,0)




    # def update_physics(self, delta_time): 
    #     self.velocity += self.acceleration*delta_time
    #     self.pos += self.velocity*delta_time
    
    #     self.m_model = self.get_model_matrix()

    #     # print(self.pos)
    #     print(self.scale)
    #     print(self.scale[0])
    #     # print(self.shape[0])

    # def update(self):
    #     delta_time= 0.016
    #     self.update_physics(delta_time)
    #     super().update()



        


# class MovingCube(Cube):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#     def update(self):
#         self.m_model = self.get_model_matrix()
#         super().update()





# print(glm.mat3(1/6))
















# # create 3d vector and  assign it a value
# vec3 = glm.vec3(1, 2, 3)
# vec2 = vec3*2
# # take each coordonate of the vector and save them in a variable
# scale= (2,1,1)

# vec1 = vec2*scale
# # print the vector
# print(vec1)


# Cube1 = Cube(1,2,3)


# cube1 =Cube(pos=(-5, 2, -50), tex_id=2 , velocity = glm.vec3(1,10,0), acceleration = glm.vec3(0,-9.8,0))



# create 3*3 matrix and assign it a value
# mat3 = glm.mat3(1)
#generate a 3*3 matrix with random value integer between 0 and 10
mat3 = glm.mat3([[1.0,1.0,1.0] ,[2.0,2.0,2.0] ,[3.0,3.0,3.0]])
# create 3 vector and assign them a value
vec3 = glm.vec3(1.0, 2.0, 3.0)
vec4 = glm.dvec3(1,2,3)
#multiply the matrix by the vector and store the result in a variable
# vec1 = mat3*vec3
# vec1 = vec3*mat3
# print the result
vec2 = glm.mul(mat3, vec3)
# vec5 = glm.mat3_mul_vector(mat3 , vec4)
vec5 = mat3 * vec4
# vec5 = glm.mul(vec4, mat3)
# print(vec1)
print(vec2)
print(f'vec5 = {vec5}')

