##### Crackme: 
###### removemytrial_by_coulomb by keciciler

##### Level:
###### Easy

##### Language:
###### C#/.NET

##### OS:
###### Windows

##### Link:
[https://crackmes.one/crackme/5ab77f6633c5d40ad448cc53](https://crackmes.one/crackme/5ab77f6633c5d40ad448cc53)

##### Walkthrough:
We need to crack trial check
<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/dotNet/removemytrial_by_coulomb%20by%20keciciler/Binary.png">
</p>

The trial check is preformed at `Button1_Click` function

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/dotNet/removemytrial_by_coulomb%20by%20keciciler/Code.png">
</p>

Let's reverse the if statement (patch the binary) by replacing IL instruction `ble.s` with `bge.s` and vice versa

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/dotNet/removemytrial_by_coulomb%20by%20keciciler/CodePatched.png">
</p>

Save patched binary and test

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/dotNet/removemytrial_by_coulomb%20by%20keciciler/Final.png">
</p>
