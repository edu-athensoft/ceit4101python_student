"""

"""
import tuit_190921.day20_200411.myconst as const
# formula

# 1.length
# 1.1 km to mile
def km_2_mile(x):
    result = x / const.KM_MILE
    return result

# 1.2 mile to km
def mile_2_km(x):
    result = x * const.MILE_KM
    return result

# 1.3 m to cm
def m_2_cm(x):
    result = x * 100
    return result

# 1.4 cm to m
def cm_2_m(x):
    result = x / 100
    return result

# 2.Temp
# 2.1 c to f
def c_2_f(x):
    return -99

# 2.2 c to f
def f_2_c(x):
    return -99

# mass
# 3.1 kg to pound
def kg_2_pound(x):
    return -99

# 3.2 pound to kg
def pound_2_kg(x):
    return -99


# 4. Area
# 4.1 sqrft to sqrm
def sqrft_2_sqrm(x):
    return -99

# 4.2 sqrm to sqrft
def sqrm_2_sqrft(x):
    return -99



# level 1 options
def select_mtype():
    print("Please select a measure type")
    print("[1]Length")
    print("[2]Temp.")
    print("[3]Mass")
    print("[4]Area")
    mtype = input("[1,2,3,4]: ")
    return mtype

# level 2 options
def select_ctype(mtype):
    print()
    ctype = ''
    if mtype == '1':
        print("select level 2 options of {}".format(mtype))
        print("[1]km to mile")
        print("[2]mile to km")
        print("[3]m to cm")
        print("[4]cm to m")
        ctype = input("[1,2,3,4]")
    elif mtype == '2':
        print("select level 2 options of {}".format(mtype))
        print("[1]c to f")
        print("[2]f to c")
        ctype = input("[1,2]")
    elif mtype == '3':
        print("select level 2 options of {}".format(mtype))
        print("[1]kg to pound")
        print("[2]pound to kg")
        ctype = input("[1,2]")
    elif mtype == '4':
        print("select level 2 options of {}".format(mtype))
        print("[1]sqr ft to sqr m")
        print("[2]sqr m to sqr ft")
        ctype = input("[1,2]")
    else:
        print("Invalid ctypes!")
    return ctype

def get_number():
    return float(input("Please input your number:"))



# main program
# select mtype for level 1
mtype = select_mtype()
# print("mtype = {}".format(mtype))

# select ctype for level 2
ctype = ''
number = 0
result = 0

if mtype == '1':
    ctype = select_ctype(mtype)
    number = get_number()
    if ctype == '1':
        result = km_2_mile(number)
    elif ctype == '2':
        result = mile_2_km()
    elif ctype == '3':
        result = m_2_cm(number)
    elif ctype == '4':
        result = cm_2_m(number)
    else:
        pass

elif mtype == '2':
    ctype = select_ctype(mtype)
    number = get_number()
    if ctype == '1':
        result = c_2_f(number)
    elif ctype == '2':
        result = f_2_c(number)
    else:
        pass

elif mtype == '3':
    ctype = select_ctype(mtype)
    number = get_number()
    if ctype == '1':
        result = kg_2_pound(number)
    elif ctype == '2':
        result = pound_2_kg(number)
    else:
        pass

elif mtype == '4':
    ctype = select_ctype(mtype)
    number = get_number()
    if ctype == '1':
        result = sqrft_2_sqrm(number)
    elif ctype == '2':
        result = sqrm_2_sqrft(number)
    else:
        pass

else:
    print("Invalid mtypes!")

print("Your result is {}".format(result))





"""
# test 1.1
length_1 = 1
print(km_2_mile(length_1))

# test 1.2
length_2 = 1
print(mile_2_km(length_2))

# test 1.3
length_3 = 1
print(m_2_cm(length_3))
"""