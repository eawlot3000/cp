package main
import "fmt"
func isValid(str string) bool {
  var s []byte
  if str[0] == '(' || str[0] == '{' || str[0] == '[' {
    for i:=0; i<len(str); i++ {
      s = append(s, str[i])
      if len(s) > 1 {
        if s[len(s)-2] == '[' && s[len(s)-1] == ']' {
          s = s[:len(s)-2]
        } else if s[len(s)-2] == '{' && s[len(s)-1] == '}' {
          s = s[:len(s)-2]
        } else if s[len(s)-2] == '(' && s[len(s)-1] == ')' {
          s = s[:len(s)-2]
        }
      }
    }
    if len(s) == 0 {
      return true
    }
  }
  return false
}

func main() {
  var input string
  fmt.Scan(&input)
  fmt.Println(isValid(input))
}
/*
package main
import (
  "fmt"
  "strings"
  "os"
)
func isValid(s string) bool {
  fmt.Scan(&s)

  if strings.Count(s, "(") != strings.Count(s, ")") || strings.Count(s, "[") != strings.Count(s, "]") || strings.Count(s, "{") != strings.Count(s, "}") == false {
    return false
    os.Exit(0)
  }
  return true


func main() {
  var s string
  fmt.Scan(&s)
  fmt.Println(isValid(s))
}
*/
