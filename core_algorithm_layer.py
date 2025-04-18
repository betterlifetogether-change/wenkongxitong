import math

class ThermodynamicsModel:
    def calculate_flow_ratio(self,T_hot,T_cold,T_target,Q_total):
        delta_total = T_hot - T_cold
        delta_cold = T_target-T_cold
        delta_hot = T_hot-T_target
        hot_ratio = Q_total*delta_cold/delta_total
        cold_ratio = Q_total*delta_hot/delta_total
        return hot_ratio,cold_ratio

class ValveOpening:
    def water_volume(self,Q_total,T_hot,T_cold,T_target):
        TM=ThermodynamicsModel()
        Q_hot,Q_cold=TM.calculate_flow_ratio(T_hot,T_cold,T_target,Q_total)
        return Q_hot,Q_cold

    def pressure_diff_calculation(self,P_hot_initial,P_cold_initial,P_end):
        P_hot=P_hot_initial-P_end
        P_cold=P_cold_initial-P_end
        return P_hot,P_cold

    def diff_temp_rou(self,T_hot,T_cold):
        # 后期需要调用freesteam库进行精确计算
        # 常压下
        rou_hot=((999.8396+16.945176*T_hot)-(7.9870401*0.001*pow(T_hot,2)))/(1+16.879850*0.001*T_hot)
        rou_cold = ((999.8396 + 16.945176 * T_cold) - (7.9870401 * 0.001 * pow(T_cold, 2))) / (
                    1 + 16.879850 * 0.001 * T_cold)
        return rou_hot,rou_cold

    def cross_sectional_area_percentage(self,P_hot,P_cold,K_hot,rou_hot,Q_hot,K_cold,rou_cold,Q_cold):
        A_hot=Q_hot/(K_hot*math.sqrt(2*P_hot/rou_hot))
        A_cold=Q_cold/(K_cold*math.sqrt(2*P_cold/rou_cold))
        return A_hot,A_cold