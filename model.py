import moderngl as mgl
import numpy as np
import glm
from math import cos, sin

# def skew_matrix(v):
#     return glm.mat3(0, -v.z, v.y,
#                     v.z, 0, -v.x,
#                     -v.y, v.x, 0)



# def euler_to_mat3(x, y, z):
#     Rx = glm.mat3(1, 0, 0,
#                   0, cos(x), -sin(x),
#                   0, sin(x), cos(x))
    
#     Ry = glm.mat3(cos(y), 0, sin(y),
#                   0, 1, 0,
#                   -sin(y), 0, cos(y))

#     Rz = glm.mat3(cos(z), -sin(z), 0,
#                   sin(z), cos(z), 0,
#                   0, 0, 1)
    
#     return Rz * Ry * Rx




# def mat3_to_rot_vec(R):
#     # Calculate rotation angle
#     theta = np.arccos((R[0][0] + R[1][1] + R[2][2] - 1) / 2)

#     # If angle is very close to 0 or pi (180 degrees), we need special handling
#     if np.isclose(theta, 0):
#         return glm.vec3(0, 0, 0)
#     elif np.isclose(theta, np.pi):
#         # It's an edge case where multiple rotation vectors are possible
#         # We'll pick one of them
#         x = np.sqrt((R[0][0] + 1) / 2)
#         y = np.sqrt((R[1][1] + 1) / 2)
#         z = np.sqrt((R[2][2] + 1) / 2)
#         return glm.vec3(theta * x, theta * y, theta * z)

#     # Calculate rotation axis for general case
#     rx = (R[2][1] - R[1][2]) / (2 * np.sin(theta))
#     ry = (R[0][2] - R[2][0]) / (2 * np.sin(theta))
#     rz = (R[1][0] - R[0][1]) / (2 * np.sin(theta))
    
#     return glm.vec3(theta * rx, theta * ry, theta * rz)



# def orthonormalize(mat):
#     x = glm.normalize(mat[0])
#     y = glm.normalize(mat[1])
#     z = glm.normalize(mat[2])
#     return glm.mat3(x, y, z)





def orthonormalize(mat):
    # Assume input is a 3x3 matrix
    x = mat[0]
    y = mat[1]
    z = mat[2]

    # Gram-Schmidt process
    x = glm.normalize(x)
    y -= x * glm.dot(x, y)
    y = glm.normalize(y)
    z = glm.cross(x, y)  # No need to subtract projections, as x and y are already orthogonal

    return glm.mat3(x, y, z)

# ... Inside your update_physics function ...











class BaseModel:
    def __init__(self, app, vao_name, tex_id, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        self.app = app
        self.pos = pos
        self.vao_name = vao_name
        self.rot = glm.vec3([glm.radians(a) for a in rot])
        # self.rot_matrix = glm.mat3(glm.eulerAngleXYZ(self.rot.x, self.rot.y, self.rot.z))
        self.rot_matrix = self.euler_to_mat3()
        # self.rot_matrix = self.euler_to_mat3(self.rot.x, self.rot.y, self.rot.z)
        self.scale = scale
        self.m_model = self.get_model_matrix()
        self.tex_id = tex_id
        self.vao = app.mesh.vao.vaos[vao_name]
        self.program = self.vao.program
        self.camera = self.app.camera
        # self.mass = 1
        self.vbo = app.mesh.vao.vbo.vbos[vao_name]
        # print(f'vbo object: {self.vbo}')
    

    def euler_to_mat3(self):
        x = self.rot.x
        y = self.rot.y
        z = self.rot.z
        Rx = glm.mat3(1, 0, 0,
                    0, cos(x), -sin(x),
                    0, sin(x), cos(x))
        
        Ry = glm.mat3(cos(y), 0, sin(y),
                    0, 1, 0,
                    -sin(y), 0, cos(y))

        Rz = glm.mat3(cos(z), -sin(z), 0,
                    sin(z), cos(z), 0,
                    0, 0, 1)
        
        return Rz * Ry * Rx

        

    def update(self): ...

    

    # def get_model_matrix(self):
    #     self.m_model = glm.mat4()
    #     self.m_model = glm.translate(self.m_model, self.pos)
    #     self.m_model *= glm.mat4(self.rot_matrix)  # Use rotation matrix instead of Euler angles
    #     self.m_model = glm.scale(self.m_model, self.scale)
    #     # return m_model
    


    def get_model_matrix(self):
        m_model = glm.mat4()
        m_model = glm.translate(m_model, self.pos)
        m_model *= glm.mat4(self.rot_matrix)  # Use rotation matrix instead of Euler angles
        m_model = glm.scale(m_model, self.scale)
        return m_model
    


    # def get_model_matrix(self):
    #     m_model = glm.mat4()
    #     # translate
    #     m_model = glm.translate(m_model, self.pos)
    #     # rotate

    #     m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
    #     m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
    #     m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
    #     # print(f'this is the rot of {self.} :\n{self.rot}')
    #     # print(self.rot)

    #     # m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
    #     # m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
    #     # m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
    #     # scale
    #     m_model = glm.scale(m_model, self.scale)
    #     return m_model





    def render(self):
        self.update()
        self.vao.render()   



class ExtendedBaseModel(BaseModel):
    def __init__(self, app, vao_name, tex_id, pos, rot, scale ):
        super().__init__(app, vao_name, tex_id, pos, rot, scale  )
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


class Cube(ExtendedBaseModel):
    def __init__(self, app, vao_name='cube', tex_id=0, pos=glm.vec3(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1),
                  velocity = glm.vec3(0,0,0), acceleration = glm.vec3(0,0,0), angular_velocity = glm.vec3(0,0,0)
                  , angular_acceleration = glm.vec3(0,0,0) , enable_extract_triangle = False , mass = 1 ,inertia_tensor = glm.mat3(1), id="no" ):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        
        self.mass = mass
        
        self.inertia_tensor = inertia_tensor
        self.natural_inertia_tensor = inertia_tensor
        self.inverse_inertia_tensor =glm.inverse(self.inertia_tensor)
        self.velocity  = velocity
        self.acceleration  = acceleration
        self.angular_velocity = angular_velocity
        self.angular_acceleration = angular_acceleration

        self.enable_extract_triangle = enable_extract_triangle
        self.triangles = self._extract_triangles()
        self.id = id





    def skew_matrix(self):
        return glm.mat3(0, -self.angular_velocity.z, self.angular_velocity.y,
                        self.angular_velocity.z, 0, -self.angular_velocity.x,
                        -self.angular_velocity.y, self.angular_velocity.x, 0)



    # def euler_to_mat3(x, y, z):
    #     Rx = glm.mat3(1, 0, 0,
    #                 0, cos(x), -sin(x),
    #                 0, sin(x), cos(x))
        
    #     Ry = glm.mat3(cos(y), 0, sin(y),
    #                 0, 1, 0,
    #                 -sin(y), 0, cos(y))

    #     Rz = glm.mat3(cos(z), -sin(z), 0,
    #                 sin(z), cos(z), 0,
    #                 0, 0, 1)
        
    #     return Rz * Ry * Rx



    # def get_model_matrix(self):
    #     m_model = glm.mat4()
    #     # translate
    #     m_model = glm.translate(m_model, self.pos)
    #     # rotate

    #     m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
    #     m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
    #     m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
    #     # print(f'this is the rot of {self.} :\n{self.rot}')
    #     # print(self.rot)

    #     # m_model = glm.rotate(m_model, self.rot.z, glm.vec3(0, 0, 1))
    #     # m_model = glm.rotate(m_model, self.rot.y, glm.vec3(0, 1, 0))
    #     # m_model = glm.rotate(m_model, self.rot.x, glm.vec3(1, 0, 0))
    #     # scale
    #     m_model = glm.scale(m_model, self.scale)
    #     return m_model




    def mat3_to_rot_vec(self):
        R = self.rot_matrix
        # Calculate rotation angle
        theta = np.arccos((R[0][0] + R[1][1] + R[2][2] - 1) / 2)

        # If angle is very close to 0 or pi (180 degrees), we need special handling
        if np.isclose(theta, 0):
            return glm.vec3(0, 0, 0)
        elif np.isclose(theta, np.pi):
            # It's an edge case where multiple rotation vectors are possible
            # We'll pick one of them
            x = np.sqrt((R[0][0] + 1) / 2)
            y = np.sqrt((R[1][1] + 1) / 2)
            z = np.sqrt((R[2][2] + 1) / 2)
            return glm.vec3(theta * x, theta * y, theta * z)

        # Calculate rotation axis for general case
        rx = (R[2][1] - R[1][2]) / (2 * np.sin(theta))
        ry = (R[0][2] - R[2][0]) / (2 * np.sin(theta))
        rz = (R[1][0] - R[0][1]) / (2 * np.sin(theta))
        
        return glm.vec3(theta * rx, theta * ry, theta * rz)

















        


            

    def _extract_triangles(self):
        triangles = []

        if not self.vbo :
            return triangles
        if not self.enable_extract_triangle:
            return None
        vertex_data = self.vbo.get_vertex_data()
        # Convert each vertex from vec3 to vec4
        homogenous_vertices = [glm.vec4(vertex[-3], vertex[-2], vertex[-1], 1.0) for vertex in vertex_data]
        # Transform each vertex using the model matrix
        world_data = [self.m_model * vertex for vertex in homogenous_vertices]
        # Convert back to vec3
        world_data_vec3 = [(vertex.x, vertex.y, vertex.z) for vertex in world_data]

        # Extract triangles using indices 
        # Assuming vertex_data has vertices in the format: triangle1_vertex1, triangle1_vertex2, triangle1_vertex3, ...
        for i in range(0, len(world_data_vec3), 3):
            triangle = [world_data_vec3[i], world_data_vec3[i+1], world_data_vec3[i+2]]
            triangles.append(triangle)


            
        return triangles
    






    def update_physics(self, delta_time, impulse=None , torque=None , r_impact =None):
        impulse = glm.vec3(0,0,0) if impulse is None else glm.vec3(impulse) 
        # effective_torque = glm.vec3(0,0,0) if torque is None else torque
        r_impact = glm.vec3(0,0,0) if r_impact is None else glm.vec3(r_impact)

        self.velocity += self.acceleration*delta_time + impulse/self.mass
        self.pos += self.velocity*delta_time

        self.inertia_tensor = self.rot_matrix * self.natural_inertia_tensor * glm.transpose(self.rot_matrix)
        self.inverse_inertia_tensor = glm.inverse(self.inertia_tensor)
        # to = glm.vec3(glm.cross(r_impact,impulse))
        to = glm.vec3(glm.cross(r_impact,impulse))
        """
        print("\n \n")
        print(f'this is to: {to}')
        print(f'this is regular vector :{glm.vec3(1,2,3)}')
        print(f'this is r_impact: {r_impact}')
        print(f'this is impulse: {impulse}')
        print("\n \n")
"""
        # self.angular_velocity += self.angular_acceleration*delta_time  + glm.mul(self.inverse_inertia_tensor , to)
        self.angular_velocity +=  glm.mul(self.inverse_inertia_tensor , glm.vec3(glm.cross(r_impact,impulse)))

##
        # omega_skew = self.skew_matrix(self.angular_velocity)
        omega_skew = self.skew_matrix()
        delta_rot = glm.mat3(1) + omega_skew * delta_time
        # self.rot = delta_rot * self.rot
        self.rot_matrix = delta_rot * self.rot_matrix
        self.rot_matrix = orthonormalize(self.rot_matrix)  # Normalization step
        # self.rot = self.mat3_to_rot_vec()
##
        # self.rot += self.angular_velocity*delta_time
        self.triangles = self._extract_triangles()
        self.m_model = self.get_model_matrix()


    def update(self):
        delta_time= 0.016
        self.update_physics(delta_time)
        super().update()





# class Cube(ExtendedBaseModel):
#     def __init__(self, app, vao_name='cube', tex_id=0, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1),
#                   velocity = glm.vec3(0,0,0), gravity = glm.vec3(0,0,0)):
#         super().__init__(app, vao_name, tex_id, pos, rot, scale)
        
#         # self.velocity  = glm.vec3(5,0,0)
#         # self.gravity  = glm.vec3(0,-2.81,0)

#         self.velocity  = velocity
#         self.gravity  = gravity



#     def update_physics(self, delta_time): 
#         self.velocity += self.gravity*delta_time
#         self.pos += self.velocity*delta_time

        
    
#         self.m_model = self.get_model_matrix()

#         # print(self.pos)
#         # print(self.scale)
#         # print(self.scale[0])
#         # print(self.shape[0])
#         # print(f'position complete {self.pos}')
#         # print(self.pos.x)

#     def update(self):
#         delta_time= 0.016
#         self.update_physics(delta_time)
#         super().update()




        


class MovingCube(Cube):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self):
        self.m_model = self.get_model_matrix()
        super().update()


class Cat(ExtendedBaseModel):
    def __init__(self, app, vao_name='cat', tex_id='cat',
                 pos=(0, 0, 0), rot=(-90, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)

    


class SkyBox(BaseModel):
    def __init__(self, app, vao_name='skybox', tex_id='skybox',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        self.program['m_view'].write(glm.mat4(glm.mat3(self.camera.m_view)))

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_skybox'] = 0
        self.texture.use(location=0)
        # mvp
        self.program['m_proj'].write(self.camera.m_proj)
        self.program['m_view'].write(glm.mat4(glm.mat3(self.camera.m_view)))


class AdvancedSkyBox(BaseModel):
    def __init__(self, app, vao_name='advanced_skybox', tex_id='skybox',
                 pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        super().__init__(app, vao_name, tex_id, pos, rot, scale)
        self.on_init()

    def update(self):
        m_view = glm.mat4(glm.mat3(self.camera.m_view))
        self.program['m_invProjView'].write(glm.inverse(self.camera.m_proj * m_view))

    def on_init(self):
        # texture
        self.texture = self.app.mesh.texture.textures[self.tex_id]
        self.program['u_texture_skybox'] = 0
        self.texture.use(location=0)



