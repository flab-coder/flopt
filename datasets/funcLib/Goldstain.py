from flopt import Variable

def create_objective(*args, **kwargs):
    def obj(x):
        x1, x2 = x
        c1 = (x1+x2+1)**2
        c2 = 19-14*x1+3*x1*x1-14*x2+6*x1*x2+3*x2*x2
        c3 = (2*x1-3*x2)**2
        c4 = 18-32*x1+12*x1*x1+48*x2-36*x1*x2+27*x2*x2
        return (1+c1*c2)*(30+c3*c4)
    return obj


def create_variables(*args, **kwargs):
    variables = [
        Variable(
            name=f'x{i}',
            lowBound=-2,
            upBound=2,
            cat='Continuous'
        )
        for i in [0, 1]
    ]
    return variables


def minimum_obj():
    return 3
