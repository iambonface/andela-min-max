

def find_max_min(the_list):
	if isinstance(the_list, list):

		convert_to_set = set(the_list)

		set_to_list = list(convert_to_set)

		length_of_list = len(set_to_list)


		minimum = set_to_list[0]

		maximum = set_to_list[length_of_list-1]

		new_list = [minimum, maximum]

		return new_list

