import numpy as np
import polyscope as ps

def tetrahedron():
    V = np.array([[0., 0., 0.],
                  [1., 0., 0.],
                  [0., 1., 0.],
                  [0., 0., 1.]])
    print(V)

    F = np.array([[1, 0, 2],
                  [0, 1, 3],
                  [1, 2, 3],
                  [2, 0, 3]])
    print(F)

    ps.init()
    ps.register_surface_mesh("triangle", V, F)
    ps.show()


def pyramid():
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

    ps.init()
    ps.register_surface_mesh("triangle", V, F)
    ps.show()


pyramid()
