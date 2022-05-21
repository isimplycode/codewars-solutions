dict = {
  H: 3600,
  M: 60,
  S: 1
}

function humanReadable (seconds) {
  let hcounter = 0;
  let mcounter = 0;
  let scounter = 0;
  let newh, news, newm;
  for (let x in dict) {
    while (seconds >= dict[x]) {
      seconds -= dict[x]
      if (x == "H") { hcounter += 1 }
      if (x == "M") { mcounter += 1 }
      if (x == "S") { scounter += 1 }
    }
  }
  if (hcounter < 10) { newh = "0" + hcounter.toString() } else { newh = hcounter }
  if (mcounter < 10) { newm = "0" + mcounter.toString() } else { newm = mcounter }
  if (scounter < 10) { news = "0" + scounter.toString() } else { news = scounter }
  return `${newh}:${newm}:${news}`;
}
