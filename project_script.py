######## import packages #########
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

######### read the cazy file ########
def read_cazy_file(filename):
    df = pd.read_table(filename, header=None) #make into pandas df
    df.columns = ['Family','Domain','Strain','Protein'] #Creates a header
    return df

######### Remove duplicates that shouldn't be there #########
#The file downloaded from the cazy database contains some redundancy. Because I want to look
#at occurences where there are several enzyme families connected to the same protein
#the duplicate rows that should not be in the file needs to be removed. 
#They cannot be removed simply by df.drop_duplicate() because that would also remove
#duplicates that should be in the file. 
#Correct duplicates are almost always consecutive. The could be non consecutive if 
#there are several subfamilies but the same family in the same protein. Then some 
#extra rows will be kept. This will be good enough for now. 

def remove_faulty_duplicates(df):
    df['consecutive_protein'] = (df.groupby(df['Protein'].ne(df['Protein'].shift()).cumsum()).cumcount() + 1) #Counts the number of consecutive proteins in the rows and writes it in a new column
    df2=df.drop_duplicates() #removes the duplicates based on all columns, correct duplicates (consecutive ones) will therefore be kept
    df3=df2[['Family','Domain','Strain','Protein']]
    return df3
################################################

#filter if wanted
def make_subset(df, include_CBMs='Yes', Domain='All', Strain='All'):
    if include_CBMs == 'Yes':
        df1=df
    elif include_CBMs == 'No':
        df1 = df[~df['Family'].str.startswith('CBM')] #creates a dataframe without the entries where the family is a CBM
    else:
        print('write "Yes" or "No"')  
    if Domain == 'All':
        df2 = df1
    else:
        df2 = df1[df1.Domain == Domain] #filters with the selected domain
    if Strain == 'All':
        df_subset = df2
    else:
        df_subset = df2[df2.Strain == Strain] #filters with the chosen strain
    return df_subset
    
#check how many domains each protein have, taking a df, the minimum and maximum number of domains you want to include
#plotting the number of domains against number of proteins 
def count_domains(df,min_domains = 0, max_domains = float('inf')):
    counts = df['Protein'].value_counts()
    counts_df = pd.DataFrame(counts)
    counts_df = counts_df.reset_index(level=0)
    counts_df.columns = ['Protein', 'Number of Domains']
    number_of_domains = counts_df['Number of Domains'].value_counts()
    number_of_domains_df = pd.DataFrame(number_of_domains)
    number_of_domains_df = number_of_domains_df.reset_index(level=0)
    number_of_domains_df.columns = ['Number of Domains','Count']
    number_of_domains_df_subset = number_of_domains_df[(number_of_domains_df['Number of Domains'] >= min_domains) & (number_of_domains_df['Number of Domains'] <= max_domains)]
    g = sns.barplot(x=number_of_domains_df_subset['Number of Domains'], y=number_of_domains_df['Count'])
    g.set_yscale("log")
    g.set(xlabel="Number of Domains per protein", ylabel="Protein count")
    plt.draw()
    plt.show()
