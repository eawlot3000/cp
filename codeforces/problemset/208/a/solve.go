package main
import (
  "fmt"
  str "strings"
)

func main() {
  var s string
  fmt.Scan(&s)
  s = str.ReplaceAll(s, "WUB", " ")
  s = str.Join(str.Fields(s), " ")
  fmt.Println(s)
}
