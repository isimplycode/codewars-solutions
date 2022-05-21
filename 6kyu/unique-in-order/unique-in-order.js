var uniqueInOrder=function(iterable){
  let arr = [];
  for (let i = 0; i <= iterable.length-1; i++) {
    if (i == iterable.length-1) {
      if ( iterable[i] != iterable[i-1] || arr[arr.length-1] != iterable[i]) {
        arr.push(iterable[i])
        } 
      continue
    }
    if (iterable[i] != iterable[i+1]) {
      arr.push(iterable[i])
    }
  }
  return arr
}
