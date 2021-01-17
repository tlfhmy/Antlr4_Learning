grammar Lambda;

term :var|'(' term ')'|term term|desc;
desc:lambda var+ dot term;
lambda : 'λ';
dot : '.';
var : ID;
ID : [a-z];