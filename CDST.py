#*********************************************************#
#CHARGE DENSITY SLICE TOOL (CDST) for VASP output files
#This python program is produced by Jui-Cheng Kao
#From Department of Materials Science and Engineering
#National Yang Ming Chiao Tung University, Hsinchu, Taiwan
#*********************************************************#
#Please feel free if users have any questions.
#Email: jckao.en10@nycu.edu.tw
#2023/03/21
#*********************************************************#

import matplotlib.pyplot as plt
import numpy as np

filename = input("Please input the charge density filename: ")
dist = float(input("Please input the z position you want to slice (crystal coordinate): "))
p_x = int(input("Please input the periodicity along x-direction: "))
p_y = int(input("Please input the periodicity along y-direction: "))

aa= [[],[],[]]
chg = []
with open(filename, mode="r") as f:
    f.readline()
    a = float(f.readline())
    for i in range(3):
        l_vec = f.readline().split()
        for j in range(3):
            aa[i].append(float(l_vec[j]))
    z_len = np.linalg.norm(aa[-1])*a
    element = f.readline().split()
    natoms = f.readline().split()
    f.readline()
    for i in range(len(element)):
        for j in range(int(natoms[i])):
            f.readline()
    f.readline()
    ng = f.readline().split()
    ngx, ngy, ngz = int(ng[0]), int(ng[1]), int(ng[2])
    NG = int(ngx*ngy*ngz)
    for line in f:
        if NG == len(chg):
            break
        ll = line.split()
        for i in range(len(ll)):
            chg.append(float(ll[i]))
chg = np.array(chg)
CHG = chg.reshape((ngz,ngx*ngy))
z_coor = np.arange(0, 1, 1/ngz)*z_len
for zz in range(len(z_coor)):
    if dist <= z_coor[zz]:
        z_inx = zz
        break
frac = (z_coor[zz]-dist)/(z_len/ngz)
new_CHG = CHG[z_inx-1]*frac + CHG[z_inx]*(1-frac)
x, y = np.mgrid[0:1:1/ngx,0:1:1/ngy]

resh_chg = new_CHG.reshape((ngy,ngx)).transpose()

xx, yy = x.reshape((1,ngx*ngy)), y.reshape((1,ngx*ngy))

x1 = np.append(x, x[0]+1)
y1 = np.append(y, y[0])
chg1 = np.append(resh_chg, resh_chg[0])

x2 = x1.reshape((ngx+1,ngy)).transpose()
y2 = y1.reshape((ngx+1,ngy)).transpose()
chg2 = chg1.reshape((ngx+1,ngy)).transpose()

x3 = np.append(x2, x2[0])
y3 = np.append(y2, y2[0]+1)
chg3 = np.append(chg2, chg2[0])

new_xx = np.array([])
new_yy = np.array([])
new_chg = np.array([])

for i in range(p_x):
    for j in range(p_y):
        new_xx = np.append(new_xx, x3+i)
        new_yy = np.append(new_yy, y3+j)
        new_chg = np.append(new_chg, chg3)

trans_xx = new_xx*aa[0][0] + new_yy*aa[1][0]
trans_yy = new_xx*aa[0][1] + new_yy*aa[1][1]

fig = plt.figure(figsize=(15,15))
plt.tricontourf(trans_xx, trans_yy, new_chg, levels=25, cmap='viridis', vmin=0, vmax=1)
#plt.tricontourf(trans_xx, trans_yy, new_chg, levels=25, cmap='viridis', vmin=0, vmax=np.max(new_chg)*0.1)
#plt.tricontourf(trans_xx, trans_yy, new_chg, levels=25, cmap='viridis', vmin=np.min(new_chg), vmax=np.max(new_chg)*0.1)
plt.axis('square')
plt.axis('off')
plt.savefig('CDST.png', transparent=True ,dpi=400)
#plt.show()

