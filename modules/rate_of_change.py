class Polynomial(object):
    def __init__(self, terms):
        """
        :param terms: [[Coefficient: number, Exponent: number], [Coefficient: number, Exponent: number]]
        """
        if type(terms) == str:
            self.terms = self.parse(terms)
        else:
            self.terms = terms

    def parse(self, string: str) -> list:
        terms = []
        string = string.split()
        for i, value in enumerate(string):
            try:
                if string[i - 1] == '-':
                    sign = '-'
                else:
                    sign = ''
            except IndexError:
                sign = ''
            if not i % 2:
                terms.append(sign + value)
        new_terms = []
        for term in terms:
            try:
                i = term.index('x')
                coefficient = float(term[:i])
                if int(coefficient) == coefficient:
                    coefficient = int(coefficient)
                try:
                    exponent = float(term[i + 2:])
                    if int(exponent) == exponent:
                        exponent = int(exponent)
                except ValueError:
                    exponent = 1
            except ValueError:
                coefficient = float(term)
                if int(coefficient) == float(coefficient): coefficient = int(coefficient)
                exponent = 0
            new_terms.append([coefficient, exponent])
        return new_terms

    def calculate(self, x_value, sig_figs=3):
        """
        Calculates and returns the y value of the polynomial at a value of x
        :param sig_figs:
        :param x_value:
        :return: y value
        """
        total_value = 0

        for term in self.terms:
            total_value += term[0] * x_value ** term[1]
        # todo: make this round to 3 significant figures
        return total_value

    def first_derivative(self):
        """
        Returns the first derivative of the polynomial as a polynomial object
        :return: Polynomial object representing the first derivative
        """
        new_terms = []
        for term in self.terms:
            if term[1] != 0:
                new_terms.append([term[0] * term[1], term[1] - 1])
        return Polynomial(new_terms)

    def take_derivative(self, derivative=1):
        """
        Returns the nth derivative where n is the variable derivative
        :param derivative: derivative to return
        :return: Polynomial object representing the nth derivative
        """
        temp = self
        for _ in range(derivative):
            temp = temp.first_derivative()
        return temp

    def __str__(self):
        """
        Returns a human friendly way to interpret the polynomial function
        :return: String
        """
        return_value = ''
        for i, term in enumerate(self.terms):
            if i > 0:
                if term[0] < 0:
                    return_value += ' -'
                else:
                    return_value += ' + '
            if term[1] == 0:
                return_value += str(abs(term[0]))
            else:
                return_value += str(abs(term[0])) + 'x^' + str(term[1])
        return return_value


if __name__ == '__main__':
    user_input = input('Enter the function: ')
    # user_input = '0.0009x^2 + 0.04x + 4'
    # user_input = '0.0007x^3 - 0.1796x^2 + 14.663x + 160'
    my_function = Polynomial(user_input)
    second_derivative = my_function.take_derivative(2)
    print(my_function.calculate(221) - my_function.calculate(220))
    print(my_function.first_derivative())
