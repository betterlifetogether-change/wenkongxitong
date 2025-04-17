import math

class ThermodynamicsModel:
    def calculate_flow_ratio(self,T_hot,T_cold,T_target,Q_tatal):
        rho_hot=1000-0.0178*pow(T_hot,1.5)
        rho_cold=1000-0.0178*pow(T_cold,1.5)
        Qh=(T_target-T_cold)/(T_hot-T_cold)
        Qc=1-Qh

        k=math.sqrt(rho_cold/rho_hot)
        hot_ratio=Qh/(Qh+Qc*k)
        cold_ratio=1-hot_ratio
        return hot_ratio,cold_ratio

class ValveOpening:
    def water_volume(self,Q_total,T_hot,T_cold,T_target):
        TM=ThermodynamicsModel
        hot_ratio,cold_ratio=TM.calculate_flow_ratio(T_hot,T_cold,T_target,Q_total)
        Q_hot=Q_total*hot_ratio
        Q_cold=Q_total*cold_ratio
        return Q_hot,Q_cold

    def pressure_diff_calculation(self,P_hot_initial,P_cold_initial,P_end):

    def diff_temp_rou(self,T_hot,T_cold):

    def cross_sectional_area_percentage(self,Q_hot,Q_cold,K_hot,P_hot,rou_hot,K_cold,P_cold,rou_cold):
        A_hot=Q_hot/(K_hot*math.sqrt(2*P_hot/rou_hot))
        A_cold=Q_cold/(K_cold*math.sqrt(2*P_cold/rou_cold))
        return A_hot,A_cold