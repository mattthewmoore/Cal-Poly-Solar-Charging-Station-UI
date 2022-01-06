import time


def get_charge_time(locker):
    return int(time.time() - locker.start_time)


def begin_charging(locker):

    locker.start_time = time.time()

    print("Charging Locker " + str(locker.number))




def stop_charging(locker):
    charge_time = get_charge_time(locker)
    ChargingData.add_data([charge_time, avg_current])



def get_current(locker):
    if locker.number == 1:
        return 10.0
    if locker.number == 2:
        return 20.0
    if locker.number == 3:
        return 30.0
    if locker.number == 4:
        return 40.0
