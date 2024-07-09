#include<stdio.h>
int max(int a, int b) {
  return a > b ? a:b;
}

int main() {
  int n;
  scanf("%d", &n);
  int group[n];
  for (int i=0; i<n; i++) {
    scanf("%d", &group[i]);
  }
  int count[5] = {0};
  for (int i=0; i<n; ++i) {
    count[group[i]]++;
  }

  int taxis = count[4] + count[3] + (count[2]*2 + max(count[1] - count[3], 0) + 3) / 4;
  printf("%d\n", taxis);
  return 0;
}
