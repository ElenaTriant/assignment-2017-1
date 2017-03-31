names = "graph_1.txt"
final = []
g = {}
c = False

with open(names) as alpha_beta:
    for line in alpha_beta:
        part = line.strip()
        l = part.split(' ')
        final.append(l)

        if l[0] not in g:
            g[l[0]] = []
        if l[1] not in g:
            g[l[1]] = []

        g[l[0]].append(l[1])

f = sorted(final)
gr = sorted(g)

days = []

for i in range(len(f)):
    pair = f[i]
    x = pair[0]
    y = pair[1]

    for a in gr:
        if c == False:
            days[0].append(a)
            c = True
        for b in range(len(gr)):
            for d in days:
            #print ("OK")
                if a not in range(len(days)):
                    if b not in range(len(days)):
                        days[d].append(a)
                        days[d].append(b)
                        print ("(", a, ",", b, ")", d)
