with open('dataset_24465_4.txt') as i, open('output.txt', 'w') as o:
    z = []
    for line in i:
        z.append(line.rstrip())
    z.reverse()
    contents = '\n'.join(z)
    o.write(contents)
