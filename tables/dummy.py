

class SampleClass(object):

    """
    Draw samples from a multivariate normal distribution.

    The multivariate normal, multinormal or Gaussian distribution is a
    generalisation of the one-dimensional normal distribution to higher
    dimensions.

    Such a distribution is specified by its mean and covariance matrix,
    which are analogous to the mean (average or "centre") and variance
    (standard deviation squared or "width") of the one-dimensional normal
    distribution.

    Parameters
    ----------
    mean : (N,) ndarray
        Mean of the N-dimensional distribution.
    cov : (N,N) ndarray
        Covariance matrix of the distribution.
    shape : tuple of ints, optional
        Given a shape of, for example, (m,n,k), m*n*k samples are
        generated, and packed in an m-by-n-by-k arrangement.  Because each
        sample is N-dimensional, the output shape is (m,n,k,N).  If no
        shape is specified, a single sample is returned.

    Returns
    -------
    out : ndarray
        The drawn samples, arranged according to `shape`.  If the
        shape given is (m,n,...), then the shape of `out` is is
        (m,n,...,N).

        In other words, each entry ``out[i,j,...,:]`` is an N-dimensional
        value drawn from the distribution.

    See Also
    --------
    normal
    scipy.stats.distributions.norm : Provides random variates, as well as
                                     probability density function, cumulative
                                     density function, etc.

    Notes
    -----
    The mean is a coordinate in N-dimensional space, which represents the
    location where samples are most likely to be generated.  This is
    analogous to the peak of the bell curve for the one-dimensional or
    univariate normal distribution.

    Covariance indicates the level to which two variables vary together.
    From the multivariate normal distribution, we draw N-dimensional
    samples, :math:`X = [x_1, x_2, ... x_N]`.  The covariance matrix
    element :math:`C_ij` is the covariance of :math:`x_i` and :math:`x_j`.
    The element :math:`C_ii` is the variance of :math:`x_i` (i.e. its
    "spread").

    Instead of specifying the full covariance matrix, popular
    approximations include:

      - Spherical covariance (`cov` is a multiple of the identity matrix)
      - Diagonal covariance (`cov` has non-negative elements, and only on
        the diagonal)

    This geometrical property can be seen in two dimensions by plotting
    generated data-points:

    >>> mean = [0,0]
    >>> cov = [[1,0],[0,100]] # diagonal covariance, points lie on x or y-axis
    >>> x,y = np.random.multivariate_normal(mean,cov,5000).T

    >>> import matplotlib.pyplot as plt
    >>> plt.plot(x,y,'x'); plt.axis('equal'); pyplot.show()

    Note that the covariance matrix must be non-negative definite.
    """
    def __init__(self, filename, mode="r", title="",
                 rootUEP="/", filters=None, **kwargs):

        #: the filename
        self.filename = filename

        #: the mode
        self.mode = mode

    def method1(self, arg1, arg2):
        """Method description.

        Parameters
        ----------
        arg1 : int
        arg2 : float

        """
        pass

    def method2(self, arg3, arg4):
        """Method 2 description.

        Parameters
        ----------
        arg3
        arg4
        """
