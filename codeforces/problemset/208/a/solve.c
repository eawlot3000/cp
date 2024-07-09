#include<stdio.h>
#include<string.h>

int main() {
  char s[201];
  scanf("%s", s);
  int len = strlen(s);
  for (int i=0; i<len; i++) {
    if (s[i] == 'W' && s[i+1] == 'U' && s[i+2] == 'B') {
      i += 2;
      putchar(' ');
    } else {
      putchar(s[i]);
    }
  }
  putchar('\n');
  return 0;
}
