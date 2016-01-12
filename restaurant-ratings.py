# your code goes here
import sys 

def create_restaurant_dictionary(filename):
    """Read in the restaraunt list and create a big dic matching the 

    resaraunt to its rating"""

    restaurant_dictionary = {} #create dictionary
    restaurant_file = open(filename) #open file
    for restaurant in restaurant_file: #for each restaraunt 
        restaurant = restaurant.strip() #removes whitespace
        restaurant_info = restaurant.split(":") #separate restaraunt and rating
        restaurant_name = restaurant_info[0] #1st entry is name
        restaurant_rating = restaurant_info[1] #2nd entry is rating
        restaurant_dictionary[restaurant_name] = restaurant_rating 
    
    return restaurant_dictionary

        

            
def alphabetize_restaurant_dictionary(dictionary):
    """Pass in dictionary, and sort its indexes in alphabetical order. 

    Return dictionary."""

    list_dictionary = dictionary.keys()

    sorted_list = sorted(list_dictionary)
    return sorted_list

#can use the keys method to create a list 

def print_sorted_dictionary(sorted_list, dictionary):
    """Print the sort of big dic"""

    for restaurant in sorted_list:
        print "%s is rated at %s." %(restaurant, dictionary[restaurant])
    




temp_dictionary = create_restaurant_dictionary(sys.argv[1])
temp_list = alphabetize_restaurant_dictionary(temp_dictionary) 
print_sorted_dictionary(temp_list, temp_dictionary)