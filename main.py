import json,os,urllib.request as u
def P(p,b):
 with u.urlopen(u.Request(os.getenv("MAKEFUN_ENV_URL")+p,json.dumps(b).encode()))as r:return json.load(r)
V=[0,100,320,330,500,900,0];CF=[0,0,6,5,3,3]
PA="505050505560603055454050505050705555607560607080"
PS=[int(PA[i:i+2])-50 for i in range(0,48,2)]
B=[0]*128
CC=[15]*128
CC[0],CC[7],CC[4],CC[112],CC[119],CC[116]=13,14,12,7,11,3
BD=[-17,-15,15,17];RD=[-16,-1,1,16];ND=[-33,-31,-18,-14,14,18,31,33];KD=sorted(BD+RD);DT={2:ND,6:KD,3:BD,4:RD,5:BD+RD}
class Z(Exception):pass
N=0;I=-30000
def L(f):
 global S,C,Y,KW,KB
 p=f.split();B[:]=[0]*128;q=112
 for c in p[0]:
  if c=="/":q-=24
  elif c.isdigit():q+=int(c)
  else:
   v="PNBRQK".index(c.upper())+1;B[q]=v if c.isupper()else-v;q+=1
 S=1-(p[1]<"w")*2;C=sum(1<<"KQkq".index(c)for c in p[2]if c in"KQkq");Y=-1;KW=B.index(6);KB=B.index(-6)
 if p[3]!="-":Y=(int(p[3][1])-1)*16+ord(p[3][0])-97
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
 global C,Y,S,KW,KB
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7;sv=[B[t],C,Y,-1,-1,-1,KW,KB];p=B[f];B[t]=pr*S if pr else p;B[f]=0
 if abs(p)==1 and t==Y and(t-f)%8:sv[3]=t-16*S;B[sv[3]]=0
 if abs(p)==6 and abs(t-f)==2:
  sv[4],sv[5]=(t+1,t-1)if t>f else(t-2,t+1);B[sv[5]]=B[sv[4]];B[sv[4]]=0
 C&=CC[f]&CC[t]
 if abs(p)==1 and t-f==32*S:Y=f+16*S
 else:Y=-1
 if abs(p)==6:KW,KB=(t,KB)if S>0 else(KW,t)
 S=-S
 return sv
def U(m,sv):
 global C,Y,S,KW,KB
 f=m&127;t=(m>>7)&127;pr=(m>>14)&7;S=-S
 B[f]=S if pr else B[t];B[t]=sv[0];C,Y=sv[1],sv[2]
 if sv[3]>=0:B[sv[3]]=-S
 if sv[4]>=0:B[sv[4]]=B[sv[5]];B[sv[5]]=0
 KW,KB=sv[6],sv[7]
def E():
 s=0
 for q,p in enumerate(B):
  if p:
   a=abs(p);f=q&7;r=q>>4;v=V[a];rr=r if p>0 else 7-r
   if a==1:v+=49 if rr==6 else PS[rr*4+(f if f<4 else 7-f)]
   elif a==6:v-=20*rr
   else:v+=CF[a]*(3-abs(f-3)-abs(min(rr,7-rr)-3))
   s+=v*(p>0 or-1)
 return s*S
def O(m):
 f=m&127;t=(m>>7)&127
 return V[abs(B[f])]//16-V[abs(B[t])]*16
def R(d,a,b,pl):
 global N
 N+=1
 if N>2e5:raise Z
 K=KW if S>0 else KB
 if d<=0:
  if A(K,-S):W=G(0)
  else:
   s=E()
   if s>=b:return b
   if s>a:a=s
   W=G(1)
   if not W:return a
 else:W=G(0)
 W.sort(key=O);r=I
 for m in W:
  sv=M(m)
  if A(KW if S<0 else KB,S):U(m,sv);continue
  s=-R(d-1,-b,-a,pl+1);U(m,sv)
  r=max(r,s)
  a=max(a,s)
  if a>=b:return a
 if r==I:return I+pl if A(K,-S)else(a if d<=0 else 0)
 return r
def X(fen,legal):
 global N
 L(fen);ms=[]
 for x in legal:
  s=lambda i:(ord(x[i+1])-49)*16+ord(x[i])-97
  ms.append(s(0)|(s(2)<<7)|("  nbrq".index(x[4])<<14)if len(x)==5 else s(0)|(s(2)<<7))
 best=ms[0]
 N=0
 for d in range(1,5):
  try:
   a=I;b=ms[0]
   for m in ms:
    sv=M(m);s=-R(d-1,I,-a,1);U(m,sv)
    if s>a:a=s;b=m
   best=b;ms.remove(b);ms.insert(0,b)
  except Z:break
 f=best&127;t=(best>>7)&127;pr=(best>>14)&7;u=lambda q:chr(97+(q&7))+chr(49+(q>>4))
 return u(f)+u(t)+("  nbrq"[pr] if pr else"")
while(g:=P("/game",{}))["status"]!="done":
 while g["status"]=="your_move":g=P("/move",{"game":g["game"],"move":X(g["fen"],g["legal_moves"])})
