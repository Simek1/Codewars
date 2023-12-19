function parse(data){
  let output=[];
  let deadfish=0;
  for (i=0; i<data.length; i++){
    if (data[i]=="i"){
      deadfish+=1;
    };
    if (data[i]=="d"){
      deadfish-=1
    };
    if (data[i]=="s"){
      deadfish=deadfish*deadfish;
    };
    if (data[i]=="o"){
      output.push(deadfish)
    };
  };
  return(output);
}
