##### Crackme: 
###### csharp_crackme by monsterhunter445

##### Level:
###### Hard

##### Language:
###### C#/.NET

##### OS:
###### Windows

##### Link:
[https://crackmes.one/crackme/5ab77f5633c5d40ad448c27c](https://crackmes.one/crackme/5ab77f5633c5d40ad448c27c)

##### Walkthrough:
Based on the author notes, we need to bypass the registration check

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/dotNet/csharp_crackme%20by%20monsterhunter445/Binary.JPG">
</p>

This lead to `CD26____EVEN` function

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/dotNet/csharp_crackme%20by%20monsterhunter445/Code.PNG">
</p>

We'll reverse the if statment at line `70` by switching the IL instruction `brtrue.s` to `befalse.s`

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/dotNet/csharp_crackme%20by%20monsterhunter445/Code1.PNG">
</p>

Now if you click on `Access Features` button, we get the following

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/dotNet/csharp_crackme%20by%20monsterhunter445/Final.PNG">
</p>

Click OK and voila!

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/Crackmes/dotNet/csharp_crackme%20by%20monsterhunter445/Final1.PNG">
</p>
