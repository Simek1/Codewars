function toCamelCase(str){
  let newstr="";
  for (let i=0; i<str.length; i++){
    if (/[A-Za-z]/.test(str[i])){
      newstr+=str[i];
    } else {
      newstr+=str[i+1].toUpperCase();
      i++;
    };    
  };
  return(newstr)
}
