function solve_graph(start, end, arcs) {
  let vis={};
  let adj={};
  for (let i=0; i<arcs.length; ++i) {
    if (arcs[i].start in adj) {
      vis[arcs[i].start]=0;
      vis[arcs[i].end]=0;
      adj[arcs[i].start].push(arcs[i].end);
    } else {
      vis[arcs[i].start]=0;
      vis[arcs[i].end]=0;
      adj[arcs[i].start]=[arcs[i].end];
    }
  }
  if (start==end) {
    return true;
  }
  let stk=[];
  stk.push(start);
  while (stk.length) {
    let temp=stk.pop();
    if (vis[temp]==1) {
      continue;
    }
    vis[temp]=1;
    if (temp==end) {
      return true;
    }
    if (temp in adj) {
      for (let i=0; i<adj[temp].length; ++i) {
        stk.push(adj[temp][i]);
      }
    }
  }
  return false;
}
