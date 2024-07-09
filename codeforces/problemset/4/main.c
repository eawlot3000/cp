#include<stdio.h>
#include<stdbool.h>
int n, left;
bool f = false;
int main() {
  scanf("%d", &n);
  for (int i=1; i<=n; i++) {
    left = n-i;
    if (left%2==0 && i%2==0) {
      f = true;
    } break;
  }
  if (f) puts("YES");
  else puts("NO");
  return 0;
}

