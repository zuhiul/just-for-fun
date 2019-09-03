#include <bits/stdc++.h>
using namespace std;
long long n,k;
int main(){
	scanf("%lld%lld",&n,&k);
	long long buf = k*(k+1)/2;
	if(buf > n||k>=1000000){
		printf("-1");
		return 0;
	}
	long long ans = 0;
	for(long long i = 1;i*i<=n;i++) {
		if(n%i==0) {
			if(n/i >= buf){
				ans = max(ans,i);
			}
			if(i>=buf) {
				ans = max(ans, n/i);
			}
		}
	}
	if(ans != 0) {
		for(long long j = 1;j<k;j++) {
			printf("%lld ", j*ans);
			n-=j*ans;
		}
		printf("%lld\n", n);
		return 0;
	}
	for(int i = 1;i<k;i++) {
		printf("%d ",i);
		n-=i;
	}
	printf("%lld",n);
	return 0;
}
