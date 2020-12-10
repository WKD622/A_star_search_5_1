from data import init_state, available_steps, available_jumps
from helpers import init_node, is_goal, make_step, operation_valid, elem_to_move, make_jump, count_idx_of_step, \
    count_idx_of_jump, not_closed, finish, state_to_string

closed = []
init_n = init_node(init_state, 0, [])
opened = [init_n]
distances = {state_to_string(init_state): 0}

while len(opened) > 0:
    opened.sort(key=lambda node: node['f'], reverse=True)
    fi = opened.pop()
    current_state = fi['state']
    current_state_str = state_to_string(current_state)

    if not_closed(closed, current_state) or (
            current_state_str in distances and fi['g'] < distances.get(current_state_str)):

        closed.append(current_state)
        distances[current_state_str] = fi['g']

        if is_goal(current_state):
            finish(fi)

        else:
            for current_index, elem in enumerate(current_state):
                if elem_to_move(elem):
                    for step in available_steps:
                        new_index = count_idx_of_step(current_index, step)
                        if operation_valid(current_state, new_index):
                            cost, new_state = make_step(fi['state'], current_index, step)
                            predecessors = fi['predecessors'][:]
                            predecessors.append(current_state)
                            opened.append(init_node(new_state, fi['g'] + cost, predecessors))

                    for jump in available_jumps:
                        new_index = count_idx_of_jump(current_index, jump)
                        if operation_valid(current_state, new_index):
                            cost, new_state = make_jump(fi['state'], current_index, jump)
                            predecessors = fi['predecessors'][:]
                            predecessors.append(current_state)
                            opened.append(init_node(new_state, fi['g'] + cost, predecessors))
