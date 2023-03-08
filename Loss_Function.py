import numpy as np

#1
def compute_error_for_line_given_points(b,w,points):
    totalError=0
    for i in range(len(points)):
        x=points[i,0]
        y=points[i,1]
        totalError+=(y-(w*x+b))**2
    return totalError/float(len(points))

def step_gradient(b_current,w_current,points,learning_rate):
    b_gradient=0
    w_gradient=0
    N=float(len(points))
    for i in range(len(points)):
        x=points[i,0]
        y=points[i,1]
        b_gradient+=(-2*(y-(w_current*x+b_current)))/N
        w_gradient+=(-2*x*(y-(w_current*x+b_current)))/N
    new_b=b_current-(learning_rate*b_gradient)
    new_w=w_current-(learning_rate*b_gradient)
    return [new_b,new_w]

def gradient_descent_runner(points,start_b,start_w,learning_rate,num_iter):
    b=start_b
    w=start_w
    for i in range(num_iter):
        b,w=step_gradient(b,w,points,learning_rate)
    return [b,w]

def run():
    points=np.random.randint(1,100,[100,2])
    learning_rate=0.005
    initial_b=0
    initial_w=0
    num_iter=100
    start_error=compute_error_for_line_given_points(initial_b,initial_w,points)
    print("start error= "+ str(start_error))
    [change_b,change_w]=gradient_descent_runner(points,initial_b,initial_w,learning_rate,num_iter)
    end_error=compute_error_for_line_given_points(change_b,change_w,points)
    print("end error= "+str(end_error))

run()