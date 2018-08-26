##### Crackme: 
###### crackme_by_coulomb by keciciler

##### Level:
###### Easy

##### Language:
###### C#/.NET

##### OS:
###### Windows

##### Link:
[https://crackmes.one/crackme/5ab77f6633c5d40ad448cc54](https://crackmes.one/crackme/5ab77f6633c5d40ad448cc54)

##### Walkthrough:
We need to crack the serial for given name

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/dotNet/crackme_by_coulomb%20by%20keciciler/Binary.png">
</p>

Let's take a look at `Button1_Click`

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/dotNet/crackme_by_coulomb%20by%20keciciler/_Code_.png">
</p>

We can see that the serial is nothing but a concatenation of multiple strings, that is name as well as label's text. Let's confirm by placing a breakpoint.

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/dotNet/crackme_by_coulomb%20by%20keciciler/Breakpoint.png">
</p>

`right` holds the desired serial value.

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/dotNet/crackme_by_coulomb%20by%20keciciler/Final.png">
</p>
