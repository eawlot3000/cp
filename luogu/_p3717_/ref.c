#include<stdio.h>
#include<math.h>
int a[105][105]={0};
int n,m,r,sum=0;
int x,y;
int main() {
scanf("%d%d%d", &n,&m,&r);
for(int i=1; i<=m; i++) {
  scanf("%d%d", &x,&y);

  for(int i=1; i<=n; i++) {
    for(int j=1; j<=n; j++) {
      double d = sqrt((x-i)*(x-i)+(y-j)*(y-j));
      if(d <= r) {
          a[i][j]=1;
      }
    }
  }
}
for(int i=1; i<=n; i++) {
    for(int j=1; j<=n; j++) {
        if(a[i][j]==1) {
            count++;
        }
    }
}
printf("%d\n",count);
return 0;
}
