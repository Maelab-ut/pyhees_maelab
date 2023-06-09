# ============================================================================
# 第四章 暖冷房設備
# 第六節 電気蓄熱暖房器
# Ver.04（エネルギー消費性能計算プログラム（住宅版）Ver.02～）
# ============================================================================

import numpy as np
from pyhees.section4_1_Q import get_Q_T_H_d_t_i


# ============================================================================
# 5. 最大暖房出力
# ============================================================================

def get_Q_max_H_d_t(q_rtd_H):
    """最大暖房出力

    Args:
      q_rtd_H(float): 定格暖房能力

    Returns:
      ndarray: 最大暖房出力

    """
    return np.ones(24 * 365) * (q_rtd_H * 3600 / 1000000)  # (1)


# ============================================================================
# 6. 暖房エネルギー消費量
# ============================================================================

def calc_E_E_H_d_t(q_rtd_H, e_rtd_H, L_H_d_t):
    """暖房エネルギー消費量

    Args:
      q_rtd_H(float): 定格暖房能力
      e_rtd_H(float): 定格暖房エネルギー消費効率
      L_H_d_t(ndarray): 暖冷房区画の１時間当たりの暖房負荷

    Returns:
      ndarray: 暖房エネルギー消費量

    """
    # 最大暖房出力
    Q_max_H_d_t = get_Q_max_H_d_t(q_rtd_H)

    # 処理暖房負荷
    Q_T_H_d_t = get_Q_T_H_d_t_i(Q_max_H_d_t, L_H_d_t)

    return Q_T_H_d_t * (1.0 / e_rtd_H) * 1000 / 3600  # (2)


def calc_Q_UT_H_d_t(q_rtd_H, e_rtd_H, L_H_d_t):
    """処理暖房負荷

    Args:
      q_rtd_H(float): 定格暖房能力
      e_rtd_H(float): 定格暖房エネルギー消費効率
      L_H_d_t(ndarray): 暖冷房区画の１時間当たりの暖房負荷

    Returns:
      ndarray: 処理暖房負荷

    """
    # 最大暖房出力
    Q_max_H_d_t = get_Q_max_H_d_t(q_rtd_H)

    # 処理暖房負荷
    Q_T_H_d_t = get_Q_T_H_d_t_i(Q_max_H_d_t, L_H_d_t)

    return L_H_d_t - Q_T_H_d_t


# ============================================================================
# 6.2 ガス消費量
# ============================================================================

def get_E_G_H_d_t():
    """ガス消費量

    Args:

    Returns:
      ndarray: ガス消費量

    """
    return np.zeros(24 * 365)


# ============================================================================
# 6.3 灯油消費量
# ============================================================================

def get_E_K_H_d_t():
    """灯油消費量

    Args:

    Returns:
      ndarray: 灯油消費量

    """
    return np.zeros(24 * 365)


# ============================================================================
# 6.4 その他の燃料による一次エネルギー消費量
# ============================================================================

def get_E_M_H_d_t():
    """その他の燃料による一次エネルギー消費量

    Args:

    Returns:
      ndarray: その他の燃料による一次エネルギー消費量

    """
    return np.zeros(24 * 365)


if __name__ == '__main__':
    # ダミー負荷
    L_H_d_t = np.ones(24 * 365) * 12

    # 設定値
    q_rtd_H = 15.0
    e_rtd_H = 0.75

    # FF暖房
    E_E_H_d_t = calc_E_E_H_d_t(
        q_rtd_H=q_rtd_H,
        e_rtd_H=e_rtd_H,
        L_H_d_t=L_H_d_t
    )
    E_G_H_d_t = get_E_G_H_d_t()
    E_K_H_d_t = get_E_K_H_d_t()
    E_M_H_d_t = get_E_M_H_d_t()
    print('E_E_H = {} '.format(np.sum(E_E_H_d_t)))
    print('E_G_H = {} '.format(np.sum(E_G_H_d_t)))
    print('E_K_H = {} '.format(np.sum(E_K_H_d_t)))
    print('E_M_H = {} '.format(np.sum(E_M_H_d_t)))
