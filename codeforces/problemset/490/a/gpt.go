package main

import (
  "fmt"
)

func main() {
  var n, t int
  fmt.Scan(&n)

  students := make([]int, n)
  maths := []int{}
  programming := []int{}
  pe := []int{}

  // separate students by their skill
  for i := 0; i < n; i++ {
    fmt.Scan(&t)
    students[i] = t
    if t == 1 {
      programming = append(programming, i+1)
    } else if t == 2 {
      maths = append(maths, i+1)
    } else {
      pe = append(pe, i+1)
    }
  }

  num_teams := min(len(maths), len(programming), len(pe))

  // output number of teams
  fmt.Println(num_teams)

  // output the teams
  for i := 0; i < num_teams; i++ {
    fmt.Println(maths[i], programming[i], pe[i])
  }
}

func min(a, b, c int) int {
  if a <= b && a <= c {
    return a
  } else if b <= a && b <= c {
    return b
  } else {
    return c
  }
}

