import numpy as np
import gpytoolbox as gpy
import polyscope as ps

V,F = gpy.read_mesh("data/spot_low_resolution.obj")

def render():
    ps.init()
    ps_spot = ps.register_surface_mesh("spot", V, F, smooth_shade=True, material="candy")
    ps.set_view_projection_mode("perspective")
    ps.set_ground_plane_mode("shadow_only")
    ps.show()

render()
