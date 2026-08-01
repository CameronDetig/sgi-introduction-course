import numpy as np 
import gpytoolbox as gpy
import polyscope as ps

def my_per_face_normals(V, F, unit_norm):
    """Vector perpendicular to all faces on a mesh

    Computes per face (optionally unit) normal vectors for a triangle mesh.

    Parameters
    ----------
    V : (n,d) numpy array
        vertex list of a triangle mesh
    F : (m,d) numpy int array
        face index list of a triangle mesh
    unit_norm : bool, optional (default True)
        Whether to normalize each face's normal before outputting

    Returns
    -------
    N : (n,d) numpy double array
        Matrix of per-face normals
    """
    N = []

    for face in F:
        v1 = V[face[0]]
        v2 = V[face[1]]
        v3 = V[face[2]]

        vec1 = v2 - v1
        vec2 = v3 - v2

        normal = np.cross(vec1, vec2)

        if unit_norm:
            normal = normal / np.linalg.norm(normal)

        N.append(normal)


    return np.array(N)


def main():
    V, F = gpy.read_mesh("data/spot_low_resolution.obj")
    N = my_per_face_normals(V, F, True)

    print(N)

    ps.init()
    ps_spot = ps.register_surface_mesh("spot", V, F, smooth_shade=False)
    ps_spot.add_vector_quantity("per-face normals", N, defined_on="faces", enabled=True)
    ps.show()

if __name__ == "__main__":
    main()
