grammar Json;

json    :   object
        |   array
        ;

object  :   '{' pair (',' pair)* '}'
        |   '{' '}'
        ;
pair    :   STRING ':' value ;

array   :   '[' value (',' value)* ']'
        |   '[' ']'
        ;

value   :   STRING
        |   NUMBER
        |   object
        |   array
        |   'true'
        |   'false'
        |   'null'
        ;

STRING  :   '"' (ESC | ~["\\])* '"' ;
fragment ESC : '\\' (["\\/bfnrt] | UNICODE) ;
fragment UNICODE : 'u' HEX HEX HEX HEX ;
fragment HEX : [0-9a-fA-F] ;

NUMBER  :   '-'? INT '.' INT EXP?
        |   '-'? INT EXP
        |   '-'? INT
        ;
fragment INT : '0' | [1-9] [0-9]* ;
fragment EXP : [Ee] [+\-]? INT ;    //\-是对-的转义，因为[...]中的-用于表达”范围“语义

WS  :   [ \t\n\r]+ -> skip;