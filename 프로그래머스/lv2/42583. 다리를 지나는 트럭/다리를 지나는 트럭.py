def solution(bridge_length, weight, truck_weights):
    stack_bridge = [0] * bridge_length
    time = 0
    while stack_bridge:
        time += 1
        stack_bridge.pop(0)
        if truck_weights:
            if sum(stack_bridge) + truck_weights[0] <= weight:
                stack_bridge.append(truck_weights.pop(0))
            else:
                stack_bridge.append(0)
    return time