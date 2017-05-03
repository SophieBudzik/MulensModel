import numpy as np

import MulensModel
from MulensModel.caustics import Caustics


MODULE_PATH = "/".join(MulensModel.__file__.split("/source")[:-1])

SAMPLE_FILE_01 = MODULE_PATH + "/data/MB11293_caustics.dat"

test_caustics = np.genfromtxt(SAMPLE_FILE_01, names=['X', 'Y'], dtype=None)


def test_caustic():
    s = 0.548
    q = 0.0053

    caustics = Caustics(q=q, s=s)
    
    x, y = caustics.get_caustics(n_points=1000)
    for i in range(0, len(x), 100):
        index = np.argmin(
            np.sqrt((test_caustics['X']-x[i])**2+(test_caustics['Y']-y[i])**2))
        np.testing.assert_almost_equal(
            x[i], test_caustics['X'][index], decimal=5)
        np.testing.assert_almost_equal(
            y[i], test_caustics['Y'][index], decimal=5)

