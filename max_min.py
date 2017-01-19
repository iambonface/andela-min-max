"""
 	Function to return maximum, minimum and length of the list
 	Args:
 	    Pass arguments to function

 	Results:
 	 	if maximum and minimum item in list is same, return length of the_list, 
 	 	else return a list with minimum and maximum values

"""

def find_max_min(the_list):
    if isinstance(the_list, list):
        if min(the_list) == max(the_list):
            """ checking equality"""
            return len(the_list)
        listx = []
        listx.append(min(the_list))
        listx.append(max(the_list))

        return listx

        


