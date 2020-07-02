# Python_GUI
GUI help make projects more interactive and informative at the same time 

This Readme file contains the installation steps of various components required for making a python GUI , we send data to the GUI using the Server , it could also be done by connecting the hardware namely arduino or any other development board .

*STEPS* to install
 .1. create a new folder in F drive -> name it Software ,
 now on google search for "python 3.8.3" (if you have python with any other version kindly uninstall it first).     
https://www.python.org/downloads/
Download the exe file and paste it in F drive software folder .

2. Type “ICDT Modbus TCP server   “
Link is : http://www.icdt.com.tw/main/index.php/2013-07-09-05-16-50/modbus-free-software/file/57-modbus-tcp-server
Translate the page , then Go to the end of the page , click “I agree” and then download the zip file .
Again paste this file in software folder and extract it there .
3.now type “ pymodbus tcp python 3.8”
Go to this link - https://pypi.org/project/pyModbusTCP/
In the page under github section there is this link :

https://github.com/sourceperl/pyModbusTCP.git
copy paste it in browser and download the zip file by clicking the “download/clone” button on top right (green color)

same with this zip file , paste it in software and then extract it .

4. now run the python exe file , it will get saved to C drive file , make a note of that path :
Also make a note of the name of the pyModbusTCP-master file’s name .(remove -master from the name for convienence ) 

Now go to control panel -> system and security->system-.> advanced -> environment variables-> path ->add 
In it add as follows :

C:/Users/DELL/AppData/Local/program/python/python38-32/Scripts


5. Go to command prompt now 
Type these one by one 
cd
cd f:
cd software
software>cd pyModbusTCP > pyModbus 
setup.py.install
exit 

6.Next create a new folder in F drive name it pythonGUI
In it , then create a text file save  as test.py

In it add the following codes

from pyModbusTCP.client import ModbusClient
c = ModbusClient(host="localhost", port=502, auto_open=True)
regs = c.read_holding_registers(0, 2)
if regs:
    print(regs)
else:
    print("read error")

Now open the ICDT Modbus TCP server app and give some values 

 
Click on the button above highlighted to set up the server .

Now run the python code . the output window should show the random values u had given in the server.
