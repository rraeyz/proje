import csv, math
W = {  # Wang+2024 Table 3, 5-sigma: Pdot ms/yr, err, N_lit, N_tess
"CoRoT-2 b":(-21.65,2.96,118,5),"HAT-P-37 b":(-34.29,6.67,27,8),"KELT-16 b":(-27.82,4.76,46,65),
"TrES-1 b":(-14.82,2.37,41,34),"TrES-5 b":(-9.71,2.11,55,66),"WASP-4 b":(-6.43,0.56,75,47),
"WASP-10 b":(-27.74,3.49,41,8),"WASP-12 b":(-30.19,0.92,107,82),"WASP-22 b":(-71.76,17.12,11,5),
"WASP-45 b":(-169.21,21.09,10,14),"XO-4 b":(-62.57,17.48,21,16),"HAT-P-7 b":(18.28,4.05,11,66),
"WASP-1 b":(22.50,5.23,36,9),"WASP-46 b":(51.68,2.86,54,32)}
MJ,MS,RS,AU,c,yr=1.898e27,1.989e30,6.957e8,1.496e11,2.998e8,3.15576e7
lat=39.9  # Erzurum
print(f"{'gezegen':11s} {'P':>6s} {'V':>5s} {'Dec':>6s} {'hmax':>5s} {'R*/a':>6s} {'Tpot':>8s} {'Pdot':>8s} {'S/N':>5s} {'Q_ima':>9s} {'Pdot(Q=1e6)':>11s} {'RV_gerek':>9s} {'N':>4s} {'Ntess':>5s}")
for r in csv.DictReader(open('p14.csv')):
    n=r['pl_name']; P=float(r['pl_orbper']); Mp=float(r['pl_bmassj'])*MJ; Ms=float(r['st_mass'])*MS
    Rs=float(r['st_rad'])*RS; a=float(r['pl_orbsmax'])*AU; V=float(r['sy_vmag']); dec=float(r['dec'])
    q=Mp/Ms; x=Rs/a; T=q*x**5
    pd,pe,nl,nt=W[n]; pdl=pd*1e-3/yr
    Qimp = -(27*math.pi/2)*T/pdl if pd<0 else float('nan')
    pd6 = -(27*math.pi/2)*T/1e6*yr*1e3
    rv = c*pdl/(P*86400)*86400  # m/s/day
    hmax=90-abs(lat-dec)
    print(f"{n:11s} {P:6.3f} {V:5.2f} {dec:6.1f} {hmax:5.0f} {x:6.3f} {T*1e8:8.2f} {pd:8.2f} {abs(pd)/pe:5.1f} {Qimp:9.2e} {pd6:11.2f} {rv:9.3f} {nl+nt:4d} {nt:5d}")
print("Tpot = (Mp/M*)(R*/a)^5 x1e8; Q_ima: Wang Pdot'u gelgitle aciklamak icin gereken Q'*; RV_gerek: Romer ile aciklamak icin gereken dv/dt (m/s/gun); hmax: Erzurum'dan max yukseklik (derece)")
