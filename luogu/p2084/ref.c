#include<stdio.h>
#include<string.h>
int main() {
  int M,i,len,flag=0,t;
  char N[1005];
  scanf("%d %s",&M,N);
  len=strlen(N);
  t=len-1;
  for(i=0;i<len;i++) {
    if(N[i]!='0') {
      if(flag==1) printf("+%c*%d^%d",N[i],M,t);
      else printf("%c*%d^%d",N[i],M,t);
      flag=1;
    }
    t--;
  }
  return 0;
}
