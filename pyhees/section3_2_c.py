# ============================================================================
# 付録C 方位係数
# ============================================================================

# ※屋根の面する方位については、勾配の有無に関わらず上面に面するものとして取扱うこと


def get_nu_boundary():
    """界壁及び界床の方位係数 (-)

    Args:

    Returns:
      float: 界壁及び界床の方位係数 (-)

    """
    return 0.0


def get_nu_H(region, direction):
    """外皮の部位の暖房期の方位係数

    Args:
      region(int): 省エネルギー地域区分
      direction(str): 外皮の部位の方位

    Returns:
      float: 外皮の部位の暖房期の方位係数

    """

    # 表1 暖房期の方位係数
    table_1 = {
        '上面': (1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, None),
        '北': (0.260, 0.263, 0.284, 0.256, 0.238, 0.261, 0.227, None),
        '北東': (0.333, 0.341, 0.348, 0.330, 0.310, 0.325, 0.281, None),
        '東': (0.564, 0.554, 0.540, 0.531, 0.568, 0.579, 0.543, None),
        '南東': (0.823, 0.766, 0.751, 0.724, 0.846, 0.833, 0.843, None),
        '南': (0.935, 0.856, 0.851, 0.815, 0.983, 0.936, 1.023, None),
        '南西': (0.790, 0.753, 0.750, 0.723, 0.815, 0.763, 0.848, None),
        '西': (0.535, 0.544, 0.542, 0.527, 0.538, 0.523, 0.548, None),
        '北西': (0.325, 0.341, 0.351, 0.326, 0.297, 0.317, 0.284, None),
        '下面': (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, None),
    }
    return table_1[direction][region - 1]


def get_nu_C(region, direction):
    """外皮の部位の冷房期の方位係数

    Args:
      region(int): 省エネルギー地域区分
      direction(str): 外皮の部位の方位

    Returns:
      f: 外皮の部位の冷房期の方位係数

    """

    # 表2 冷房期の方位係数
    table_2 = {
        '上面': (1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0),
        '北': (0.329, 0.341, 0.335, 0.322, 0.373, 0.341, 0.307, 0.325),
        '北東': (0.430, 0.412, 0.390, 0.426, 0.437, 0.431, 0.415, 0.414),
        '東': (0.545, 0.503, 0.468, 0.518, 0.500, 0.512, 0.509, 0.515),
        '南東': (0.560, 0.527, 0.487, 0.508, 0.500, 0.498, 0.490, 0.528),
        '南': (0.502, 0.507, 0.476, 0.437, 0.472, 0.434, 0.412, 0.480),
        '南西': (0.526, 0.548, 0.550, 0.481, 0.520, 0.491, 0.479, 0.517),
        '西': (0.508, 0.529, 0.553, 0.481, 0.518, 0.504, 0.495, 0.505),
        '北西': (0.411, 0.428, 0.447, 0.401, 0.442, 0.427, 0.406, 0.411),
        '下面': (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
    }
    return table_2[direction][region - 1]
