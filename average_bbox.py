def avgbndbox(filename):
    file=open(filename,"r")
    xmin=0
    ymin=0
    xmax=0
    ymax=0
    counter=0
    while True:
        line = file.readline()
        if not line:
            break
        if line.find("<bndbox>")!=-1:
            temp=int(file.readline().strip("<xmin>/ \t\n"))
            xmin=xmin+temp
            temp=int(file.readline().strip("<ymin>/ \t\n"))
            ymin=ymin+temp
            temp=int(file.readline().strip("<xmax>/ \t\n"))
            xmax=xmax+temp
            temp=int(file.readline().strip("<ymax>/ \t\n"))
            ymax=ymax+temp
            counter=counter+1
    file.close()        
    avgwidth=int((xmax)-(xmin)/counter)
    avgheight=int((ymax)-(ymin)/counter)
    return avgwidth,avgheight

avgwidth,avgheight=avgbndbox("/home/sahil/000002.xml")

print("average width: {}".format(avgwidth))
print("average height: {}".format(avgheight))




