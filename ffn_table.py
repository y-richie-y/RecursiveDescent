non_term = [chr(ord('A')+i) for i in range(26)]
non_term += [x + "_" for x in non_term]

def compute_ffn(var):
    first = dict()
    nullable = dict()
    follow = dict()

    term = set()
    for key in var:
        for deriv in var[key]:
            for token in deriv:
                if token not in non_term:
                    term.add(token)

    term = list(term)

    for key in var:
        first[key] = set()
        follow[key] = set()
        nullable[key] = False

    for key in term:
        first[key] = set()
        first[key].add(key)
        follow[key] = set()
        nullable[key] = False
    
    nullable[""] = True

    flag = True
    while flag:
        flag = False
        for key in var:
            for deriv in var[key]:
                can_null = True
                for token in deriv:
                    if token not in non_term:
                        can_null = False
                    else:
                        can_null &= nullable[token]

                if not nullable[key] and can_null:
                    flag = True
                    nullable[key] = True
                
                k = len(deriv)
                for i in range(k):
                    # rule 1
                    prev_len = len(first[key])

                    all_nullable = True
                    for l in range(i):
                        all_nullable &= (deriv[l] in non_term and nullable[deriv[l]])

                    if all_nullable:
                        first[key] |= first[deriv[i]]

                    flag |= prev_len != len(first[key])

                    # rule 2
                    prev_len = len(follow[deriv[i]])

                    all_nullable = True
                    for l in range(i+1, k):
                        all_nullable &= (nullable[deriv[l]])
                    
                    if all_nullable:
                        follow[deriv[i]] |= follow[key]

                    for j in range(i+1, k):
                        # rule 3
                        all_nullable = True
                        for l in range(i+1, j):
                            all_nullable &= (nullable[deriv[l]])
                        
                        if all_nullable:
                            follow[deriv[i]] |= first[deriv[j]]

                        flag |= prev_len != len(follow[deriv[i]])
    return (first, follow, nullable)
