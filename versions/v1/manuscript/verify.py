from dataclasses import dataclass
from itertools import combinations, permutations, product
import json
from random import Random


@dataclass(frozen=True)
class Gaussian:
    real: int = 0
    imag: int = 0

    def __add__(self, other):
        return Gaussian(self.real + other.real, self.imag + other.imag)

    def __neg__(self):
        return Gaussian(-self.real, -self.imag)

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        return Gaussian(self.real * other.real - self.imag * other.imag,
                        self.real * other.imag + self.imag * other.real)

    def conjugate(self):
        return Gaussian(self.real, -self.imag)

    def norm_squared(self):
        return self.real * self.real + self.imag * self.imag


ZERO = Gaussian()
ONE = Gaussian(1)


def require(condition, label):
    if not condition:
        raise ValueError(label)


def determinant(matrix):
    dimension = len(matrix)
    result = ZERO
    for ordering in permutations(range(dimension)):
        inversions = sum(ordering[first] > ordering[second]
                         for first in range(dimension)
                         for second in range(first + 1, dimension))
        term = Gaussian(-1 if inversions % 2 else 1)
        for index, column in enumerate(ordering):
            term = term * matrix[index][column]
        result = result + term
    return result


def adjoint(matrix):
    return [[matrix[row][column].conjugate() for row in range(len(matrix))]
            for column in range(len(matrix[0]))]


def multiply(left, right):
    return [[sum((left[row][index] * right[index][column]
                  for index in range(len(right))), ZERO)
             for column in range(len(right[0]))] for row in range(len(left))]


def add(left, right):
    return [[first + second for first, second in zip(left_row, right_row)]
            for left_row, right_row in zip(left, right)]


def selected(matrix, rows, columns):
    return [[matrix[row][column] for column in columns] for row in rows]


def random_matrix(generator, rows, columns):
    return [[Gaussian(generator.randint(-2, 2), generator.randint(-2, 2))
             for column in range(columns)] for row in range(rows)]


def hermitian_matrix(generator, dimension):
    matrix = random_matrix(generator, dimension, dimension)
    return add(matrix, adjoint(matrix))


def gram_matrix(matrix):
    return multiply(adjoint(matrix), matrix)


def check_pair(first, second, totals):
    row_count, dimension = len(first), len(first[0])
    hermitian = add(multiply(adjoint(first), second), multiply(adjoint(second), first))
    positive = add(gram_matrix(first), gram_matrix(second))
    require(hermitian == adjoint(hermitian), 'Hermitian Jordan expression')
    require(positive == adjoint(positive), 'Hermitian Gram expression')
    coefficients_hermitian, coefficients_positive = [], []
    for degree in range(dimension + 1):
        sum_hermitian, sum_positive, sum_absolute = 0, 0, 0
        for columns in combinations(range(dimension), degree):
            minor_hermitian = determinant(selected(hermitian, columns, columns))
            minor_positive = determinant(selected(positive, columns, columns))
            require(minor_hermitian.imag == minor_positive.imag == 0, 'Real principal determinants')
            require(abs(minor_hermitian.real) <= minor_positive.real, 'Absolute principal bound')
            upper = selected(first, range(row_count), columns)
            lower = selected(second, range(row_count), columns)
            stacked_first, stacked_second = upper + lower, lower + upper
            mixed, norm_first, norm_second = ZERO, 0, 0
            for rows in combinations(range(2 * row_count), degree):
                minor_first = determinant(selected(stacked_first, rows, range(degree)))
                minor_second = determinant(selected(stacked_second, rows, range(degree)))
                mixed = mixed + minor_first.conjugate() * minor_second
                norm_first += minor_first.norm_squared()
                norm_second += minor_second.norm_squared()
            require(mixed == minor_hermitian, 'Mixed Cauchy-Binet identity')
            require(norm_first == norm_second == minor_positive.real, 'Gram Cauchy-Binet identities')
            require(mixed.norm_squared() <= norm_first * norm_second, 'Gram determinant inequality')
            sum_hermitian += minor_hermitian.real
            sum_positive += minor_positive.real
            sum_absolute += abs(minor_hermitian.real)
            totals['principal_subsets'] += 1
        require(abs(sum_hermitian) <= sum_absolute <= sum_positive, 'Elementary symmetric coefficient bounds')
        coefficients_hermitian.append(sum_hermitian)
        coefficients_positive.append(sum_positive)
        totals['coefficient_bounds'] += 1
    difference_trace = sum(positive[index][index].real - hermitian[index][index].real
                           for index in range(dimension))
    squared_distance = sum((first[row][column] - second[row][column]).norm_squared()
                           for row in range(row_count) for column in range(dimension))
    require(difference_trace == squared_distance, 'Trace equality identity')
    totals['trace_identities'] += 1
    for parameter in [ZERO, ONE, Gaussian(-1), Gaussian(2), Gaussian(0, 1), Gaussian(1, 1)]:
        evaluated = [[(ONE if row == column else ZERO) + parameter * hermitian[row][column]
                      for column in range(dimension)] for row in range(dimension)]
        polynomial, power = ZERO, ONE
        for coefficient in coefficients_hermitian:
            polynomial = polynomial + power * Gaussian(coefficient)
            power = power * parameter
        require(determinant(evaluated) == polynomial, 'Determinant polynomial identity')
        if parameter.imag == 0:
            upper_bound = sum(coefficient * abs(parameter.real) ** degree
                              for degree, coefficient in enumerate(coefficients_positive))
            require(polynomial.norm_squared() <= upper_bound * upper_bound, 'Real determinant polynomial bound')
        if parameter.real == 0 and abs(parameter.imag) == 1:
            upper_bound = sum(coefficients_positive)
            require(polynomial.norm_squared() <= upper_bound * upper_bound, 'Imaginary determinant polynomial bound')
        totals['polynomial_identities'] += 1
    totals['matrix_pairs'] += 1
    return coefficients_hermitian, coefficients_positive


def main():
    generator = Random(512579)
    totals = {key: 0 for key in ['matrix_pairs', 'principal_subsets', 'coefficient_bounds',
                                'trace_identities', 'polynomial_identities']}
    for dimension in range(1, 5):
        for sample in range(6):
            check_pair(hermitian_matrix(generator, dimension),
                       hermitian_matrix(generator, dimension), totals)
        for sample in range(4):
            check_pair(gram_matrix(random_matrix(generator, dimension, dimension)),
                       gram_matrix(random_matrix(generator, dimension, dimension)), totals)
        for row_count in range(1, 4):
            for sample in range(3):
                check_pair(random_matrix(generator, row_count, dimension),
                           random_matrix(generator, row_count, dimension), totals)
        zero = [[ZERO for column in range(dimension)] for row in range(dimension)]
        check_pair(zero, zero, totals)
        equal = random_matrix(generator, dimension, dimension)
        equal_coefficients = check_pair(equal, equal, totals)
        require(equal_coefficients[0] == equal_coefficients[1], 'Simultaneous equality example')
        opposite_coefficients = check_pair(equal, [[-entry for entry in row] for row in equal], totals)
        require(opposite_coefficients[0] == [(-1) ** degree * coefficient
                                            for degree, coefficient in enumerate(opposite_coefficients[1])],
                'Opposite-matrix absolute equality example')
    example_first = [[Gaussian(1), ZERO], [ZERO, ZERO]]
    example_second = [[Gaussian(1), Gaussian(1)], [Gaussian(1), Gaussian(1)]]
    example_coefficients = check_pair(example_first, example_second, totals)
    require(example_coefficients == ([1, 2, -1], [1, 5, 2]), 'Indefinite Jordan example')
    scalar_schur_count = 0
    for entries in product(range(6), repeat=3):
        largest, middle, smallest = sorted(entries, reverse=True)
        total = sum(entries)
        squares = sum(entry * entry for entry in entries)
        cubic_expression = 6 * sum(entry ** 3 for entry in entries) + total ** 3
        certificate = 2 * ((largest - middle) ** 2 * (largest + middle - smallest)
                           + smallest * (largest - smallest) * (middle - smallest))
        require(cubic_expression - 5 * total * squares == certificate >= 0,
                'Scalar Schur identity')
        scalar_schur_count += 1
    totals['scalar_schur_identities'] = scalar_schur_count
    result = {
        'status': 'pass',
        'arithmetic': 'Gaussian integers; exact integer determinant expansion',
        'seed': 512579,
        'scope': {
            'hermitian_pairs': '6 seeded pairs per n=1,2,3,4',
            'positive_semidefinite_pairs': '4 Gram-matrix pairs per n=1,2,3,4',
            'rectangular_pairs': '3 seeded pairs per p=1,2,3 and n=1,2,3,4',
            'boundary_pairs': 'zero, equal and opposite pairs for each n=1,2,3,4',
            'polynomial_parameters': ['0', '1', '-1', '2', 'i', '1+i'],
            'polynomial_bounds': 'parameters 0,1,-1,2,i',
            'scalar_schur': 'all triples in {0,1,2,3,4,5}^3',
            'universal_statements': 'written proofs in note.tex; finite checks cover the stated matrices'
        },
        'counts': totals,
        'example': {'elementary_coefficients_H': example_coefficients[0],
                    'elementary_coefficients_R': example_coefficients[1]}
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
