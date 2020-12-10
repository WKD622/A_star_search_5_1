from data import max_size


def switch(state, index_1, index_2):
    new_state = state[:]
    pom = new_state[index_2]
    new_state[index_2] = new_state[index_1]
    new_state[index_1] = pom
    return new_state


def operation_valid(state, new_index):
    return max_size - 1 >= new_index >= 0 and state[new_index] == '_'


def is_goal(state):
    return count_h(state) == 0


def count_idx_of_step(current_index, step):
    new_index = current_index + step
    return new_index


def count_idx_of_jump(current_index, jump):
    new_index = current_index + int(jump / abs(jump)) + jump
    return new_index


def make_step(state, current_index, step):
    new_index = current_index + step
    return abs(step), switch(state, current_index, new_index)


def make_jump(state, current_index, jump):
    new_index = current_index + int(jump / abs(jump)) + jump
    return abs(jump), switch(state, current_index, new_index)


def count_h(state):
    h = 0
    counter = 0
    for idx_1, elem in enumerate(state):
        if counter == 2:
            return h
        if elem == 'x':
            counter += 1
            for idx in range(idx_1, max_size):
                if state[idx] == 'o':
                    h += 1
    return h


def init_node(state, g, predecessors):
    h = count_h(state)
    return {
        'state': state,
        'g': g,
        'h': h,
        'f': h + g,
        'predecessors': predecessors,
    }


def elem_to_move(elem):
    return elem == 'o' or elem == 'x'


def not_closed(closed, state):
    return state not in closed


def finish(fi):
    predecessors = fi['predecessors']
    predecessors.append(fi['state'])
    print("solution:  " + str(predecessors))
    exit(0)


def state_to_string(state):
    return ''.join(state)
