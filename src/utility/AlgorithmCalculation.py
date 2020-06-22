class AlgorithmCalculation:
    @staticmethod
    def green_light_duration(historical_data, z=30, min_green_light=15):
        return (1 + historical_data) * (z - min_green_light) + min_green_light

    @staticmethod
    def historical_data(weights, historical_array_info):
        return sum(list(map(lambda weight, historical: weight * historical, weights, historical_array_info)))


