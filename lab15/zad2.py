def merge_stacks(stack1, stack2):
    result = []

    i, j = 0, 0
    
    while i < len(stack1) and j < len(stack2):
        if stack1[i] < stack2[j]:
            result.append(stack1[i])
            i += 1
        else:
            result.append(stack2[j])
            j += 1

    while i < len(stack1):
        result.append(stack1[i])
        i += 1
    
    while j < len(stack2):
        result.append(stack2[j])
        j += 1
    
    return result

stack1 = [1, 3, 5]
stack2 = [2, 4, 6]

merged_result = merge_stacks(stack1, stack2)
print(merged_result)