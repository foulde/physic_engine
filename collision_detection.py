

# #take in 2 model entities and check for collision between them
# def check_for_collision(entitie1 , entitie2):
    
#     if entitie1.position.x < entitie2.position.x + entitie2.size.x and entitie1.position.x + entitie1.size.x > entitie2.position.x:
#         if entitie1.position.y < entitie2.position.y + entitie2.size.y and entitie1.position.y + entitie1.size.y > entitie2.position.y:
#             return True
#     return False


# def test_aabb_overlap( a , b):

#     dx = b.pos.x - a.pos.x
#     px = (b.scale[0] + a.scale[0]) - abs(dx)
#     if px <= 0:
#         return False
    
#     dy = b.pos.y - a.pos.y
#     py = (b.scale[1] + a.scale[1]) - abs(dy)
#     if py <= 0:
#         return False
    
#     dz = b.pos.z - a.pos.z
#     pz = (b.scale[2] + a.scale[2]) - abs(dz)
#     if pz <= 0:
#         return False
    
#     return True


# def test_aabb_overlap( a , b):

#     dx = b.pos[0] - a.pos[0]
#     px = (b.scale[0] + a.scale[0]) - abs(dx)
#     if px <= 0:
#         return False
    
#     dy = b.pos[1] - a.pos[1]
#     py = (b.scale[1] + a.scale[1]) - abs(dy)
#     if py <= 0:
#         return False
    
#     dz = b.pos[2] - a.pos[2]
#     pz = (b.scale[2] + a.scale[2]) - abs(dz)
#     if pz <= 0:
#         return False
    
#     return True

import glm


def test_aabb_overlap( a , b):

    dx = b.pos[0] - a.pos[0]
    px = (b.scale[0] + a.scale[0]) - abs(dx)
    if px <= 0:
        return False
    
    dy = b.pos[1] - a.pos[1]
    py = (b.scale[1] + a.scale[1]) - abs(dy)
    if py <= 0:
        return False
    
    dz = b.pos[2] - a.pos[2]
    pz = (b.scale[2] + a.scale[2]) - abs(dz)
    if pz <= 0:
        return False
    
    #just to look at the collision and freeze the objects
    a.velocity = glm.vec3(0,0,0)
    a.acceleration = glm.vec3(0,0,0)
    b.velocity = glm.vec3(0,0,0)
    b.acceleration = glm.vec3(0,0,0)
    a.angular_velocity = glm.vec3(0,0,0)
    a.angular_acceleration = glm.vec3(0,0,0)
    b.angular_velocity = glm.vec3(0,0,0)
    b.angular_acceleration = glm.vec3(0,0,0)
    
    return True




