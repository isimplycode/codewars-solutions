function validParentheses(parens) {
  if (parens[0] == ")") { return false }
  let stack = [];
  for (let i = 0; i <= parens.length-1; i++ ) {
    if (parens[i] == "(") { stack.push("(") }
    if (parens[i] == ")") { if (stack.length == 0) { return false } stack.pop() } 
  }  
  if (stack.length == 0) { return true }
  return false;
}
