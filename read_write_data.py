from pandas import DataFrame, read_csv


def add_data(charge_time, avg_current):
    data = DataFrame({'ChargingTime': [int(charge_time)]
                     , 'AverageCurrent': [float(avg_current)]})
    data.to_csv('charge_data.csv', mode='a', index=False, header=False)


def get_avg_current():
    df = read_csv('charge_data.csv')
    avg_current = 0
    for column in range(len(df)):
        current = float(df['AverageCurrent'][column])
        avg_current += current
    avg_current = avg_current / (len(df))
    return round(avg_current, 2)


def get_time_hours():
    df = read_csv('charge_data.csv')
    total_time = 0
    for column in range(len(df)):
        time = df['ChargingTime'][column]
        total_time += time
    print(total_time)
    return round(total_time/3600.0, 2)
