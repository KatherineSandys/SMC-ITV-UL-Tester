# ITV UL tester

This was build for the UL test for the ITV. The test has 3 ITV's connected together and need to be controlled in different configurations and get output on what pressure the ITV is outputting.

## Details

The code uses SPI communication to control SMC ITV's that have Ethernet/IP. It is built to run on a raspberry pi with a screen attached that you can click, either with a mouse or by touch, on so you can interface with the UI and control the ITV's that are connected.
 ITV: https://www.smcusa.com/products/ITV-Electro-Pneumatic-Regulator-w-Ethernet~133254

### Running the tests

The ITV's IP address are constants listed in ITV_control.py. The defaults are listed below.

```
hostname1 = "192.168.1.20"  #IP address of ITV 1
hostname2 = "192.168.1.21"  #IP address of ITV 2
hostname3 = "192.168.1.22"  #IP address of ITV 3
```

You can either change the ITV's IP addresses or change the code (line 6).

## Built With

* [ITV](https://www.smcusa.com/products/ITV-Electro-Pneumatic-Regulator-w-Ethernet~133254) - The ITV's used
* [PyQt5](https://pypi.org/project/PyQt5/) - Create the user interface
* [pyeip]() - Used to communicate to the ITV's
* [Raspberry Pi](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/) - The code runs on

## FILES
* control_ITV_UI.py : python code that builds the interface, generated from the .ui file
* control_ITV.ui : designed by pyqt5 designer and contorls the look
* ITV_control.py : file to run the screen, has all functionallity coded here
* pyeip.py : File that
* Older versions folder:
  * control_ITV_v1.0.py : first working version with tktinker
  * control_ITV_v1.1.py : using qt5 now for interface
  * control_ITV_v2.0.py : comments added, removed btntest function,
  * control_ITV_v2.1.py : controlling the user interface with python
  * control_ITV_v2.2.py : reordering of code and comments
  * ITV EIP Set and Read.py : file that just has the code for communicating with ITV with ethernet

## Authors

* **Katherine Sandys** - *Initial work*


## Acknowledgments

* Made in 2020
* Created during my Internship at SMC
