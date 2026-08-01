import numpy as np
import gpytoolbox as gpy
import polyscope as ps

V = np.array([[0., 0., 0.],
                [0., 0., 1.],
                [1., 0., 0.],
                [1., 0., 1.],
                [0.5, 1., 0.5]])
print(V)

F = np.array([[0, 1, 4],
                [1, 3, 4],
                [3, 2, 4],
                [2, 0, 4],])
print(F) 

gpy.write_mesh('data/pyramid.obj', V, F)


V, F = gpy.read_mesh('data/bunny.obj')

ps.init()
ps.register_surface_mesh("triangle", V, F)
ps.show()
