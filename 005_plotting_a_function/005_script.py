import numpy as np
import gpytoolbox as gpy
import polyscope as ps

V,F = gpy.read_mesh("data/spot.obj")

def per_vertex():
    # To plot a per-vertex function, define a vector of length n, 
    # where n is the number of vertices that holds the function value for each vertex
    f = V[:, 0]**2 + V[:, 1]**2 + V[:, 2]**2

    ps.init()
    ps_spot = ps.register_surface_mesh("spot", V, F)
    ps_spot.add_scalar_quantity("f", f, enabled=True)
    ps.show()

def per_face():
    # To plot a per-face function, define a vector of length m, 
    # where m is the number of faces that holds the function value for each face
    centers = (V[F[:,0], :] + 
               V[F[:,1], :] + 
               V[F[:,2], :]) / 3
    f = centers[:,0]**2 + centers[:,1]**2 + centers[:,2]**2

    ps.init()
    ps_spot = ps.register_surface_mesh("spot", V, F)
    ps_spot.add_scalar_quantity("f", f, defined_on="faces", cmap="reds", enabled=True)
    ps.show()

per_face()
