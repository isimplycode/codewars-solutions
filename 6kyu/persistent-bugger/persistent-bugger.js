function persistence(num) {
  let counter = 0;
  while (num.toString().length > 1) { num = num.toString().split(""); num = num.reduce((a,b)=> a*b); counter += 1; }
  return counter
}
