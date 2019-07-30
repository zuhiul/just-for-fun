#include<bits/stdc++.h>
using namespace std;

void circle(double x1,double y1,double x2,double y2,double x3,double y3,double&a,double&b){
	a=((y2-y1)*(y3*y3-y1*y1+x3*x3-x1*x1)-(y3-y1)*(y2*y2-y1*y1+x2*x2-x1*x1))/(2.0*((x3-x1)*(y2-y1)-(x2-x1)*(y3-y1)));
	b=((x2-x1)*(x3*x3-x1*x1+y3*y3-y1*y1)-(x3-x1)*(x2*x2-x1*x1+y2*y2-y1*y1))/(2.0*((y3-y1)*(x2-x1)-(y2-y1)*(x3-x1)));
}
double dis2(double x1,double y1,double x2,double y2){
	double dx = x1-x2;
	double dy = y1-y2;
	return dx*dx+dy*dy;
}

double gao(double x1,double y1,double x2,double y2,double x3,double y3){
	double d1 = dis2(x2,y2,x3,y3);
	double d2 = dis2(x1,y1,x2,y2);
	double cosv = 1-d1/d2/2;
	if(cosv<-1) cosv = -1;
	if(cosv>1) cosv = 1;
	return acos(cosv);
}

double eps = 1e-4;

double gcd(double a,double b){
	if(a<eps) return b;
	return gcd(fmod(b,a),a);
}

int main(){
	double x[4],y[4];
	for(int i = 0;i<3;i++) cin>>x[i]>>y[i];
	circle(x[0],y[0],x[1],y[1],x[2],y[2],x[3],y[3]);
	double a = gao(x[3],y[3],x[1],y[1],x[2],y[2]);
	double b = gao(x[3],y[3],x[0],y[0],x[2],y[2]);
	double c = 2*acos(-1) - a - b;
	double n = gcd(a,gcd(b,c));
	printf("%.6f\n",acos(-1)*dis2(x[3],y[3],x[0],y[0])*sin(n)/n);
	return 0;
}
