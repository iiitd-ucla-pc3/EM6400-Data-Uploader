

def normalize(power_series,voltage_series):
    normalized_series=[0]*len(power_series)
    for i in range(0,len(power_series)):
        normalization_factor=(230/voltage_series[i])**2
        normalized_series[i]=normalization_factor*power_series[i]
    return normalized_series
        