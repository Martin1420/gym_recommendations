from data import *
from welcome import *
from linkedlist import LinkedList

print_welcome()


# Write code to insert gym types into a data structure (LinkedList) here. The data is in data.py
def insert_gym_categories():
    gym_category_list = LinkedList()
    for category in categories:
        gym_category_list.insert_beginning(category)
    return gym_category_list


# Write code to insert gym data into a data structure (LinkedList of LinkedLists) here. The data is in data.py
def insert_gym_data():
    gym_data_list = LinkedList()
    for category in categories:
        gym_sublist = LinkedList()
        for gym in gym_data:
            if gym[0] == category:
                gym_sublist.insert_beginning(gym)
        gym_data_list.insert_beginning(gym_sublist)
    return gym_data_list



my_gym_type_list = insert_gym_categories()
my_gym_list = insert_gym_data()


selected_gym_type = ""

# Write code for user interaction here
while len(selected_gym_type) == 0:
    user_input = str(input(
        "\nWhat type of gym would you like to go to?\nType the beginning of that gym type and press enter to see if "
        "it's here.\n")).lower()

    # Search for user_input in gym types data structure here
    matching_types = []
    type_list_head = my_gym_type_list.get_head_node()
    while type_list_head is not None:
        if str(type_list_head.get_value()).startswith(user_input):
            matching_types.append(type_list_head.get_value())
        type_list_head = type_list_head.get_next_node()

    # print list of matching gym types
    for gym_type in matching_types:
        print(gym_type)

    # Check if only one type of gym was found, ask user if they would like to select this type
    if len(matching_types) == 1:
        select_type = str(input(
            "\nThe only matching type for the specified input is " + matching_types[0] + ". \nDo you want to look at " +
            matching_types[0] + " gyms? Enter y for yes and n for no\n")).lower()

        # After finding gym type write code for retrieving gym data here
        if select_type == 'y':
            selected_gym_type = matching_types[0]
            print("Selected Gym Type: " + selected_gym_type)
            gym_list_head = my_gym_list.get_head_node()
            while gym_list_head.get_next_node() is not None:
                sublist_head = gym_list_head.get_value().get_head_node()
                if sublist_head.get_value()[0] == selected_gym_type:
                    while sublist_head.get_next_node() is not None:
                        print("--------------------------")
                        print("Name: " + sublist_head.get_value()[1])
                        print("Price: " + sublist_head.get_value()[2] + "/5")
                        print("Rating: " + sublist_head.get_value()[3] + "/5")
                        print("Address: " + sublist_head.get_value()[4])
                        print("--------------------------\n")
                        sublist_head = sublist_head.get_next_node()
                gym_list_head = gym_list_head.get_next_node()

            # Ask user if they would like to search for other types of gyms
            repeat_loop = str(input("\nDo you want to find other gyms? Enter y for yes and n for no.\n")).lower()
            if repeat_loop == 'y':
                selected_gym_type = ""