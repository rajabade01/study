from asammdf import MDF
import csv
mdf = MDF('C:\git\Test\MDF_4_1_01_20200103_101149.mf4')
with open('innovators.csv', 'w', newline='') as file:
   writer = csv.writer(file)
   writer.writerow(mdf.channels_db.keys())

mdf.get('Epm_nEng').samples

 #"Eng Input torque from ECU(Nm)" in mdf.channels_db.keys()



mdf.export(fmt='csv', filename='file_excel.csv')

speed = mdf.get('AccPed_tqInrDes_f')
mdf.groups[0].channels[2]
print(len(mdf.channels_db))
mdf.channels_db['Epm_nEng']
speed = mdf.get('Exh_tAdapTPFltUs').samples
speed.plot()

important_signals = ['Int32_Signal', 'Uint8_Signal']
# get short measurement with a subset of channels from 10s to 12s
short = mdf.filter(important_signals).cut(start=10, stop=12)

# convert to version 4.10 and save to disk
short.convert('4.10').save('huge.mf4')

# plot some channels from a huge file
efficient = MDF('huge.mf4')
for signal in efficient.select(['Int32_Signal', 'Uint8_Signal']):
   signal.plot()