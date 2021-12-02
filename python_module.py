# The script MUST contain a function named azureml_main
# which is the entry point for this module.

# imports up here can be used to
import pandas as pd

# The entry point function MUST have two input arguments.
# If the input port is not connected, the corresponding
# dataframe argument will be None.
#   Param<dataframe1>: a pandas.DataFrame
#   Param<dataframe2>: a pandas.DataFrame
def azureml_main(dataframe1 = None, dataframe2 = None):

    # Execution logic goes here
    df_updated = dataframe1[['New Cases','New Deaths','Province']]
    
    # df_updated
    data_index = df_updated['Province'].value_counts()
    
    # new_dataframe consist of 33 rows (province)
    list_province = []
    for row in data_index.index:
        list_province.append(row)
    list_new_cases = []
    list_new_deaths = []
    for x in list_province:
        df_list = df_updated.loc[df_updated['Province'] == x]
        new_list = df_list.sum(axis=0)
        list_new_cases.append(new_list['New Cases'])
        list_new_deaths.append(new_list['New Deaths'])


    covid_data = {'New Cases':list_new_cases,
                'New Deaths':list_new_deaths,
                'Province': list_province
                }
    df_final1 = pd.DataFrame(covid_data)
    df_final2 = pd.DataFrame(covid_data)
    
    return df_final2,df_final2
