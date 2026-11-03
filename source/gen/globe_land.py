"""Dot-globe land points (lat, lon, region) for Act 5. Regions: 0 land, 1 India, 2 GCC, 3 Europe, 4 US."""
import math, json
from global_land_mask import globe
IND=[(68.2,23.6),(70.2,20.9),(72.6,21.4),(73,17),(74.5,13),(76.5,8.1),(78,8.3),(80.2,13),(80.3,15.8),(82.3,17),(85,19.5),(87,21.5),(88.8,22),(89,26.2),(92,25),(97,28),(95.5,29),(91.5,27.8),(88.2,27.8),(88,26.5),(85,27.3),(81,30.3),(79,32.5),(78,35.5),(74.5,37),(73.8,34.5),(74.6,32.5),(73.8,30.5),(71,27.9),(70,25.8),(69.5,24.3)]
def pip(x,y,P):
    c=False
    for i in range(len(P)):
        x1,y1=P[i];x2,y2=P[i-1]
        if (y1>y)!=(y2>y) and x<(x2-x1)*(y-y1)/(y2-y1)+x1:c=not c
    return c
def region(la,lo):
    if pip(lo,la,IND):return 1
    if 16.5<=la<=30.2 and lo<=60 and lo>35+(28-la)*.55 and not(lo>=50 and la>26.6) and not(la>29.3 and lo<46.5):return 2
    if (-10<=lo<=24 and 36<=la<=70) or (21<=lo<=30 and 54<=la<=70) or (20<=lo<=29.5 and 41<=la<=48.3):
        if not(la<37.2 and lo>-6 and lo<12) and not(lo>26 and la<42):return 3
    if 25<=la<=49 and -125<=lo<=-67:return 4
    return 0
def build(step=2.3):
    out=[];la=-56.0
    while la<=78:
        n=max(1,int(round(360*math.cos(math.radians(la))/step)));off=(int(la/step)%2)*.5
        for k in range(n):
            lo=-180+(k+off)*360/n
            if globe.is_land(la,lo):out+=[round(la*10),round(lo*10),region(la,lo)]
        la+=step
    return out
if __name__=='__main__':
    d=build();print(len(d)//3,[sum(1 for i in range(2,len(d),3) if d[i]==g) for g in range(5)])
    json.dump(d,open('globe_land.json','w'),separators=(',',':'))
