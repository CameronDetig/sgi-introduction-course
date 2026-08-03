import gpytoolbox as gpy
import numpy as np
import polyscope as ps

def my_angle_defect(V,F):
    """
    Compute the angle defect per vertex on the mesh V,F
    """

    angles = gpy.tip_angles(V, F) # shape (m, 3), angles[i, j] is the angle
    # at vertex F[i, j] inside triangle i

    # Sum the tip angles meeting at each vertex by scattering each corner's
    # angle into a per-vertex accumulator (a vertex can appear in many
    # triangles, so this adds up all the angles it's the "tip" of).
    angle_sum = np.zeros(V.shape[0])
    np.add.at(angle_sum, F.flatten(), angles.flatten())

    # A flat interior point has angles summing to 2*pi; a flat boundary
    # point (edge of an open mesh) only has angles summing to pi, since
    # it's not surrounded on all sides. Angle defect is how far short of
    # that flat-case total the actual angle sum falls.
    full_angle = np.full(V.shape[0], 2 * np.pi)
    boundary_verts = gpy.boundary_vertices(F)
    full_angle[boundary_verts] = np.pi

    return full_angle - angle_sum


def main():
    V, F = gpy.read_mesh("data/armadillo.obj")

    angle_def = my_angle_defect(V, F)

    ps.init()
    ps_mesh = ps.register_surface_mesh("mesh", V, F)
    ps_mesh.add_scalar_quantity("angle_defect", angle_def, cmap="coolwarm", enabled=True)
    ps.show()


if __name__ == "__main__":
    main()
    