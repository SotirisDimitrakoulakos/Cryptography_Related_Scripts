def z_generators(np):
    gens = []
    for i in set(range(1, np)):
        nl = set()
        for j in set(range(1, np)):
            n = (i**j) % np
            nl.add(n)
        if nl == elems:
            gens.append(i)
    return gens


for p in [691, 1009, 182980571794372947622904898662364989219257159219670110553071607284160744200112117607405683]:
    elems = set(range(1, p))
    z_gens = z_generators(p)
    print(f"\n\nGenerators of p={p} are:\n"+str(z_gens)+"\n\n")
