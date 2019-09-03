#include<bits/stdc++.h>
using namespace std;
const int maxm = 1e5+10;
int num[maxm];
int n,k;
int pri[100],cnt[100],now[100];
void init(){
	for(int i = 2;i*i<=k;i++)
		if(k%i==0){
			pri[++pri[0]] = i;
			while(k%i==0) cnt[pri[0]]++,k/=i;
		}
	if(k!=1) pri[++pri[0]] = k,cnt[pri[0]] = 1;
}
bool check() {
	for(int i = 1;i<=pri[0];i++){
		if(now[i]<cnt[i]) return false;
	}
	return true;
}
int main(){
	scanf("%d%d",&n,&k);
	if(k==1) {
		printf("%lld\n", 1ll*n*(n+1)/2);
		return 0;
	}
	init();
	for(int i = 1;i<=n;i++) scanf("%d",&num[i]);
	int l = 1,r = 0;
	long long ans = 0;
	while(r<=n){
		while(!check()){
			r++;
			if(r>n) break;
			int buf = num[r];
			for(int i = 1;i<=pri[0];i++){
				while(buf%pri[i]==0){
					now[i]++;
					buf/=pri[i];
				}
			}
		}
		if(r>n) break;
		int buf = num[l];
		for(int i = 1;i<=pri[0];i++)
			while(buf%pri[i]==0){
				now[i]--;
				buf/=pri[i];
			}
		l++;
		ans+=n-r+1;
	}
	printf("%lld\n",ans);
	return 0;
}
