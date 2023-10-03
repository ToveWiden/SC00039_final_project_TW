######## import packages #########
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

######### read the cazy file ########
df = pd.read_table('cazy_data.txt', header=None) #make into pandas df
df.columns = ['Family','Domain','Strain','Protein'] #Creates a header
df.head(10)

######### Remove duplicates that shouldn't be there #########
#The file downloaded from cazy contains some redundancy. Because I want to look
#at occurences where there are several enzyme families connected to the same protein
#the duplicate rows that should not be in the file needs to be removed. 
#They cannot be removed simply by df.drop_duplicate() because that would also remove
#duplicates that should be in the file. 
#Correct duplicates are almost always consecutive. The could be non consecutive if 
#there are several subfamilies but the same family in the same protein. Then some 
#extra rows will be kept. This will be good enough for now. 
df['consecutive_protein'] = (df.groupby(
    df['Protein'].ne(df['Protein'].shift()).cumsum()
).cumcount() + 1) #Counts the number of consecutive proteins in the rows and
#writes it in a new column

duplicate_free_df = df.drop_duplicates() #removes the duplicates based on 
#all columns, correct duplicates (consecutive ones) will therefore be kept
duplicate_free_df
df_D = duplicate_free_df[['Family','Domain','Strain','Protein']]
df_D.head()

################################################

#filter if wanted
noCBMs_df = df_D[~df_D['Family'].str.startswith('CBM')]
#cazymes_bacteria = cazy_organisms[cazy_organisms.Domain == 'Bacteria']
#sort on protein
#number entries per protein
#
a=noCBMs_df.sort_values('Protein')
a['entries'] = (a.groupby(
    a['Protein'].ne(a['Protein'].shift()).cumsum()
).cumcount() + 1)

b=a.sort_values('entries')


counts = b['Protein'].value_counts()
counts_df = pd.DataFrame(counts)
counts_df = counts_df.reset_index(level=0)
counts_df.columns = ['Protein', 'Number of Domains']
#counts_df.head()
number_of_multicats = counts_df['Number of Domains'].value_counts()
number_of_multicats_df = pd.DataFrame(number_of_multicats)
number_of_multicats_df = number_of_multicats_df.reset_index(level=0)
number_of_multicats_df.columns = ['Number of Domains','Count']
number_of_multicats_df
sns.displot(data=counts_df, x="Number of Domains",log_scale = (False, True))

noCBMs_df.head()
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
