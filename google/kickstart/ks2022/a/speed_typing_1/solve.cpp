#include<cstdio>
#include<cstring>

const int N = 1000005;

int n, m;
char s[N], t[N];

bool is_subsequence() {
  int a=0;
  for (int i=0; i<m; i++) {
    if (s[a] == t[i]) a++;
    if (a == n) return true;
  }
  return false;
}

int main() {
  int r;
  scanf("%d", &r);
  int c=1;
  while(r--) {
    scanf("%s", s);
    scanf("%s", t);
    n = strlen(s);
    m = strlen(t);
    printf("Case #%d: ", c++);
    if (is_subsequence()) printf("%d\n", m-n);
    else puts("IMPOSSIBLE");
  }
  return 0;
}
