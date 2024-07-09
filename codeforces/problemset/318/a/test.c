#include<stdio.h>
int main() {
  int long long n,k;
  int long long arr[500000000001];

  scanf("%lld %lld", &n, &k);
  for (int i=0; i<=n; i++) {
    if(i%2) arr[i] = i;
  }
  for (int j=0; j<=100; j++) printf("%64lld", arr[j]);
  //printf("%lld %lld", n, k);
  return 0;
}


