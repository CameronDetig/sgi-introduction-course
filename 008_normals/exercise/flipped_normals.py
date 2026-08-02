import gpytoolbox as gpy
import numpy as np
import polyscope as ps

def flipped_normals(V,F):
    """
    Compute the flipped per-face normals of a triangle mesh.
    """

    N = []

    for face in F:
        v1 = V[face[0]]
        v2 = V[face[1]]
        v3 = V[face[2]]

        vec1 = v2 - v1
        vec2 = v3 - v2

        normal = np.cross(vec2, vec1)

        N.append(normal)


    return np.array(N)


def main():
    V, F = gpy.read_mesh("data/spot_low_resolution.obj")
    N = flipped_normals(V, F)

    print(N)

    ps.init()
    ps_spot = ps.register_surface_mesh("spot", V, F)
    ps_spot.set_edge_width(1.0)
    ps_spot.set_transparency(0.2)
    ps_spot.add_vector_quantity("per-face flipped normals", N, defined_on="faces", enabled=True)
    ps.show()

if __name__ == "__main__":
    main()

