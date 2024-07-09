#include<stdio.h>
int main() {
  int n, count = 0;
  int ret[10005] = {0};
  scanf("%d", &n);
  for (int i=0; i<n; i++) scanf("%d", &ret[i]);
  for (int i=0; i<n; i++)
    for (int j=i+1; j<n; j++)
      if (ret[i] > ret[j]) count++;
  printf("%d\n",count);
  return 0;
}
