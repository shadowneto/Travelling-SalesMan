import pandas as pd

#Generate a list of all possible combinations of cities that can be visisted

from itertools import product

cities = ["Ottawa", "Montreal", "Kingston", "Toronto", "Sudbury"]
cities_set = list(product(cities, repeat = 5))

city_set = []
for x in cities_set:
    lst = set(x)
    if len(lst) == 5:
        city_set.append(list(lst))


#print(cities_set[0])
#print(city_set[0])



all_costs = []
all_paths = []

#An array of each cit`y and the distance to other cities
arr_1 = [
    {"Ottawa" : {
        "Montreal" : 199,
        "Kingston": 196,
        "Toronto" : 450,
        "Sudbury": 484
    }},

    {
        "Montreal" : {
            "Ottawa" : 199,
            "Kingston" : 287,
            "Toronto" : 542,
            "Sudbury" : 680
        }},

    {
        "Kingston" : {
            "Ottawa" : 196,
            "Montreal" : 287,
            "Toronto" : 263,
            "Sudbury" : 634

        }
    },

    {
        "Toronto" : {
            "Ottawa" : 450,
            "Montreal" : 542,
            "Kingston" : 263,
            "Sudbury" : 400
        }
    },

    {
        "Sudbury" : {
            "Ottawa" : 484,
            "Montreal" : 680,
            "Kingston" : 634,
            "Toronto" : 400
        }
    }
]





def find_min_path(list):
    el_1 = list[0]
    el_2 = list[1]
    el_3 = list[2]
    el_4 = list[3]
    el_5 = list[4]
    el_6 = list[0]

    pairs = [[el_1, el_2],[el_2, el_3], [el_3, el_4], [el_4 , el_5], [el_5, el_6], [el_6, el_1]]


    #encode each city with an index
    encoded_city = {"Ottawa": 0, "Montreal": 1, "Kingston":2, "Toronto":3, "Sudbury":4}
    
    pairs_idx = 0
    path_cost = 0
    while pairs_idx < 6:
        fro_ = pairs[pairs_idx][0]
        to_ = pairs[pairs_idx][1]

        city_idx_lst = [value for key, value in encoded_city.items() if key == fro_]
        city_idx = city_idx_lst[0]
        path_1 = arr_1[city_idx]

        for key, value in path_1.items():
            for key, value in value.items():
                if key == to_:
                    path_cost +=value

        pairs_idx += 1
    all_paths.append(list)
    return path_cost
    


current_city_set_idx = 0
while current_city_set_idx < len(city_set):
    cost = find_min_path(city_set[current_city_set_idx])
    all_costs.append(cost)
    current_city_set_idx += 1
    

path_and_cost = zip(all_paths, all_costs)
my_dataframe = pd.DataFrame(path_and_cost)

min_cost = min(all_costs)
best_path = all_paths[all_costs.index(min_cost)]
print(min_cost)
print(best_path)

#print(my_dataframe.head(10).sort_values(by=1, ascending=True))

## 0  [Toronto, Ottawa, Kingston, Montreal, Sudbury]  2013

