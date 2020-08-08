Description:
  This was build for the UL test for the ITV. The test has 3 ITV's connected together. 
  The code uses SPI communication to control SMC ITV's that have Ethernet/IP. It is built to run on a raspberry pi with a screen attached that you can click on so you can interface with the UI and control the ITV's. 
   ITV: https://www.smcusa.com/products/ITV-Electro-Pneumatic-Regulator-w-Ethernet~133254

THE FILES:
  control_ITV_UI.py : python code that builds the interface, generated from the .ui file
  control_ITV.ui : designed by pyqt5 designer and contorls the look
  ITV_control.py : file to run the screen, has all functionallity coded here
  pyeip.py : File that 
  Older versions folder:
    control_ITV_v1.0.py : first working version with tktinker
    control_ITV_v1.1.py : using qt5 now for interface
    control_ITV_v2.0.py : comments added, removed btntest function,
    control_ITV_v2.1.py : controlling the user interface with python
    control_ITV_v2.2.py : reordering of code and comments
    ITV EIP Set and Read.py : file that just has the code for communicating with ITV with ethernet
