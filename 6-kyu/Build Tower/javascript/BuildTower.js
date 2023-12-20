function towerBuilder(nFloors) {
  let tower=[];
  for (let i=0; i<nFloors; i++){
    let row="";
    for(let j=0; j<((nFloors*2-1)-(i*2+1))/2; j++){
      row+=" "
    };
    for(j=0; j<(i*2+1); j++){
      row+="*"
    };
    for(j=0; j<((nFloors*2-1)-(i*2+1))/2; j++ ){
      row+=" "
    };
    tower.push(row)
  };
  return(tower)
}
