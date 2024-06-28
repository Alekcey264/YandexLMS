def future(*masses, **consts):
    pro = 1
    for value in consts.values():
        pro *= value
    if sum(masses) * pro > VIN:
        return "ACCELERATION"
    elif sum(masses) * pro < VIN:
        return "DECELERATION"
    else:
        return "UNCHANGED"

VIN = 540
mass = [1, 2, 3, 4, 5]
const = {'e0': 9, 'mu0': 4}
print(future(*mass, **const))