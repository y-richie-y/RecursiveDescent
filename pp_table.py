non_term = [chr(ord('A')+i) for i in range(26)]
non_term += [x + "_" for x in non_term]

def compute_pp(var, first, follow, nullable):
    table = dict()

    term = filter(lambda x: x not in non_term, first.keys())

    for key in var:
        table[key] = dict()
        for val in term:
            table[key][val] = []

    for key in var:
        for deriv in var[key]:
            for val in term:
                add = False
                all_nullable = True
                for token in deriv:
                    if val in first[token]:
                        add = True
                    elif not nullable[token]:
                        all_nullable = False
                        break

                if add or (val in follow[key] and all_nullable):
                    table[key][val].append(deriv)

    return table
