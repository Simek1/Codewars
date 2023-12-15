function reverseWords(str) {
  let rev_str = "";
  let word = "";
  for (let i = 0; i < str.length; i++) {
    if (/\s/.test(str[i])){
      word=word.split("").reverse().join("");
      rev_str+=word;
      word="";
      rev_str+=str[i];
    } else {
      word+=str[i];
    };
  };
  word=word.split("").reverse().join("");
  rev_str+=word;
  return rev_str;
}
