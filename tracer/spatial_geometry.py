# Various routines for vector geometry, rotations, etc.
# References:
# [1] John J. Craig, Introduction to Robotics, 3rd ed., 2005. 

from math import sin,  cos
import numpy as N

def general_axis_rotation(axis,  angle):
    """Generates a rotation matrix around <axis> by <angle>, using the right-hand
    rule.
    Arguments: 
        axis - a 3-component 1D array representing a unit vector
        angle - rotation counterclockwise in radians around the axis when the axis 
            points to the viewer.
    Returns: A 3x3 array representing the matrix of rotation.
    Reference: [1] p.47
    """
    s = sin(angle); c = cos(angle); v = 1 - c
    add = N.array([[0,          -axis[2], axis[1]],  
                            [axis[2],  0,          -axis[0]], 
                            [-axis[1], axis[0],  0        ] ])
    return N.multiply.outer(axis,  axis)*v + N.eye(3)*c + add*s

def generate_transform(axis, angle, translation):
    """Generates a transformation matrix                                                      
    Arguments: axis - a 3-component 1D array giving the unit vector to rotate about          
    angle - angle of rotation counter clockwise in radians about the given axis in the 
    parent frame                         
    translation - a 3-component column vector giving the translation along the coordinates
    of the parent object/assembly
    """  
    rot = general_axis_rotation(axis, angle)
    return N.vstack((N.hstack((rot, translation)), N.r_[[0,0,0,1]]))

def rotx(ang):
    """Generate a homogenous trransform for ang radians around the x axis"""
    s = sin(ang); c = cos(ang)
    return N.array([
        [1., 0, 0, 0],
        [0, c, s, 0],
        [0,-s, c, 0],
        [0, 0, 0, 1]
    ])

def roty(ang):
    """Generate a homogenous trransform for ang radians around the y axis"""
    s = sin(ang); c = cos(ang)
    return N.array([
        [c, 0, s, 0],
        [0, 1, 0, 0],
        [-s,0, c, 0],
        [0, 0, 0, 1]
    ])
