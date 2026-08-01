import numpy as np
import gpytoolbox as gpy

def my_boundary_edges(F):
    """Given a triangle mesh with face indices F, returns all unique oriented
    boundary edges as indices into the vertex array.
    Works only on manifold meshes.

    Parameters:
    F : (m,3) numpy int array.
        face index list of a triangle mesh

    Returns:
    bE : (be,2) numpy int array.
        indices of boundary edges into the vertex array
    """
    edges = [[0, 1], [1, 2], [0, 2]]
    bE = []

    for cur_face in range(len(F)):
        for edge in edges:
            is_boundary = True
            for compare_face in range(len(F)):
                if compare_face != cur_face:
                    if F[cur_face][edge[0]] in F[compare_face] and F[cur_face][edge[1]] in F[compare_face]:
                        is_boundary = False
            if is_boundary == True:
                bE.append([int(F[cur_face][edge[0]]), int(F[cur_face][edge[1]])])
                


    return bE
    

V = np.array([[0, 0], [0, 0.5], [0, 1], [0.5, 0], [0.5, 0.5], [0.5, 1], [1, 0], [1, 0.5], [1, 1]]) 
F = np.array([[0,3,1], [3,4,1], [1,4,2], [4,5,2], [3,6,4], [6,7,4], [4,7,5], [7,8,5]])


boundary_edges = my_boundary_edges(F)
for edge in boundary_edges:
    print(edge)

bdry_edges = gpy.boundary_edges(F)
print(f"\nTrue answer: \n{bdry_edges}")
