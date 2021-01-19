grammar Lambda;

term :var
     |'(' term ')'
     |term term
     |desc
     ;

desc:Lambda var+ Dot term;
var : ID;

Lambda : 'λ';
Dot : '.';
ID : [a-z];