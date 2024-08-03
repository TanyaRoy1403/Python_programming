# import turtle as tur
# # tur.hideturtle()
# # tur.color("green")
# tur.begin_fill()
# tur.forward(100)
# tur.left(90)
# tur.forward(100)
# tur.left(90)
# tur.forward(100)
# tur.left(90)
# tur.forward(100)
# # tur.end_fill()


# # tur.color("yellow")
# # tur.begin_fill()
# tur.seth(45)
# tur.penup()
# tur.fd(50)
# tur.seth(0)
# tur.pendown()
# tur.forward(100)
# tur.left(90)
# tur.forward(100)
# tur.left(90)
# tur.forward(100)
# tur.left(90)
# tur.forward(100)
# # tur.end_fill()

# # tur.color("black")
# tur.goto(0,0)
# tur.left(180)
# tur.penup()
# tur.forward(100)
# tur.seth(45)
# tur.pendown()
# tur.fd(50)
# tur.penup()
# tur.right(45)
# tur.fd(100)
# tur.seth(45)
# tur.pendown()
# tur.bk(50)
# tur.goto(100,0)
# tur.fd(50)





# screen = tur.Screen()
# screen.exitonclick()
import numpy as np
# x = np.array([1, -2, -5])
# y = np.array([4, 3, -1])

# print("Shape of vector x:", x.shape)
# print("Number of dimensions of vector x:", x.ndim)
# print("Shape of vector x, reshaped to a matrix:", x.reshape((3, 1)).shape)
# print("Number of dimensions of vector x, reshaped to a matrix:", x.reshape((3, 1)).ndim)
# result=np.matmul(x,y)
# print(result)
# print(np.dot(x,y))

def T(v,u):
    w = np.zeros((3,1))
    w[0,0] = 3*v[0,0]
    w[2,0] = -2*v[1,0]
    
    return w

# v = np.array([[3], [5]])
# w = T(v)

print("Original vector:\n", v, "\n\n Result of the transformation:\n", w)

u = np.array([[1], [-2]])
v = np.array([[2], [4]])
print(u)
print(v)

k = 7

print("T(k*v):\n", T(k*v), "\n k*T(v):\n", k*T(v), "\n\n")
print("T(u+v):\n", T(u+v), "\n T(u)+T(v):\n", T(u)+T(v))