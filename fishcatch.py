'''
Description:
<This program contains a separate function,
one that will write out a fishy dictionary containing
the fish' name, and average mass in grams >
'''



def fish_dict_from_file(file_name):

    fishy_dict = {'1': "Bream", '2': "Whitefish", '3': "Roach", '4': "?", '5': "Smelt", '6': "Pike", '7': "Perch"}

    fishy_data = {}

    fishy_data_file = open(file_name, "r")


    for line in fishy_data_file:
        data = line.strip().split()
        if "NA" == data[2]:
            pass
        else:
            key, values = data[1], data[2]
            if fishy_dict[key] not in fishy_data:
                fishy_data[fishy_dict[key]] = [float(values)]
            else:
                fishy_data[fishy_dict[key]].append(float(values))


    return fishy_data





#==========================================================
def main():
    fishy_info = fish_dict_from_file("fishcatch.dat")

    print ("#".rjust(4, " ") , "NAME".ljust(10, " ") , "MEAN WT".rjust(10, " "))

    for key in sorted(fishy_info) :
        fishy_reference = key
        value = fishy_info[key]
        count = len(value)
        average_weight = round((sum(fishy_info[key]) / len(fishy_info[key])), 1)

        print(str(count).rjust(4, " ") , fishy_reference.ljust(10, " ") + str(average_weight).rjust(10, " ") + "g".rjust(0, " "))

    





    
