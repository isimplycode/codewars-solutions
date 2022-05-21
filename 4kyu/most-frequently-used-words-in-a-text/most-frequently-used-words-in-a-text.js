function textFilter(character) {
  if ("~!@#%^&*()_+-=|[]}{:,./".includes(character) != true) { return character }
}
function topThreeWords(text) {
  let dict = {}
  text = text.split("").filter(textFilter).join("").replace(/\n/g, " ").split(" ")
  for (let j = 0; j <= text.length-1; j++) {
    if (text[j] == "" || text[j] == "''") { continue }
    if (dict[text[j].toLowerCase()] == null) { dict[text[j].toLowerCase()] = 1; continue }
    dict[text[j].toLowerCase()]++
  }
  let highestacount = 0, highestbcount = 0, highestccount = 0;
  let highesta = "", highestb = "", highestc = "";
  for (value in dict) {
    if (dict[value] > highestacount) { highestccount = highestbcount; highestc = highestb; highestbcount = highestacount; highestb = highesta; highestacount = dict[value]; highesta = value; continue }
    if (dict[value] > highestbcount) { highestccount = highestbcount; highestc = highestb; highestbcount = dict[value]; highestb = value; continue }
    if (dict[value] > highestccount) { highestccount = dict[value]; highestc = value }
  }
  if (highesta == "" && highestb == "" && highestc == "") { return [] }
  let returnArr = [] 
  if (highesta != "" && highesta != "\'") { returnArr.push(highesta) }
  if (highestb != "") { returnArr.push(highestb) }
  if (highestc != "") { returnArr.push(highestc) }
  return returnArr
}
