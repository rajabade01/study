from asammdf import MDF

with MDF(r'C:\git\MDF_4_1_01_20200103_101149.mf4') as mdf_file:
    df = mdf_file.to_dataframe()
    #signals = mdf_file.extract_can_logging('C:\git\MDF_4_1_01_20200103_101149.mf4')
    df.to_csv("file1.csv", sep='\t', encoding='utf-8')
    mdf_file.export(fmt='csv', filename='file2.csv')

    #mdf_file.export(fmt='excel', filename='filename3.xlsx')


    print(mdf_file.version)
    mdf_file.export(fmt='xls', filename='filename2.xls')