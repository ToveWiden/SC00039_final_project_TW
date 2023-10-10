# SC00039_final_project_TW

## Background - Analysis of CAZy database download file
[CAZy](cazy.org) is a database for carbohydrate active enzymes. 
It classifies proteins and predicted proteins into enzyme familes based on their amino acid sequence. 
A protein can contain multiple domains that may or may not belong to different enzyme families. The families are glycoside hydrolases (GH),glycosyltransferases (GT), polysaccharide lyases (PL), carbohydrate esterases (CE) and auxilary activities (AA). A special case of classification are the proteins classified as Carbohydrate binding modules (CBMs) which are not enzymes since they have no catalytic mechanim, but still provide important functions in carbohydrate degradation and therefor is included in the database. 
In this script we want to investigate the presence of multidomain or multicatalytic enzymes. 

## Contents
There are two sctipts in the repo, project_script.py and enable_argparse.py. 
There is also a file with test data called test_data.txt. 

The script project_script.py contains a set of functions and can be imported as a module and used to analyze a data file downloaded from CAZy (or the test_data.txt).
The script enable_argparse.py can be run from command line and imports and runs the functions from project_script.py as a complete workflow. 

The datafile should be a tsv file without a header, containing columns describing Family, Domain, Strain and Protein. 

This is an example of a row: 

AA5_2    Eukaryota    Aspergillus flavus AF13    QMW46863.1

## How to run from command-line

### How to run
    python enable_argparse.py -fn 'test_data.txt'

### Arguments
    -h prints help message
    -fn filename 
    -rmd Optional. Remove duplicates: 'Yes' or 'No', default='Yes'
    -CBMs Optinal. Include CBMs: 'Yes' or 'No', default='Yes'
    -Dom Optinal. Domain of interest: 'All','Archaea','Bacteria', 'Eukaryota' or 'Viruses', default='All'
    -St Optional. Strain of interest . e.g. 'Aspergillus flavus AF13'. default='All'
    -min Optional. Minimum number of domains included in plot. float. default=0
    -max Optional. Maximum number of domains included in plot. default=float('inf')

### Example 1 
     python enable_argparse.py -fn 'test_data.txt'

### Example 2
    python enable_argparse.py -fn 'test_data.txt' -CBMs 'No' -Dom 'Bacteria'
    
### Example 3
    python enable_argparse.py -fn 'test_data.txt' -St 'Aspergillus flavus AF13' -min 0 -max 4
    
## Details on the different functions

### read_cazy_file(filename)
This function takes the filename as an argument and creates a pandas dataframe with an appropriate header that can be used for further analysis. 

**Example:** 

    df = read_cazy_file('cazy_data.txt')

### remove_faulty_duplicates(df)
As it is now the file downloaded from the CAZy database contains some double entries. Some enzyme families have subefamilies and these seems to have been added to the file twice, once all the entries in the whole familiy (eg. GH5) has been added, and then all of the entries for all of the subfamilies (e.g. GH5_1, GH5_2...) have been added again. This function is used to remove some of the redundant entries. 

The function takes a pandas dataframe as argument and returns a new pandas dataframe. 

**Example:** 

    df = remove_faulty_duplicates(df)

### make_subset(df, include_CBMs='Yes', Domain='All', Strain='All')
This function enables filtering of the dataframe. The default is to include everything and would return the same dataframe. 
The function takes a dataframe as argument and returns a new dataframe. It also takes keyword arguments for filtering conditions. 

include_CBMs can be 'Yes' or 'No'

Domain can be 'All' or the domain of interest, either of 'Archaea','Bacteria', 'Eukaryota' or 'Viruses'. 

Strain can be 'All' or the strain of interest e.g. 'Aspergillus flavus AF13'


**Example 1:** 

    df_subset = make_subset(df, include_CBMs='No', Domain='Bacteria')

**Example 2:** 

    df_subset = make_subset(df, include_CBMs='Yes', Strain = 'Aspergillus flavus AF13')

### count_domains(df,min_domains = 0, max_domains = float('inf'))
This function plots the number of domains of the proteins in the dataframe. The number of domains are on the x-axis and the count of how many proteins there are that contains that many domains are on the y-axis. 
It takes a dataframe as an argument as well as the minimum or maximum number of domains per proteins that you want to include in the plot. The default is to include everything. 

**Example:** 

    count_domains(df,min_domains = 2, max_domains = 10)


