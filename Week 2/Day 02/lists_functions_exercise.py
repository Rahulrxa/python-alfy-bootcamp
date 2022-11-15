def input_list(str_input=None):
    number_list = []
    total_sum = 0.0
    while str_input != '':
        str_input = input()
        if str_input != '':
            number_list.append(str_input)
            total_sum += float(str_input)
    number_list.append(total_sum)
    return number_list


def monotonicity_by_operator(operator, sequence):
    monolist = []
    for i in range(len(sequence) - 1):
        # use Dictionaries
        match operator:
            case '<=':
                if sequence[i] <= sequence[i + 1]:
                    monolist.append(True)
                else:
                    monolist.append(False)
            case '<':
                if sequence[i] < sequence[i + 1]:
                    monolist.append(True)
                else:
                    monolist.append(False)
            case '>=':
                if sequence[i] >= sequence[i + 1]:
                    monolist.append(True)
                else:
                    monolist.append(False)
            case '>':
                if sequence[i] > sequence[i + 1]:
                    monolist.append(True)
                else:
                    monolist.append(False)
    return False not in monolist
    # if False in monolist:
    #     return False
    # else:
    #     return True


def check_monotonic_sequence(sequence):
    operators = ['<=', '<', '>=', '>']
    lst = []
    if len(sequence) < 2:
        return [True, True, True, True]
    for operator in operators:
        lst.append(monotonicity_by_operator(operator, sequence))
    return lst


def check_monotonic_sequence_inverse(def_bool):
    match def_bool:
        case [True, True, True, True]:
            return [10]
        case [True, True, False, False]:
            return [1, 2, 3, 4, 5, 6, 7, 8]
        case [True, False, False, False]:
            return [1, 2, 2, 3]
        case [True, False, True, False]:
            return [1, 1, 1, 1]
        case [False, False, True, False]:
            return [3, 2, 1, 1]
        case [False, False, True, True]:
            return [7.5, 4, 3.141, 0.111]
        case [False, False, False, False]:
            return [1, 0, -1, 1]
        case _:
            return None


def primes_generator(no_of_primes):
    index = 2
    check_if_prime = 2
    prime_list = []
    is_prime = True
    if no_of_primes == 0:
        return prime_list
    while len(prime_list) < no_of_primes:
        while index <= check_if_prime / 2:
            if check_if_prime % index == 0:
                is_prime = False
            index += 1
        if is_prime:
            prime_list.append(check_if_prime)
        check_if_prime += 1
        is_prime = True
        index = 2
    return prime_list


def is_empty_vector(vec_lst):
    if len(vec_lst) < 1:
        return True
    for i in range(len(vec_lst)):
        if len(vec_lst[i]) == 0:
            return True
    return False


def vectors_list_sum(vec_lst):
    number_of_vectors = len(vec_lst)
    total = 0
    total_list = []
    if is_empty_vector(vec_lst):
        return True
    for i in range(len(vec_lst[0])):
        for j in range(number_of_vectors):
            if len(vec_lst[0]) != len(vec_lst[j]):
                return 0
            total += vec_lst[j][i]
        total_list.append(total)
        total = 0
    return total_list


def calc_the_inner_product(vec_1, vec_2):
    product = 0
    if len(vec_1) != len(vec_2):
        return None
    if len(vec_1) == 0 and len(vec_2) == 0:
        return 0
    for i in range(len(vec_1)):
        product += vec_1[i] * vec_2[i]
    return product


def orthogonal_number(vectors):
    count = 0
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            product = calc_the_inner_product(vectors[i], vectors[j])
            if product == 0:
                count = count + 1
    return count