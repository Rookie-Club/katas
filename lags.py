def check_flys(fly_list):
        return True

def check_gain_max(fly_list):
    fly_gain = []
    fly_gain_max = []

    for fly in fly_list:
        fly_gain.append(fly[-1])
    fly_gain_max = max(fly_gain)
    return fly_gain_max

def check_hours(fly_list):
    flys_compatibility = []
    flys_hours = []
    fly_hours_tmp = []
    index = 0

    for fly in fly_list:
        fly_begin = fly_list[index][1]
        fly_ending = fly_list[index][1] + fly_list[index][2]
        fly_hours_tmp.append(fly_begin)
        fly_hours_tmp.append(fly_ending)
        flys_hours.append(fly_hours_tmp)
        fly_hours_tmp = []
        index += 1
    return flys_hours

def check_compatibility(fly_list):
    flys_hours = check_hours(fly_list)
    fly_compatibility = []
    fly_compatibility_tmp = [0]
    base = flys_hours[0][1]
    index = 1

    for fly in flys_hours:
        if flys_hours[index][0] >= base:
            fly_compatibility_tmp.append(index)
            base = flys_hours[index][1]
        else:
            flys_hours.remove(flys_hours[0])
            fly_compatibility.append(fly_compatibility_tmp)
            index += 1

    return fly_compatibility
