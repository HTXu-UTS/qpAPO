import csv
import numpy as np

#============================================================================================
'''
写入：幕序号、每一幕的时间步数、累计的时间步数、累计运行时间、每一幕的奖励
'''
def write_results_to_csv(fn, episode_list, epistep_list, allstep_list, time_list, return_list):
#

    with open(fn, "w", encoding="utf-8", newline="") as csvFile:
        writer = csv.writer(csvFile)       #创建写的对象
        #先写入columns_name                             
        writer.writerow(["No","EpiSteps",
                     "AllSteps",
                     "Time",
                     "Returns"])     #写入列的名称
        writer.writerows(np.transpose([episode_list, epistep_list, allstep_list, \
                                       time_list, return_list]))
         
        csvFile.close()
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------