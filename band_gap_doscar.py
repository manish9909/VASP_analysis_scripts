def get_bandgap(location,tol):
    doscar = open(location)
#     print(doscar)
    for i in range(6):
        l=doscar.readline()
    efermi = float(l.split()[3])
    step1 = doscar.readline().split()[0]
    step2 = doscar.readline().split()[0]
    step_size = float(step2)-float(step1)
    not_found = True
    while not_found:
        l = doscar.readline().split()
#         print(l)
        e = float(l.pop(0))
#         print(e)
        dens = 0
        for i in range(int(len(l)/2)):
            dens += float(l[i])
        if e < efermi and dens > tol:
            bot = e
        elif e > efermi and dens > tol:
            top = e
            not_found = False
    if top - bot < step_size*2:
        return 0,0,0
    else:
        #return top - bot,bot-efermi,top-efermi
        return top - bot,bot,top
