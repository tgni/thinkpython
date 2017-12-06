def swap_age(age):
    if age < 100:
        s = str(age).zfill(2)
        return int(s[1] + s[0])
    else:
        s = str(age).zfill(3)
        return int(s[2] + s[1] + s[0])

me_age  = 1
mom_age = 73 - 37 + 1
while mom_age <= 200:
    if swap_age(me_age) == mom_age:
        print 'me age is', me_age
    me_age += 1
    mom_age += 1

print 'done'
