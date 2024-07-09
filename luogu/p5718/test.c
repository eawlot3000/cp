// we dont have the <min> fuc, so we solve this bitch with ret[]!
#include<stdio.h>
int main() {
  int ret[100] = {0};
  int n;
  int in=0;
  int check = 0;
  scanf("%d", &n);
  for (int i=0; i<n; i++) {
    scanf("%d", &in);
    ret[i] = in;
    if (ret[i] > ret[i+1]) check = ret[i+1];
    else check = ret[i];
  }
  //printf("%d",ret[3]);
  printf("%d\n", check);
  return 0;

}



