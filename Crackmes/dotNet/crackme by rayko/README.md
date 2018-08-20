##### Crackme: 
###### crackme by rayko

##### Level:
###### Easy

##### Language:
###### VB/.NET

##### OS:
###### Windows

##### Link:
[https://crackmes.one/crackme/5ab77f6633c5d40ad448cc4b](https://crackmes.one/crackme/5ab77f6633c5d40ad448cc4b)

##### Walkthrough:
This crackme is a fairly easy one, we need to crack the serial for given name pretty much.

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/dotNet/crackme%20by%20rayko/Program.PNG">
</p>

Let's open the exeutable in dnSpy and examine the serial generation algorithm.

<p align="center">
<img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/dotNet/crackme%20by%20rayko/Functions.PNG">
</p>

As you may see the program takes `_txtName` string as an input, mutate it using `Encrypt()` function, and ultimately compare the encrypted string to `_txtSerial` string. If the `flag` is true we win, otherwise we get "Try Again" `MsgBox`. 

There are two ways you could go about solving this challenge you either reverse engineer `Encrypt()` function or set a breakpoint at the `flag` if statment and then extract `right` macro's value at runtime. I'll go with the latter cause I'm lazy, let's set a breakpoint on line `201` and run the program with `test` as Name.

<p align="center">
<img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/dotNet/crackme%20by%20rayko/Serial.PNG">
</p>

Looking at the bottom window, we see that `right` value equals `66830`. Let's open the program outside dnSpy and test.

<p align="center">
<img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/dotNet/crackme%20by%20rayko/Crack.PNG">
</p>

Game over.
