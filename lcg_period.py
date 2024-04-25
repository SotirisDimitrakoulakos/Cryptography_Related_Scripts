x0 = 14
a = 193
b = 78
m = 1337

def period (lgc):
    y = (lgc["a"]*lgc["x"]+lgc["b"])%lgc["m"]
    if y in val_ls:
        return
    val_ls.append(y)
    print(y)
    l_temp = {"x": y, "a": a, "b": b, "m": m}
    period(l_temp)


val_ls = []
LGC = {"x": x0, "a": a, "b": b, "m": m}

period(LGC)
per_num = len(val_ls)

print("\nPeriod: " + str(per_num) + " distinct values")


