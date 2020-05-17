class Constraint:
    """Constraint Class

    three type constraint, ==, <=, and >=.
    
    1. eq type (equal); `expression == 0`

    2. le type (less than or equal); `expression <= 0`

    3. ge type (greater than or equal); `expression >= 0`

    Parameters
    ----------
    expression : Expression family
        expression of constraint.
    type : str
        Constraint type. We must choice from eq, le or ge.
    """
    def __init__(self, expression, _type, name=None):
        assert _type in {'eq', 'le', 'ge'},\
            f"""get constraint type {_type} but this is not supported.
                You must choice from eq, le or ge. 
             """
        self.expression = expression
        self.type = _type
        self.name = None
    
    def value(self, solution=None):
        return self.expression.value(solution)
    
    def getVariables(self):
        return self.expression.getVariables()
    
    def __str__(self):
        s  = f'Name: {self.name}\n'
        s += f'  Type      :  Constraint\n'
        s += f'  ConstType : {self.type}\n'
        s += f'  Expression: {self.expression}\n'
        return s

    def __repr__(self):
        return f'Constraint({self.expression.__repr__()}, {self.type}, {self.name})'
