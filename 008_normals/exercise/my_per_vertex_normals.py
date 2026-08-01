import numpy as np 
import gpytoolbox as gpy
import polyscope as ps
from my_per_face_normals import my_per_face_normals

def my_per_vertex_normals(V,F):
    """Normal vectors to all vertices on a mesh

    Computes area-weighted per-vertex unit normal vectors for a triangle mesh.

    Parameters
    ----------
    V : (n,d) numpy array
        vertex list of a triangle mesh
    F : (m,d) numpy int array
        face index list of a triangle mesh

    Returns
    -------
    N : (m,d) numpy double array
        Matrix of per-vertex normals
    """

    face_normals = my_per_face_normals(V, F, True)
    face_double_areas = gpy.doublearea(V, F)

    vert_normals = []

    for vert_index in range(len(V)):
        vert_faces = []
        for face_index in range(len(F)):
            if vert_index in F[face_index]:
                vert_faces.append(face_index)

        weighted_normals = []
        for face_index in vert_faces:
            weighted_normals.append(face_normals[face_index] / (face_double_areas[face_index] / 2))

        vert_normals.append(np.mean(np.array(weighted_normals), axis=0))

    return np.array(vert_normals)
  

V, F = gpy.read_mesh("data/spot_low_resolution.obj")
vertex_normals = my_per_vertex_normals(V, F)

ps.init()
ps_spot = ps.register_surface_mesh("spot", V, F, smooth_shade=False)
ps_spot.add_vector_quantity("per-vertex normals", vertex_normals, defined_on="vertices", enabled=True)
ps.show()
