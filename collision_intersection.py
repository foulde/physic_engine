



import numpy as np

def compute_plane(triangle):
    a, b, c = triangle
    normal = np.cross(b - a, c - a)
    d = -np.dot(normal, a)
    return normal, d

def side_of_plane(plane, point):
    normal, d = plane
    return np.sign(np.dot(normal, point) + d)

def intersection_line(plane1, plane2):
    direction = np.cross(plane1[0], plane2[0])
    x = np.linalg.solve([plane1[0], plane2[0], direction], [plane1[1], plane2[1], 0.])
    return x, direction

def triangle_triangle_intersection(t1, t2):
    plane1 = compute_plane(t1)
    plane2 = compute_plane(t2)
    

    if all(side_of_plane(plane1, v) > 0 for v in t2) or all(side_of_plane(plane1, v) < 0 for v in t2):
        return False, np.zeros(3), np.zeros(3)
    
    if all(side_of_plane(plane2, v) > 0 for v in t1) or all(side_of_plane(plane2, v) < 0 for v in t1):
        return False,np.zeros(3), np.zeros(3)

    point, direction = intersection_line(plane1, plane2)

    t1_intervals = []
    for i in range(3):
        t1_intervals.append(np.dot(t1[i] - point, direction))

    t2_intervals = []
    for i in range(3):
        t2_intervals.append(np.dot(t2[i] - point, direction))

    t1_min, t1_max = min(t1_intervals), max(t1_intervals)
    t2_min, t2_max = min(t2_intervals), max(t2_intervals)

    if t1_max < t2_min or t2_max < t1_min:
        return False,np.zeros(3), np.zeros(3)

    i_min = max(t1_min, t2_min)
    i_max = min(t1_max, t2_max)

    p1 = point + i_min * direction
    p2 = point + i_max * direction

    return True,p1, p2

triangle3 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
triangle4 = np.array([[2, 0, 0], [0, 2, 0], [0, 0, 2]])
# triangle4 = np.array([[0, 0, 0], [1, 0, 1], [1, 1, 1]])

# p1, p2 = triangle_triangle_intersection(triangle3, triangle4)
ooo , a , b = triangle_triangle_intersection(triangle3, triangle4)
print(ooo)
#does not handle when the triangles are coplanar to solve the issue introduce very small epsilon value
# print(p1, p2)


# def 


import glm

def compute_r1_r2(cube1_pos, cube2_pos, contact_point):
    """
    Calculate the vectors from the center of mass of each cube to the point of contact.
    
    Args:
    cube1_pos (glm.vec3): The position of the center of mass of cube1.
    cube2_pos (glm.vec3): The position of the center of mass of cube2.
    contact_point (glm.vec3): The position of the contact point where collision occurs.
    
    Returns:
    glm.vec3, glm.vec3: Returns r1 and r2, vectors from center of mass to contact point for cube1 and cube2 respectively.
    """
    r1 = contact_point - cube1_pos
    r2 = contact_point - cube2_pos
    return r1, r2

# Usage Example
cube1_pos = glm.vec3(1, 2, 3)
cube2_pos = glm.vec3(4, 5, 6)
contact_point = glm.vec3(2, 3, 4)

r1, r2 = compute_r1_r2(cube1_pos, cube2_pos, contact_point)
print("r1:", r1)
print("r2:", r2)



def compute_impulse(u, m1, m2, r1, r2, IA1_inv, IA2_inv):
    # Helper function to compute the 3x3 skew-symmetric matrix of a vector
    def skew_symmetric(v):
        return np.array([
            [0, -v[2], v[1]],
            [v[2], 0, -v[0]],
            [-v[1], v[0], 0]
        ])
    
    # Mass matrix component
    M_inv = np.diag([1/m1 + 1/m2]*3)
    
    # Inertia components
    R1 = skew_symmetric(r1)
    R2 = skew_symmetric(r2)
    I1 = R1 @ IA1_inv @ R1.T
    I2 = R2 @ IA2_inv @ R2.T
    
    # Assemble the K matrix
    K = M_inv + I1 + I2
    
    # Compute impulse
    try:
        p = np.linalg.inv(K) @ u
        return p
    except np.linalg.LinAlgError:
        print("Matrix K is singular. Cannot compute the impulse.")
        return np.zeros(3)

# You can then test this updated function with your values


# Example usage:
u = np.array([1, 0, 0])  # Relative velocity
m1 = 1.0
m2 = 1.0
r1 = np.array([0, 1, 0])
r2 = np.array([0, -1, 0])
IA1_inv = np.eye(3)  # Inverse inertia tensor for body 1 (assuming it's a unit cube for simplicity)
IA2_inv = np.eye(3)  # Inverse inertia tensor for body 2 (assuming it's a unit cube for simplicity)

impulse = compute_impulse(u, m1, m2, r1, r2, IA1_inv, IA2_inv)
print(f'this is the impulse: {impulse}')
