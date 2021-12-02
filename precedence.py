'''
using BUDMAS/BODMAS
U REFERS TO UTINARY FUNCTION IE i++ i-- ARE NOT INPYTHON
1024 512 256 128 64 32 16 8 4 2 1
0     0   0   0  0  0   0 1 0 0 0 >>8
1024 512 256 128 64 32 16 8 4 2 1
0     0   0   0   0  0  0 0 1 0 0  >>4
0     0   0   0   0  0  1 0 0 0 0  >> ans 16(4<<2)
0     0   0   0   0  0  0 1 1 0 0  >>| 12

'''


alpha=8
beta=4
gamma=(alpha|beta)/((alpha*2)*beta<<2)
#      (12)/(16*16)
#12/256
print(gamma)

