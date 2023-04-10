import numpy as np

v1 = np.asarray((4, 1, 3, -1))
v2 = np.asarray((2, 1, -3, 4))
v3 = np.asarray((1, 0, -2, 7))
v4 = np.asarray((6, 2, 9, -5))
print(type(v4))
list_vect = [v1, v2, v3, v4]
list_ui = []
u1 = v1
list_ui.append(u1)
for i in range(2, 4+1):
    list_uij = []
    ui = np.asarray((0, 0, 0, 0))
    for j in range(1, i):
        u_ij = (list_vect[i-1]*list_ui[j-1]) / \
            np.sqrt(sum(list_ui[j-1]*list_ui[j-1]))
        ui = ui + list_vect[i-1] - u_ij * list_ui[j-1]
    list_ui.append(ui)
print("{:.5f}".format(list_ui[-1][1]))
# 0.91611
# import numpy as np
# def vect_add(v1:tuple,v2:tuple):
#     return tuple([v1[i]+v2[i] for i in range(len(v1))])
# def vect_product(v1:tuple,v2:tuple):
#     return tuple([v1[i]*v2[i] for i in range(len(v1))])
# def k_vect(k:float,v1:tuple):
#     return tuple([k*coef for coef in v1])
# print(vect_product((4, 6, 2, 5),(4, 6, 2, 5)))
# v1 = (4,1,3,-1)
# v2 = (2,1,-3,4)
# v3 = (1,0,-2,7)
# v4 = (6, 2, 9, -5)
# list_vect=[v1,v2,v3,v4]
# list_ui=[]
# u1 = v1
# list_ui.append(u1)
# for i in range(2,4+1):
#     list_uij=[]
#     ui=(0,0,0,0)
#     for j in range(1,i):
#         u_ij =  k_vect(1/sum(vect_product(list_ui[j-1],list_ui[j-1])),vect_product(list_vect[j],list_ui[j-1]))
#         ui+=  (list_vect[j] - u_ij) * list_ui[j-1]   #vect_add(vect_add(list_vect[j],k_vect(-1, u_ij)),list_ui[j-1])
#     list_ui.append(ui)
# print(list_ui)
