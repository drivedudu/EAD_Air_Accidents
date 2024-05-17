import pandas as pd

def fill0(data):
    data = data.fillna(0)
    return data

def tpint(data):
    data = data.astype(int)
    return data

def tpdate(data):
    data = pd.to_datetime(data,  format='%Y-%m-%d')
    return data

def fillstr(data, string):
    data = data.fillna(string)
    return data

def filter_accidents_by_decade(data):
    Filter_10_df = pd.DataFrame()
    
    # Getting the initial and final year of the data
    start_year = data['Event.Date'].dt.year.min()
    end_year =   data['Event.Date'].dt.year.max()
    
    # Iterating every 10 years
    for year in range(start_year, end_year + 1, 10):
       
        # Filtering rows for the 10-year interval        
        if (year + 10) > end_year:
            year_last = end_year
        else:
            year_last = year + 10

        result_10_years_df = data.query('@year <= `Event.Date`.dt.year < @year_last')

        # Calculating the total number of accidents
        total_accidents = result_10_years_df['Accident.Number'].nunique()

        # Creating a new DataFrame with the results
        new_result_df = pd.DataFrame({'start_year': year, 
                                      'end_year': year_last, 
                                      'total_of_accidents': total_accidents},
                                     index=[0])
        Filter_10_df = pd.concat([Filter_10_df, new_result_df])
    
    # Resetting the indices of the new DataFrame
    Filter_10_df.reset_index(drop=True, inplace=True)
    return Filter_10_df