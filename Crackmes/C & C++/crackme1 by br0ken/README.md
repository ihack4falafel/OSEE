##### Crackme: 
###### crackme1 by br0ken

##### Level:
###### Very easy

##### Language:
###### C/C++

##### OS:
###### Windows

##### Link:
[https://crackmes.one/crackme/5ab77f5333c5d40ad448c100](https://crackmes.one/crackme/5ab77f5333c5d40ad448c100)

##### Walkthrough:
Based on the author notes we need to crack the password and serial but i'll be patching cause i'm lazy :)

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/C%20%26%20C%2B%2B/crackme1%20by%20br0ken/Binary.png">
</p>

We find the part that takes care of the password check

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/C%20%26%20C%2B%2B/crackme1%20by%20br0ken/Code.png">
</p>

Let's patch it using `Never Branch` option in Binary Ninja that will effectivly eliminate the chance of failure based on the result of `test eax, eax` instruction

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/C%20%26%20C%2B%2B/crackme1%20by%20br0ken/Code1.png">
</p>

Now we identify the serial check branch

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/C%20%26%20C%2B%2B/crackme1%20by%20br0ken/Code2.png">
</p>

We patch

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/C%20%26%20C%2B%2B/crackme1%20by%20br0ken/Code3.png">
</p>

Let's run it

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/C%20%26%20C%2B%2B/crackme1%20by%20br0ken/Final.png">
</p>

Game over!
