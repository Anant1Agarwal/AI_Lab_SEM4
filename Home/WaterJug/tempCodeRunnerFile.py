 if current_state == goal:
            path = [current_state]
            while parent_state is not None:
                path.append(parent_state[0])
                parent_state = parent_state[1]
            path.reverse()
            return path