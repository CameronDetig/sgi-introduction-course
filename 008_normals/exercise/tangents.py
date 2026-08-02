import numpy as np 
import gpytoolbox as gpy
import polyscope as ps

def tangents(V,F):
    """
    Computes two orthogonal, oriented tangent vectors for each face in a
    triangle mesh.
    """

    # vectorize the verts without having to use a for loop
    vert1 = V[F[:,0]]
    vert2 = V[F[:,1]]
    vert3 = V[F[:,2]]

    print(vert1[:3])

    # Extract the first edge of each face and normalize it.
    edge1 = vert2 - vert1
    # axis=-1 takes the norm over the xyz components of each row (not across
    # faces), giving one length per face; keepdims=True keeps that as shape
    # (num_faces, 1) instead of (num_faces,) so it broadcasts against edge1's
    # (num_faces, 3) shape during the division.
    tangent_1 = edge1 / np.linalg.norm(edge1, axis=-1, keepdims=True)

    # Extract the second edge and project onto the orthogonal complement of E1.
    edge2 = vert3 - vert1
    proj_len = np.sum(edge2 * tangent_1, axis=-1, keepdims=True)
    edge2_orth = edge2 - proj_len * tangent_1

    # Normalize to get unit vectors (same axis=-1/keepdims reasoning as above)
    tangent_2 = edge2_orth / np.linalg.norm(edge2_orth, axis=-1, keepdims=True)

    return tangent_1, tangent_2



def main():
    V, F = gpy.read_mesh("data/spot_low_resolution.obj")
    tangent_1, tangent_2 = tangents(V, F)

    ps.init()
    ps_spot = ps.register_surface_mesh("spot", V, F, smooth_shade=False)
    ps_spot.add_vector_quantity("tangent 1", tangent_1, defined_on="faces", enabled=True)
    ps_spot.add_vector_quantity("tangent 2", tangent_2, defined_on="faces", enabled=True)
    ps.show()

if __name__ == "__main__":
    main()
