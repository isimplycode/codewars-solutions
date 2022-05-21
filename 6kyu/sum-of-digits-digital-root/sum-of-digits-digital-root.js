function digital_root(n) {
  while (n.toString().length > 1) {
    n = n.toString().split("")
    n = n.reduce((a,b) => parseInt(a)+parseInt(b))
  }
  return n
}
