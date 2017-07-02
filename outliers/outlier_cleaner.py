#!/usr/bin/python
#coding=utf-8
import numpy as np
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    predictionsNP = np.array(predictions)#预测值
    net_worthsNP = np.array(net_worths)#实际值

    errors = np.abs(predictionsNP - net_worthsNP)#错误


    # multiValueList = []
    # for index in range(len(ages)):
    #
    #     age = ages[index][0]
    #     net_worth = net_worths[index][0]
    #     error = errors[index][0]
    #     oneLine = {'age':age,"net_worth":net_worth,"error":error}
    #     multiValueList.append(oneLine)
    #
    # print(np.array(multiValueList))
    cleaned_data = []


    ### your code goes here

    
    return cleaned_data

