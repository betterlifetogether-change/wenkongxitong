def calculate_water_ratio(cold_temp, hot_temp, target_temp, total_volume):
    """
    计算混合到目标温度所需的冷热水体积比例

    参数:
    cold_temp (float): 冷水温度 (°C)
    hot_temp (float): 热水温度 (°C)
    target_temp (float): 目标混合温度 (°C)
    total_volume (float): 最终混合体积 (mL)

    返回:
    tuple: (冷水体积, 热水体积, 冷热比例)
    """
    # 温度有效性检查
    if target_temp <= cold_temp or target_temp >= hot_temp:
        raise ValueError("目标温度必须介于冷水和热水温度之间")
    if cold_temp >= hot_temp:
        raise ValueError("热水温度必须高于冷水温度")

    # 计算温度差值
    delta_total = hot_temp - cold_temp
    delta_cold = target_temp - cold_temp
    delta_hot = hot_temp - target_temp

    # 计算体积比例
    hot_volume = total_volume * delta_cold / delta_total
    cold_volume = total_volume - hot_volume

    # 计算比例（冷水:热水）
    ratio = cold_volume / hot_volume

    return (cold_volume, hot_volume, ratio)


# 示例使用
if __name__ == "__main__":
    try:
        # 输入参数
        cold = 20.0  # 冷水温度
        hot = 80.0  # 热水温度
        target = 40.0  # 目标温度
        total = 500.0  # 总混合体积

        # 调用函数
        cold_vol, hot_vol, ratio = calculate_water_ratio(cold, hot, target, total)

        # 输出结果
        print(f"输入参数:")
        print(f"冷水温度: {cold}°C")
        print(f"热水温度: {hot}°C")
        print(f"目标温度: {target}°C")
        print(f"总混合体积: {total} mL")

        print("\n计算结果:")
        print(f"需要冷水: {cold_vol:.2f} mL")
        print(f"需要热水: {hot_vol:.2f} mL")
        print(f"冷热比例: 1:{ratio:.2f} (冷水:热水)")

    except ValueError as e:
        print(f"错误: {e}")