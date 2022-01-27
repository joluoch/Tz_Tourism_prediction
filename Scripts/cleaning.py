def convert_yes_no(df,colname:str):
    df[colname].replace(['No','Yes'],[0,1],inplace=True)

def convert(df,colname:str,val:str,val2:str,res,res2):
    df[colname].replace([val,val2],[res,res2],inplace=True)