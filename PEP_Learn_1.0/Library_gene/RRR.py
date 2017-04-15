
a = "MGSSHHHHHHSSGLVPRGSHMARVTLVLRYAARSDRGLVRANNEDSVYAGARLLALADGMGGHAAGEVASQLVIAALAHLDDDEPGGDLLAKLDAAVRAGNSAIAAQVEMEPDLEGMGTTLTAILFAGNRLGLVHIGDSRGYLLRDGELTQITKDDTFVQTLVDEGRITPEEAHSHPQRSLIMRALTGHEVEPTLTMREARAGDRYLLCSDGLSDPVSDETILEALQIPEVAESAHRLIELALRGGGPDNVTVVVADVVD"

    
import sys

def frg_gen(ofs, fs):

    frg_list = []

    if ofs > fs:
        print "Offset count be greater then frg size"
        sys.exit()

    else:
        pass
    for i in range(0,len(a)):

        n = 0
        i = (n+i)*ofs
        e = i+fs
        if e < len(a):
            frg_list.append(a[i:e])
            #print i, e
    print len(frg_list)
    print frg_list


frg_gen(5, 9)
