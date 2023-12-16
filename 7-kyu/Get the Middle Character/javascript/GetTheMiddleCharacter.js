function getMiddle(s)
{
  let len;
  len=s.length/2;
  if (len % 1 == 0){
    return s[len-1]+s[len];
  } else {
    return s[Math.ceil(len-1)];
  };
}
