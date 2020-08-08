# ITV UL tester

This was build for the UL test for the ITV. The test has 3 ITV's connected together and need to be controlled in different configurations and get output on what pressure the ITV is outputting.

## Details

The code uses SPI communication to control SMC ITV's that have Ethernet/IP. It is built to run on a raspberry pi with a screen attached that you can click, either with a mouse or by touch, on so you can interface with the UI and control the ITV's that are connected.
 ITV: https://www.smcusa.com/products/ITV-Electro-Pneumatic-Regulator-w-Ethernet~133254

### Running the tests

The ITV's IP address are constants listed in ITV_control.py. The defaults are listed below.
```
Give the example
```
hostname1 = "192.168.1.20"  #IP address of ITV 1
hostname2 = "192.168.1.21"  #IP address of ITV 2
hostname3 = "192.168.1.22"  #IP address of ITV 3
```
until finished
```

You can either change the ITV's IP addresses or change the code (line 6).

## Built With

* [ITV](https://www.smcusa.com/products/ITV-Electro-Pneumatic-Regulator-w-Ethernet~133254) - The ITV's used
* [PyQt5](https://pypi.org/project/PyQt5/) - Create the user interface
* [pyeip]() - Used to communicate to the ITV's


## Authors

* **Katherine Sandys** - *Initial work*


## Acknowledgments

* Made in 2020
* Created during my Internship at SMC
