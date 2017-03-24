

def check_fly(fly_list):
    if (fly_list == []):
        return None
    else:
        return True

def check_max_gain(fly_list):
    gain_max = 0
    gain_list = []

    for fly in fly_list:
        gain_list.append(fly[-1])
    gain_max = max(gain_list)
    return gain_max

def check_hours(fly_list):
    fly_begin = []
    fly_ending = []
    fly_hours = []

    for fly in fly_list:
        fly_begin.append(fly[1])
        fly_ending.append(fly[1] + fly[2])
        fly_hours.append(fly_begin, fly_ending)
    return fly_hours

def check_fly_compatibility(fly_list, fly_hours):
    compatibility_list = []

    for fly in fly_hours:
        if fly[0][0] > fly[1][-1]:
            compatibility_list.append(fly_list[0], fly_list[1])
    return compatibility_list
