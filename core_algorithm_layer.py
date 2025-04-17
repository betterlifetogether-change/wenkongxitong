class ThermodynamicsModel:
    def calculate_flow_ratio(self,T_hot,T_cold,T_target,hot_ratio,cold_ratio):
        rho_hot=1000-0.0178*pow(T_hot,1.5)
        rho_cold=1000-0.0178*pow(T_cold,1.5)
        Qh=(T_target-T_cold)/(T_hot-T_cold)
        Qc=1-Qh

        k=(rho_cold/rho_hot)^0.5
        hot_ratio=Qh/(Qh+Qc*k)
        cold_ratio=1-hot_ratio
        return hot_ratio,cold_ratio
