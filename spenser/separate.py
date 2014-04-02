with open('spense', 'r') as f:
    inpoem = False
    pnum = 1
    for line in f:
        print line
        if inpoem and len(line.split()) < 2:
            inpoem = False
            pfile.close()
            continue
        if len(line.split()) < 2:
            continue

        # assume in a new poem
        if not inpoem:
            inpoem = True
            pfile = open('spense{}'.format(pnum), 'w')
            pnum += 1
        pfile.write(line)
    pfile.close()

