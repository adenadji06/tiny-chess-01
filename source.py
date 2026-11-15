import json,os,urllib.request as u
def P(p,b):
 with u.urlopen(u.Request(os.getenv("MAKEFUN_ENV_URL")+p,json.dumps(b).encode()))as r:return json.load(r)
V=[0,100,320,330,500,900,0]
PA=[0,0,0,0,0,0,0,0,50,50,50,50,50,50,50,50,10,10,20,30,30,20,10,10,5,5,10,25,25,10,5,5,0,0,0,20,20,0,0,0,5,-5,-10,0,0,-10,-5,5,5,10,10,-20,-20,10,10,5,0,0,0,0,0,0,0,0]
NA=[-50,-40,-30,-30,-30,-30,-40,-50,-40,-20,0,0,0,0,-20,-40,-30,0,10,15,15,10,0,-30,-30,5,15,20,20,15,5,-30,-30,0,15,20,20,15,0,-30,-30,5,10,15,15,10,5,-30,-40,-20,0,5,5,0,-20,-40,-50,-40,-30,-30,-30,-30,-40,-50]
BA=[-20,-10,-10,-10,-10,-10,-10,-20,-10,0,0,0,0,0,0,-10,-10,0,5,10,10,5,0,-10,-10,5,5,10,10,5,5,-10,-10,0,10,10,10,10,0,-10,-10,10,10,10,10,10,10,-10,-10,5,0,0,0,0,5,-10,-20,-10,-10,-10,-10,-10,-10,-20]
RA=[0,0,0,0,0,0,0,0,5,10,10,10,10,10,10,5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,-5,0,0,0,0,0,0,-5,0,0,0,5,5,0,0,0]
QA=[-20,-10,-10,-5,-5,-10,-10,-20,-10,0,0,0,0,0,0,-10,-10,0,5,5,5,5,0,-10,-5,0,5,5,5,5,0,-5,0,0,5,5,5,5,0,-5,-10,5,5,5,5,5,0,-10,-10,0,5,0,0,0,0,-10,-20,-10,-10,-5,-5,-10,-10,-20]
KM=[-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-30,-40,-40,-50,-50,-40,-40,-30,-20,-30,-30,-40,-40,-30,-30,-20,-10,-20,-20,-20,-20,-20,-20,-10,20,20,0,0,0,0,20,20,20,30,10,0,0,10,30,20]
KE=[-50,-40,-30,-20,-20,-30,-40,-50,-30,-20,-10,0,0,-10,-20,-30,-30,-10,20,30,30,20,-10,-30,-30,-10,30,40,40,30,-10,-30,-30,-10,30,40,40,30,-10,-30,-30,-10,20,30,30,20,-10,-30,-30,-30,0,0,0,0,-30,-30,-50,-30,-30,-30,-30,-30,-30,-50]
PS=[0,PA,NA,BA,RA,QA,0]
PPB=[0,5,10,20,35,60,100,0]
TOT=6400
B=[0]*128
CC=[15]*128
CC[0],CC[7],CC[4],CC[112],CC[119],CC[116]=13,14,12,7,11,3
BD=[-17,-15,15,17];RD=[-16,-1,1,16];ND=[-33,-31,-18,-14,14,18,31,33];KD=sorted(BD+RD);DT={2:ND,6:KD,3:BD,4:RD,5:BD+RD}
class Z(Exception):pass
N=0;I=-30000;NB=80000
EV=0;NP=0;WB=0;BB=0;WP=set();BP=set()
TT={};KL=[0]*128;TM=0
def L(f):
 global S,C,Y,KW,KB,EV,NP,WB,BB,WP,BP
 p=f.split();B[:]=[0]*128;q=112
 for c in p[0]:
  if c=="/":q-=24
  elif c.isdigit():q+=int(c)
  else:
   v="PNBRQK".index(c.upper())+1;B[q]=v if c.isupper()else-v;q+=1
 S=1-(p[1]<"w")*2;C=sum(1<<"KQkq".index(c)for c in p[2]if c in"KQkq");Y=-1;KW=B.index(6);KB=B.index(-6)
 if p[3]!="-":Y=(int(p[3][1])-1)*16+ord(p[3][0])-97
 EV=0;NP=0;WB=0;BB=0;WP=set();BP=set()
 for q,x in enumerate(B):
  if not x or abs(x)==6:continue
  a=abs(x);f=q&7;r=q>>4;i=(7-r)*8+f if x>0 else r*8+f
  EV+=(V[a]+PS[a][i])*(1 if x>0 else -1)
  if a==1:(WP if x>0 else BP).add(q)
  else:
   NP+=V[a]
   if a==3:
    if x>0:WB+=1
    else:BB+=1
def pv(a,q,s):
 f=q&7;r=q>>4;i=(7-r)*8+f if s>0 else r*8+f
 return PS[a][i]
def A(q,c):
 for D,v in(((-15*c,-17*c),1),(ND,2),(KD,6)):
  for d in D:
   t=q+d
   if not t&136 and B[t]==v*c:return 1
 for d in BD+RD:
  t=q+d
  while not t&136:
   x=B[t]
   if x:
    if x==5*c or x==(3*c if d in BD else 4*c):return 1
    break
   t+=d
 return 0
def G(cp):
 M=[];w=M.append
 for q,p in enumerate(B):
  if not p or p*S<0:continue
  a=abs(p)
  if a==1:
   d=16*S
   for e in(d-1,d,d+1):
    t=q+e
    if t&136:continue
    if(e==d and not B[t] and not cp)or(e!=d and(B[t]*S<0 or t==Y)):
     if(t>>4)==7*(S>0):M+=[q|(t<<7)|(r<<14)for r in range(5,1,-1)]
     else:
      w(q|(t<<7))
      if e==d and(q>>4)==6-5*(S>0)and not B[t+d]:w(q|((t+d)<<7))
  else:
   D=DT[a]
   for d in D:
    t=q+d
    while not t&136:
     if B[t]:
      if B[t]*S<0:w(q|(t<<7))
      break
     if not cp:w(q|(t<<7))
     if a in(2,6):break
     t+=d
 if not cp:
  for r,kf,kt,rf in((1,4,6,7),(2,4,2,0),(4,116,118,119),(8,116,114,112)):
   if C&r and(S>0)==(kf<16)and all(not B[s]for s in(range(kf+1,kt+1)if kt>kf else range(rf+1,kf)))and B[rf]==4*S and all(not A(s,-S)for s in(range(kf,kt+1)if kt>kf else range(kt,kf+1))):w(kf|(kt<<7))
 return M
def M(m):
 global C,Y,S,KW,KB,EV,NP,WB,BB
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7;sv=[B[t],C,Y,-1,-1,-1,KW,KB,EV,NP,WB,BB];p=B[f];v=B[t]
 if abs(p)!=6:EV-=(V[abs(p)]+pv(abs(p),f,p))*(1 if p>0 else -1)
 if v:
  if abs(v)!=6:EV-=(V[abs(v)]+pv(abs(v),t,v))*(1 if v>0 else -1)
  if abs(v)==1:(WP if v>0 else BP).discard(t)
  elif abs(v)!=6:
   NP-=V[abs(v)]
   if abs(v)==3:
    if v>0:WB-=1
    else:BB-=1
 B[t]=pr*S if pr else p;B[f]=0
 if pr:
  EV+=(V[pr]+pv(pr,t,pr*S))*(1 if S>0 else -1);NP+=V[pr]
  if pr==3:
   if S>0:WB+=1
   else:BB+=1
 else:
  if abs(p)!=6:EV+=(V[abs(p)]+pv(abs(p),t,p))*(1 if p>0 else -1)
 if abs(p)==1:
  (WP if S>0 else BP).discard(f)
  if not pr:(WP if S>0 else BP).add(t)
  if t==Y and(t-f)%8:sv[3]=t-16*S;B[sv[3]]=0;EV-=(100+pv(1,sv[3],-S))*(1 if S<0 else -1);(WP if S<0 else BP).discard(sv[3])
 if abs(p)==6 and abs(t-f)==2:
  sv[4],sv[5]=(t+1,t-1)if t>f else(t-2,t+1);B[sv[5]]=B[sv[4]];B[sv[4]]=0
  EV+=(pv(4,sv[5],p)-pv(4,sv[4],p))*(1 if p>0 else -1)
 C&=CC[f]&CC[t]
 if abs(p)==1 and t-f==32*S:Y=f+16*S
 else:Y=-1
 if abs(p)==6:KW,KB=(t,KB)if S>0 else(KW,t)
 S=-S
 return sv
def U(m,sv):
 global C,Y,S,KW,KB,EV,NP,WB,BB
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7;S=-S
 p=B[t]
 B[f]=S if pr else p;B[t]=sv[0];C,Y=sv[1],sv[2]
 if sv[3]>=0:B[sv[3]]=-S;(WP if S<0 else BP).add(sv[3])
 if sv[4]>=0:B[sv[4]]=B[sv[5]];B[sv[5]]=0
 KW,KB=sv[6],sv[7];EV,NP,WB,BB=sv[8],sv[9],sv[10],sv[11]
 if abs(p)==1 or pr:
  (WP if S>0 else BP).add(f);(WP if S>0 else BP).discard(t)
 if sv[0] and abs(sv[0])==1:(WP if S<0 else BP).add(t)
def E():
 s=EV
 if WB>=2:s+=30
 if BB>=2:s-=30
 for k,sg in((KW,1),(KB,-1)):
  f=k&7;r=k>>4;i=(7-r)*8+f if sg>0 else r*8+f
  s+=sg*(KM[i]*NP+KE[i]*(TOT-NP))//TOT
 for k,sg,Q in((KW,1,WP),(KB,-1,BP)):s+=sg*5*sum(1 for e in(-1,0,1)if k+16*sg+e in Q)+sg*2*sum(1 for e in(-1,0,1)if k+32*sg+e in Q)
 for q in WP:
  f=q&7;r=q>>4
  for x in BP:
   if (x>>4)>r and (x&7)-f in(-1,0,1):break
  else:s+=PPB[r]
 for q in BP:
  f=q&7;r=q>>4
  for x in WP:
   if (x>>4)<r and (x&7)-f in(-1,0,1):break
  else:s-=PPB[7-r]
 return s*S+10
def O(m,pl):
 f=m&127;t=(m>>7)&127
 if m==TM:return 1000000
 if pl<64 and(m==KL[pl*2] or m==KL[pl*2+1]):return 5000
 v=B[t]
 if v:return 10000+V[abs(v)]//16-V[abs(B[f])]*16
 if m>>14:return 9000+(m>>14)*100
 return 0
def R(d,a,b,pl,nm=1):
 global N,TM,S,Y
 N+=1
 if N>NB:raise Z
 K=KW if S>0 else KB
 inck=A(K,-S)
 if d<=0:
  if inck:W=G(0)
  else:
   s=E()
   if s>=b:return b
   if s>a:a=s
   W=G(1)
   if not W:return a
 else:
  if nm and d>=3 and not inck and NP>0:
   y=Y;S=-S;Y=-1
   s=-R(d-3,-b,-b+1,pl+1,0)
   S=-S;Y=y
   if s>=b:return b
  key=(tuple(B),S,C,Y)
  e=TT.get(key)
  if e:
   if e[0]>=d:
    if e[1]==0:return e[2]
    if e[1]==1 and e[2]>=b:return e[2]
    if e[1]==2 and e[2]<=a:return e[2]
   TM=e[3]
  else:TM=0
  W=G(0)
 W.sort(key=lambda m:O(m,pl),reverse=True)
 r=I;a0=a;bm=0
 for i,m in enumerate(W):
  sv=M(m)
  if A(KW if S<0 else KB,S):U(m,sv);continue
  dd=fd=d-1+inck
  if d>=3 and i>=3 and not B[(m>>7)&127] and not(m>>14) and not inck:dd=d-2
  if i:
   s=-R(dd,-a-1,-a,pl+1);U(m,sv)
   if a<s<b:sv=M(m);s=-R(fd,-b,-a,pl+1);U(m,sv)
  else:s=-R(dd,-b,-a,pl+1);U(m,sv)
  if s>r:r=s;bm=m
  if s>a:a=s
  if a>=b:
   if pl<64 and not B[(m>>7)&127] and not(m>>14):
    if KL[pl*2]!=m:KL[pl*2+1]=KL[pl*2];KL[pl*2]=m
   break
 if r==I:return I+pl if inck else(a if d<=0 else 0)
 if d>0 and abs(r)<29000:
  fl=0 if a0<r<b else(1 if r>=b else 2)
  if len(TT)>150000:TT.clear()
  TT[key]=(d,fl,r,bm)
 return r
def X(fen,legal,H):
 global N,TM
 L(fen);ms=[];k=(tuple(B),S,C,Y);H[k]=H.get(k,0)+1
 for x in legal:
  s=lambda i:(ord(x[i+1])-49)*16+ord(x[i])-97
  ms.append(s(0)|(s(2)<<7)|("  nbrq".index(x[4])<<14)if len(x)==5 else s(0)|(s(2)<<7))
 best=ms[0];sc={}
 N=0
 for d in range(1,9):
  try:
   a=I;b=ms[0]
   for j,m in enumerate(ms):
    sv=M(m);s=-R(d-1,-a-1 if j else I,-a,1);U(m,sv)
    if j and a<s:sv=M(m);s=-R(d-1,I,-a,1);U(m,sv)
    if s>a:a=s;b=m
    sc[m]=s
   best=b;ms.remove(b);ms.insert(0,b)
  except Z:break
 L(fen)
 v=sc.get(best,0)
 if v>80:
  for m in ms:
   sv=M(m);k=(tuple(B),S,C,Y);U(m,sv);c=H.get(k,0)
   if c<2 and not(c==1 and v>200):best=m;break
 sv=M(best);k=(tuple(B),S,C,Y);H[k]=H.get(k,0)+1;U(best,sv)
 f=best&127;t=(best>>7)&127;pr=(best>>14)&7;u=lambda q:chr(97+(q&7))+chr(49+(q>>4))
 return u(f)+u(t)+("  nbrq"[pr] if pr else"")
while(g:=P("/game",{}))["status"]!="done":
 H={}
 while g["status"]=="your_move":g=P("/move",{"game":g["game"],"move":X(g["fen"],g["legal_moves"],H)})
