import numpy as np

# how many missing values exist or better still what is the % of missing values in the dataset?
def percent_missing(df):

    # Calculate total number of cells in dataframe
    totalCells = np.product(df.shape)

    # Count number of missing values per column
    missingCount = df.isnull().sum()

    # Calculate total number of missing values
    totalMissing = missingCount.sum()

    # Calculate percentage of missing values
    print("The  dataset contains", round(((totalMissing/totalCells) * 100), 2), "%", "missing values.")


def convert_yes_no(df,colname:str):
    df[colname].replace(['No','Yes'],[0,1],inplace=True)

def convert(df,colname:str,val:str,val2:str,res,res2):
    df[colname].replace([val,val2],[res,res2],inplace=True)

def fill_null(df,col,val):
    df[col] = df[col].fillna(val)