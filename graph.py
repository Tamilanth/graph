import matplotlib.pyplot as plt

def graph(function, x, y, fd = "", sd = ""):
    l = 0
    z = x
    del x
    i,fdv, xval, sdv= [] ,[],[],[]
    xin = 0.01
    for k in range(z,y):
       for n in range(99):
           l += xin
           xval.append(k + l)
       l = 0.00
    for x in xval:
        i.append(eval(function))
        if (fd != ""):
            fdv.append(eval(fd))
        if (sd != ""):
            sdv.append(eval(sd))
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.plot(xval,i, label= 'Function')
    if (fd != ""):
        plt.plot(xval,fd, label = '1st Derivative')
    if (fd != ""):
        plt.plot(xval,sd, label = '2nd Derivative')
    plt.legend()
    plt.show()
