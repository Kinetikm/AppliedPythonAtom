def find_indices(input_list, n):
    sup_dict = {}
    for i in range(len(input_list)):
         if input_list[i] in sup_dict:
             return sup_dict.get(input_list[i]), i
         else:
             sup_dict[n - input_list[i]] = i
    return None