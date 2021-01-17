grammar Lambda;

term :var|'(' term ')'|term term|lambda var+ dot term;
lambda : 'λ';
dot : '.';
var : ID;
ID : [a-z];