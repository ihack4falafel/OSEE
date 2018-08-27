##### Crackme: 
###### keygenme_1337 by subminking

##### Level:
###### Medium

##### Language:
###### C#/.NET

##### OS:
###### Windows

##### Link:
[https://crackmes.one/crackme/5ab77f6533c5d40ad448cba2](https://crackmes.one/crackme/5ab77f6533c5d40ad448cba2)

##### Walkthrough:
We need to crack the serial pretty much

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/dotNet/keygenme_1337%20by%20subminking/Binary.JPG">
</p>

Examine `button1_Click`

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/dotNet/keygenme_1337%20by%20subminking/Code.JPG">
</p>

And `CheckKey`

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/dotNet/keygenme_1337%20by%20subminking/Code1.JPG">
</p>

Let's take the easy route and patch `if` statement via IL instructions :D

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/dotNet/keygenme_1337%20by%20subminking/Code2.JPG">
</p>

Save and run without input

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/dotNet/keygenme_1337%20by%20subminking/Final.JPG">
</p>
