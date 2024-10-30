sudo apt-get install wine -y
#Used to load wine packages

wget http://www.mikrotik.com/download/winbox.exe
#To download winbox app

sudo mv winbox.exe /bin
#Used to move winbox to bin directory

wine /bin/winbox.exe
#useful to run