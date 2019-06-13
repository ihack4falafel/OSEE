### Windows Unicode Stack Buffer Overflow
Unicode buffer overflow due to miscalculating the size (in characters) for destination buffer, that is `lpWideCharStr` in `MultiByteToWideChar()` function.

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/VulnCases/Windows%20Unicode%20Buffer%20Overflow/Ghidra.PNG">
</p>

<p align="center">
  <img src="https://github.com/ihack4falafel/OSEE/blob/master/VulnCases/Windows%20Unicode%20Buffer%20Overflow/WinDbg.PNG">
</p>
