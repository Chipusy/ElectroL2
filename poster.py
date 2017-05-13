import urllib, datetime, os

month = str(datetime.datetime.now().month) if datetime.datetime.now().month >= 10 else '0'+str(datetime.datetime.now().month) 
year = str(datetime.datetime.now().year)
day = str(datetime.datetime.now().day) if datetime.datetime.now().day >= 10 else '0'+str(datetime.datetime.now().day)
hour = str((datetime.datetime.now()-datetime.timedelta(hours=2)).hour) if (datetime.datetime.now()-datetime.timedelta(hours=2)).hour >= 10 else '0'+str((datetime.datetime.now()-datetime.timedelta(hours=2)).hour)

month_name = datetime.datetime.now().strftime("%B")

url = 'ftp://electro:electro@ftp.ntsomz.ru/ELECTRO_L_2/'+year+'/'+month+'_'+month_name+'/'+day+'_'+month+'_'+year+'/'+day+month+year+'_'+hour+'%2000.jpg'

urllib.urlretrieve(url, '/tmp/planet.jpg')

os.system("gsettings set org.gnome.desktop.background picture-uri file:///tmp/planet.jpg")
os.system("gsettings set org.gnome.desktop.background picture-options 'centered'")