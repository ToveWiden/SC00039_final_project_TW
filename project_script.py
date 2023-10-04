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
def make_subset(df, include_CBMs=True ,**Domain,**Strain):
    if include_CBMs == False:
        df1 = df[~df['Family'].str.startswith('CBM')] #creates a dataframe without the entries where the family is a CBM
    else:
        df1=df
    if Domain = True:
        df2 = df1[df1.Domain == Domain] #creates a df with the selected domain
    else:
        df2 = df1
    if Strain = True:
        df_subset = df2[df2.Strain == Strain]
    else:
        df_subset = df2
    return df_subset
    
    
df_subset_bacteria = noCBMs_df[noCBMs_df.Domain == 'Bacteria'] #creates a df with the selected domain
df_subset_strain = noCBMs_df[noCBMs_df.Strain == 'Bacteroides thetaiotaomicron 7330'] #creates df with the selected strain
#sort on protein
#number entries per protein
#
a=df_subset_noCBMs.sort_values('Protein') #sorts df based on protein name
a['entries'] = (a.groupby(
    a['Protein'].ne(a['Protein'].shift()).cumsum()
).cumcount() + 1) #adds a column where each entry with the same protein gets a number

b=a.sort_values('entries')


counts = a['Protein'].value_counts()
counts_df = pd.DataFrame(counts)
counts_df = counts_df.reset_index(level=0)
counts_df.columns = ['Protein', 'Number of Domains']
number_of_domains = counts_df['Number of Domains'].value_counts()
number_of_domains_df = pd.DataFrame(number_of_domains)
number_of_domains_df = number_of_domains_df.reset_index(level=0)
number_of_domains_df.columns = ['Number of Domains','Count']
number_of_domains_df_subset = number_of_domains_df[(number_of_domains_df['Number of Domains'] >=0) & (number_of_domains_df['Number of Domains'] <= float('inf'))]


#plots a barplot how many proteins there are with 1 domains, 2 domains etc.
g = sns.barplot(x=number_of_domains_df_subset['Number of Domains'], y=number_of_domains_df['Count'])
g.set_yscale("log")
g.set(xlabel="Number of Domains", ylabel="Count")
plt.show()




#Enable different filtering options
## make a function that takes different argumets
##Organism
##Enzyme family 
##Exclude CBMs 

#org_df = duplicate_free_df[duplicate_free_df.Strain == 'Caldicellulosiruptor saccharolyticus DSM 8903']
#enz_df = duplicate_free_df[duplicate_free_df.Family == 'GH10']
#no_CBM_df = duplicate_free_df[~duplicate_free_df['Family'].str.startswith('CBM')]

#organism
#sort on protein
####a=enz_fam.sort_values('Protein')

#number 
#count the occurrance of each number, no of 1s, no of 2s etc. 
#plot distribution in barplot
# most common combo
# heatmap (needs some kind of subset or too much data)


#filtering on enz_fam
#cant just filter
#need to select all protein codes from the whole df that are present in selected family
# count the occurrance of each number, no of 1s, no of 2s etc. 
# Barplot of x most common enz_fams connected to the selected enz_fam



#Visualization

#heatmaps
#class vs classes GH, PL etc. 
#select class vs class ex. GH vs PL
# all families vs all families in the organisms
# One family vs everything its connected to? 
#custom list vs custom list
