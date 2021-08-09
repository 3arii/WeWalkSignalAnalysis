
#TODO: Read a single row from the OrientationDataGood csv file
#      Create a list that is the length of the read row containing numbers.
#      Create a list that will contain the second list and the initial csv file but seperated with commas
#      Create a for loop that will print them seperately to another .csv file.

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
from data import data

index_data = []
vertex_data = []
final_data = []
vertex_string = ""

data = data[0].split(",")

def get_len_list(data_list):
  for num in range(len(data_list)):
    index_data.append(num)
  
  return index_data

def get_final_data(data_list, index_data):
  vertex_string = "" 
  for num in range(len(data_list)):
    vertex_string = f"{index_data[num]},{data_list[num]}"
    final_data.append(vertex_string)
    vertex_string = ""
  
  return final_data

def write_lines(text_file, final_data):
  file1 = open(text_file, "a")
  file1.truncate(0)

  for num in range(len(final_data)):
    file1.writelines(f"{final_data[num]}\n" )
  
  file1.close

def write_acc_data(data, data_file):
  index_data = get_len_list(data)
  final_data = get_final_data(data, index_data)
  write_lines(data_file, final_data)

def write_comp_data(data):
  index_data = get_len_list(data)
  final_data = get_final_data(data, index_data)
  write_lines("CompData.txt", final_data)

def write_gyro_data(data):
  index_data = get_len_list(data)
  final_data = get_final_data(data, index_data)
  write_lines("GyroData2.txt", final_data)

write_acc_data(data, "AccDataBroken.txt")

