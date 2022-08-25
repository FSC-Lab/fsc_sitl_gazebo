# Copyright (c) 2022 hs293go
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import numpy as np

# pylint: disable=invalid-name


def quaternion_to_rotation_matrix(q):
    [x, y, z, w] = q
    tx = 2 * x
    ty = 2 * y
    tz = 2 * z
    twx = tx * w
    twy = ty * w
    twz = tz * w
    txx = tx * x
    txy = ty * x
    txz = tz * x
    tyy = ty * y
    tyz = tz * y
    tzz = tz * z

    res = np.empty((3, 3))
    res[0, 0] = 1.0 - (tyy + tzz)
    res[0, 1] = txy - twz
    res[0, 2] = txz + twy
    res[1, 0] = txy + twz
    res[1, 1] = 1.0 - (txx + tzz)
    res[1, 2] = tyz - twx
    res[2, 0] = txz - twy
    res[2, 1] = tyz + twx
    res[2, 2] = 1.0 - (txx + tyy)


def quaternion_rotate_point(q, v):
    w = q[3]
    vec = q[0:3]
    uv = np.cross(vec, v)
    uv += uv
    return v + w * uv + np.cross(vec, uv)
