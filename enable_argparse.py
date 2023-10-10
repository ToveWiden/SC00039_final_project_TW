import argparse
import project_script as ps





# Main function
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-fn", "--filename", action="store", help="filename")
    parser.add_argument("-rmd", "--removeduplicates", action="store", nargs="?",default='Yes', help="Optional. Remove duplicates: 'Yes' or 'No', default='Yes'")
    parser.add_argument("-CBMs", "--include_CBMs", nargs="?", action="store", default='Yes', help="Optinal. Include CBMs: 'Yes' or 'No', default='Yes'")
    parser.add_argument("-Dom", "--Domain", action="store", nargs="?", default='All', help="Optinal. Domain of interest: 'All','Archaea','Bacteria', 'Eukaryota' or 'Viruses', default='All' ")
    parser.add_argument("-St", "--Strain", action="store", nargs="?", default='All', help="Optional. Strain of interest . e.g. 'Aspergillus flavus AF13'. default='All'")
    parser.add_argument("-min", "--min_domains", action="store", nargs="?", default=0, type=float, help="Optional. Minimum number of domains included in plot. float. default=0")
    parser.add_argument("-max", "--max_domains", action="store", nargs="?", default=float('inf'), type=float, help="Optional. Maximum number of domains included in plot. default=float('inf')")
    args = parser.parse_args()
    df = ps.read_cazy_file(args.filename)
    print('df created')
    if args.removeduplicates == 'Yes':
        df = ps.remove_faulty_duplicates(df)
        print('duplicates removed')
    else: 
        print('No duplicates removed')
    df_subset = ps.make_subset(df,args.include_CBMs,args.Domain,args.Strain)
    print('subset created')
    ps.count_domains(df_subset,args.min_domains, args.max_domains)
    print('Plot plotted')



if __name__ == "__main__":
    main()