import gpytoolbox as gpy, polyscope as ps, numpy as np

def plot_z_coord(V,F):
    """This method plots the z-coordinate on the input mesh V,F"""

    f = V[:, 0]*0 + V[:, 1]*0 + V[:, 2]

    ps.init()
    ps_spot = ps.register_surface_mesh("spot", V, F)
    ps_spot.add_scalar_quantity("f", f, enabled=True)
    ps.show()

V, F = gpy.read_mesh("data/spot.obj")
plot_z_coord(V, F)
    