

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

import numpy as np

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



def broad_phase_collision(a , b ):

    distance = glm.distance(a.position , b.position)
    if distance < 4:
        return True
    
    return False



def broad_phase_collision2(a , b  ):
    
    distance = glm.distance(a.position , b.position)
    if a.radius + b.radius > distance :

        return True
    
    return False


#region triafgle triangle intersection

def compute_plane(triangle):
    # Given triangle with points a, b, c
    a, b, c = triangle
    normal = np.cross(b - a, c - a)
    d = -np.dot(normal, a)
    return normal, d

def side_of_plane(plane, point):
    normal, d = plane
    return np.sign(np.dot(normal, point) + d)

def triangle_triangle_intersection(t1, t2):
    # 1. Compute the plane equation of triangle 1
    plane1 = compute_plane(t1)
    # Check if all vertices of triangle 2 are on the same side of plane 1
    if all(side_of_plane(plane1, v) > 0 for v in t2) or \
       all(side_of_plane(plane1, v) < 0 for v in t2):
        return False
    
    # 2. Compute the plane equation of triangle 2
    plane2 = compute_plane(t2)
    # Check if all vertices of triangle 1 are on the same side of plane 2
    if all(side_of_plane(plane2, v) > 0 for v in t1) or \
       all(side_of_plane(plane2, v) < 0 for v in t1):
        return False

    # 3. Compute the line L of intersection between the two planes.
    # Skipping this step in this code since we use it indirectly in the next steps

    # 4. Determine which principal coordinate axis is most parallel with the line L
    line_direction = np.cross(plane1[0], plane2[0])  # This is the direction of the line of intersection
    axis = np.argmax(np.abs(line_direction))

    # 5. Project the triangles onto the principal axis and compute scalar intervals
    t1_proj = [v[axis] for v in t1]
    t2_proj = [v[axis] for v in t2]
    t1_interval = (min(t1_proj), max(t1_proj))
    t2_interval = (min(t2_proj), max(t2_proj))

    # 6. Check if the intervals overlap
    return not (t1_interval[1] < t2_interval[0] or t1_interval[0] > t2_interval[1])

# Example usage:
triangle1 = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
triangle2 = np.array([[0.5, 0.5, 0], [1.5, 0.5, 0], [0.5, 1.5, 0]])

triangle3 = np.array([[0, 0, 0], [1, 0, 0], [0, 0, 1]])
triangle4 = np.array([[0, 0.5, 0], [1, 0.5, 0], [0, 0.5, 1]])
# print(triangle_triangle_intersection(triangle1, triangle2))  # This should print True since the triangles intersect
print(triangle_triangle_intersection(triangle3, triangle4))  # This should print True since the triangles intersect

#endregion 

# def narrow_phase_collision(cube1 , cube2):
#     triangles = 
#     for triangle1 in cube1.triangles:
#         for triangle2 in cube2.triangles:
#             if triangle_triangle_intersection(triangle1, triangle2):
#                 return True
#     return False