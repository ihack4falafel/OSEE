#include <stdio.h>
#include <string.h>
#include "alloc.h"

// use the following command to compile with alloc.c super secure heap allocator
// gcc -g -o alloc_user alloc_user.c alloc.c

int main(int argc, char **argv)
{
	char *buf1 = alloc(128); // allocate 128 bytes chunk on the heap for buf1
	char *buf2 = alloc(128); // allocate 128 bytes chunk on the heap for buf 2
  dealloc(buf2);           // free buf2 chunk and move to the free link list
	strcpy(buf1, argv[1]);   // copy user input to buf1 (no boundary checks), will use to overwrite buf2 metadata
	char *buf3 = alloc(128); // allocate 128 bytes chunk on the heap for buf3 which will effectivly trigger an overflow while reading buf2 metadata
	printf("boom!");
	return 0;
}
