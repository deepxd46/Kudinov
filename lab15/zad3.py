import re

def parse_polynomial(poly_str):

    coefficients = []
    

    terms = re.findall(r'([+-]?\d*)(x\^(\d+)|x)?', poly_str.replace(" ", ""))
    

    max_degree = 0
    for term in terms:
        if term[2]:  
            degree = int(term[2])
            max_degree = max(max_degree, degree)
        elif 'x' in term[1]:  
            max_degree = max(max_degree, 1)
    
    # Заполняем коэффициенты
    for degree in range(max_degree, -1, -1):
        match = next((term for term in terms if (term[2] and int(term[2]) == degree) or (term[1] == "x" and degree == 1) or (degree == 0 and term[1] == "")), None)
        
        if match:
            coefficient = match[0]
            if coefficient == '' or coefficient == '+':  
                coefficient = 1
            elif coefficient == '-':  
                coefficient = -1
            else:
                coefficient = int(coefficient)
        else:
            coefficient = 0
        
        coefficients.append(coefficient)
    
    return coefficients


poly = "3x^4 + 2x^2 - 5x + 7"
coefficients = parse_polynomial(poly)
print(coefficients)  