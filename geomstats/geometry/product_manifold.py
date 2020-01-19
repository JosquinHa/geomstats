"""
Product of manifolds.
"""

import geomstats.backend as gs
from geomstats.geometry.manifold import Manifold

# TODO(nina): get rid of for loops
# TODO(nina): unit tests


class ProductManifold(Manifold):
    """Class for a product of manifolds."""

    def __init__(self, manifolds):
        self.manifolds = manifolds
        self.n_manifolds = len(manifolds)
        dimensions = [manifold.dimension for manifold in manifolds]
        super(ProductManifold, self).__init__(
            dimension=sum(dimensions))

    def belongs(self, point):
        """Check if the point belongs to the manifold."""
        belong = [self.manifold[i].belongs(point[i])
                  for i in range(self.n_manifolds)]
        return gs.all(belong)

    def regularize(self, point):
        """
        Regularizes the point's coordinates to the canonical representation
        chosen for this manifold.
        """
        regularize_points = [self.manifold[i].regularize(point[i])
                             for i in range(self.n_manifolds)]
        return regularize_points

    def geodesic(self, initial_point,
                 end_point=None, initial_tangent_vec=None,
                 point_type='vector'):
        """
        Geodesic curve for a product metric seen as the product of the geodesic
        on each space.
        """
        geodesics = gs.asarray([[self.manifold[i].metric.geodesic(
            initial_point,
            end_point=end_point,
            initial_tangent_vec=initial_tangent_vec,
            point_type=point_type)
            for i in range(self.n_manifolds)]])
        return geodesics
