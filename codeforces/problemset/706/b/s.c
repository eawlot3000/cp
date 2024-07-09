#include<stdio.h>
#define MAX_N 1000
#define MAX_S 1000

int main() {
  int n, an[MAX_N], s, ret[MAX_S], cnt = 0;
  scanf("%d", &n);
  for (int i = 0; i < n; i++) {
    scanf("%d", &an[i]);
  }
  scanf("%d", &s);
  for (int i = 0; i < s; i++) {
    scanf("%d", &ret[i]);
    for (int j = 0; j < n; j++) {
      if (an[j] <= ret[i]) {
        cnt++;
      }
    }
    printf("%d\n", cnt);
    cnt = 0;
  }
  return 0;
}
