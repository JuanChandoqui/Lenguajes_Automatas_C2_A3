import re

def readRegex(input_text):
    #-------------FECHA DE NACIMIENTO------------------------------------------------
    O_I_P = '((2((0[1-9])|(1[0-9])|(2[0-8])))|((1|3|5|7|8)((0[1-9])|((1|2)[0-9])|(3(0|1))))|((4|6|9)((0[1-9])|((1|2)[0-9])|(3(0))))){1}'
    Q_R = '(((0|2)((0[1-9])|((1|2)[0-9])|(3(0|1))))|(1((0[1-9])|((1|2)[0-9])|(3(0))))){1}'
    U_V_W = '(((1|3|5|7|8)((0[1-9])|(1|2[0-9])|(3(0|1))))|(2((0[1-9])|(1|2[0-9])))|((4|6|9)((0[1-9])|((1|2)[0-9])|(3(0))))){1}'

    b_1 = '(1|3|5|7|9)(((0|1|3|4|5|7|8|9)(0('+O_I_P+')|1('+Q_R+')))|((2|6)(0('+U_V_W+')|1('+Q_R+'))))'
    b_2 = '(0|2|4|6|8)(((1|2|3|5|6|7|9)(0('+O_I_P+')|1('+Q_R+')))|((0|4|8)(0('+U_V_W+')|1('+Q_R+'))))'
    #--------------------------------------------------------------------------------------

    a = '([A-Z]{4})'
    b = '((' + b_1 +'|'+ b_2 + '){1})' 
    c = '((H|M){1})'
    d = '(((A(S)|B(S|C)|C(S|C|M|H|L)|D(F|G)|G(T|R)|H(G)|J(C)|M(N|C|S)|N(T|E|L)|O(C)|P(L)|Q(T|R)|S(L|R|P)|T(S|L|C)|V(Z)|Y(N)|Z(S))){1})'
    e = '([A-Z]{3})'
    f = '(([A-Z]|[0-9]){1})'
    g = '([0-9]{1})'

    regular_expression = a + b + c + d + e + f + g + '$'

    patron = re.compile(regular_expression)

    x = patron.match(input_text)

    if x:
        status = True
    else:
        status = False

    return status