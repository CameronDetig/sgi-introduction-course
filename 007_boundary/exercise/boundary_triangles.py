import gpytoolbox as gpy, numpy as np

def boundary_triangles(F):
    """Return a list of boundary triangle indices for an input triangulation F.
    """

    # Compute boundary edges.
    bdry_edges = gpy.boundary_edges(F)

    # Find all triangles that contain both vertices of a boundary edge.
    # HINT: Look at the documentation of the `where` or `nonzero` function in NumPy.
    bdry_tri_list = []

    for face in F:
        for edge in bdry_edges:
            if edge[0] in face and edge[1] in face:
                bdry_tri_list.append(face)
                break

    return np.array(bdry_tri_list)


V = np.array([[0, 0], [0, 0.5], [0, 1], [0.5, 0], [0.5, 0.5], [0.5, 1], [1, 0], [1, 0.5], [1, 1]]) 
F = np.array([[0,3,1], [3,4,1], [1,4,2], [4,5,2], [3,6,4], [6,7,4], [4,7,5], [7,8,5]])

boundary_faces = boundary_triangles(F)

print(boundary_faces)
