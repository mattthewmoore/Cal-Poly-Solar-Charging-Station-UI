import pandas as pd


def get_file_name(locker_num):
    if locker_num == 1:
        return "current_locker1.csv"
    elif locker_num == 2:
        return "current_locker2.csv"
    elif locker_num == 3:
        return "current_locker3.csv"
    elif locker_num == 4:
        return "current_locker4.csv"


def get_avg_current(locker_num):
    locker_file = get_file_name(locker_num)
    df = pd.read_csv(locker_file)
    avg_current = 0
    for column in range(len(df)):
        current = float(df['Current'][column])
        avg_current += current
    avg_current = avg_current / (len(df))
    return round(avg_current, 2)


def add_current_val(current, locker_num):
    locker_file = get_file_name(locker_num)
    current_val = pd.DataFrame({'Current': [float(current)]})
    current_val.to_csv(locker_file, mode='a', index=False, header=False)


def clear_data(locker_num):
    locker_file = get_file_name(locker_num)
    df = pd.read_csv(locker_file)
    row_list = []
    for x in range(len(df)):
        row_list.append(x)
    df2 = df.drop(row_list)
    df2.to_csv(locker_file, index=False)






