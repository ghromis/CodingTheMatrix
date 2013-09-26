from mat import Mat
import math
import image_mat_util 

## Task 1
def identity(labels = {'x','y','u'}):
    '''
    In case you have never seen this notation for a parameter before,
    the way it works is that identity() now defaults to having labels 
    equal to {'x','y','u'}.  So you should write your procedure as if 
    it were defined 'def identity(labels):'.  However, if you want the labels of 
    your identity matrix to be {'x','y','u'}, you can just call 
    identity().  Additionally, if you want {'r','g','b'}, or another set, to be the
    labels of your matrix, you can call identity({'r','g','b'}).  
    '''
    d = {}
    for e in labels:
        d[(e,e)]=1
    return Mat((labels, labels),d)
    

## Task 2
def translation(x,y):
    '''
    Input:  An x and y value by which to translate an image.
    Output:  Corresponding 3x3 translation matrix.
    '''
    d=identity().f
    d[('x','u')]=x
    d[('y','u')]=y
    return Mat((identity().D),d)
    

## Task 3
def scale(a, b):
    '''
    Input:  Scaling parameters for the x and y direction.
    Output:  Corresponding 3x3 scaling matrix.
    '''
    d=identity().f
    d[('x','x')]=a
    d[('y','y')]=b
    return Mat((identity().D),d)

## Task 4
def rotation(angle):
    '''
    Input:  An angle in radians to rotate an image.
    Output:  Corresponding 3x3 rotation matrix.rota
    Note that the math module is imported.
    '''
    d=identity().f
    d[('x','x')]=math.cos(angle)
    d[('y','x')]=math.sin(angle)
    d[('x','y')]=-math.sin(angle)
    d[('y','y')]=math.cos(angle)
    return Mat((identity().D),d)

## Task 5
def rotate_about(x,y,angle):
    '''
    Input:  An x and y coordinate to rotate about, and an angle
    in radians to rotate about.
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
    '''
    return translation(x,y) * rotation(angle) * translation(-x,-y)

## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.
    '''
    return scale(-1, 1)

## Task 7
def reflect_x():
    '''
    Inpute:  None.
    Output:  3x3 X-reflection matrix.
    '''
    return scale(1, -1)
    
## Task 8    
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.
    '''
    d=identity(labels = {'r','g','b'}).f
    d[('r','r')]=scale_r
    d[('g','g')]=scale_g
    d[('b','b')]=scale_b
    return Mat((identity(labels = {'r','g','b'}).D),d)

## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    d=identity(labels = {'r','g','b'}).f
    l = [v for k,v in d.items()]
    c = 77*l[0]/256 + 151*l[1]/256 + 28*l[2]/256
    d[('r','r')]=77*l[0]/256
    d[('g','r')]=77*l[0]/256
    d[('b','r')]=77*l[0]/256
    d[('g','g')]=151*l[1]/256
    d[('r','g')]=151*l[1]/256
    d[('b','g')]=151*l[1]/256
    d[('b','b')]=28*l[2]/256
    d[('g','b')]=28*l[2]/256
    d[('r','b')]=28*l[2]/256
    return Mat((identity(labels = {'r','g','b'}).D),d) 


## Task 10
def reflect_about(p1,p2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.
    '''
    pass


