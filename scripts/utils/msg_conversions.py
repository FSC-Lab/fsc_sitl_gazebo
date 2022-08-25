# Copyright (c) 2022 hs293go
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import numpy as np


def components_to_array(msg):
    components = "xyzw" if hasattr(msg, "w") else "xyz"
    return np.array([getattr(msg, component) for component in components])


def array_to_components(arr, data_class):
    components = "xyzw" if hasattr(data_class, "w") else "xyz"
    return data_class(**dict(zip(components, arr)))
