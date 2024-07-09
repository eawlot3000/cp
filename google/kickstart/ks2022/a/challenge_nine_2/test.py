import sys
import os
from io import BytesIO, IOBase
from sys import stdin, stdout
BUFSIZE = 8192

class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")

sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

def ri():
	return int(input())

#n = ri()
n = 1
for k in range(n):
  #aa = str(input())
  #aa = str(aa)
  aa = '30'
  final = []
  for j in range(1,10):
    ret = []
    for i in range(len(aa)):
      ret += [int(str(j) + aa)]
      ret += [int(aa[0:i+1] + str(j) + aa[i+1:])]
      for s in ret:
        if int(s)%9 == 0:
          final += [s]
          print(final)
  print("Case #{}: {}".format(k+1, min(final)))




''' #this sort of works...
aa = '1212'
f = True
for j in range(1, 10):
  for i in range(len(aa)):
    temp = []
    # tear part each string
    if f:
      p1 = aa[0:i+1]
      p2 = aa[i+1:]
      temp += [int(str(j) + p1 + p2)]
      temp += [int(p1 + str(j) + p2)]
      temp += [int(p1 + p2 + str(j))]
      ar = min(temp)
      print(temp)
    temp = []
    if f: f = False
    else: f = True
'''
