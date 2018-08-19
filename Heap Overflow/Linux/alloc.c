#include <unistd.h>
#include <stdio.h>
#include "alloc.h"

#define REDSTART "\033[31m"
#define REDEND "\033[0m"
#define GREENSTART "\033[42m"
#define GREENEND "\033[0m"

int g_initialized = 0;
void *g_heap_start;
void *g_heap_end;

#define ALLOC_LOG(x,s...)  \
			printf(REDSTART); \
			printf(x,## s); \
			printf(REDEND);

typedef struct control_block
{
	int available;
	int size;
	struct control_block *next_free_chunk;
	struct control_block *prev_free_chunk;
} control_block_t;

control_block_t *g_free_chunks = 0;

void alloc_init()
{
	g_initialized = 1;
	g_heap_start = sbrk(0);
	g_heap_end = g_heap_start;
	ALLOC_LOG("alloc_init called heap start = 0x%x, heap end = 0x%x\n", g_heap_start, g_heap_end);
}


void dealloc(void *mem)
{
	ALLOC_LOG("dealloc called on 0x%x\n", mem);
	control_block_t *current_cb;

	current_cb = mem - sizeof(control_block_t);
	current_cb->available = 1;

	defrag_heap();
}

void *alloc(long numbytes)
{
	void *current_chunk;
	control_block_t  *current_cb;
	void *chunk_to_use;

	if (!g_initialized)
		alloc_init();

	numbytes += sizeof(control_block_t);
	ALLOC_LOG("alloc requesting %d bytes total\n", numbytes);
	chunk_to_use = 0;

	current_chunk = g_free_chunks;
	while (current_chunk)
	{
		current_cb = (control_block_t *)current_chunk;
		if (current_cb->size >= numbytes)
		{
			current_cb->available = 0;
			chunk_to_use = current_chunk;
			ALLOC_LOG("alloc found a previously used chunk to use\n");
			ALLOC_LOG("chunk location = 0x%x, chunk size = %d\n", chunk_to_use, current_cb->size);
			unlink_chunk((void *)chunk_to_use);
			break;
		}
		current_chunk = ((control_block_t *)current_chunk)->next_free_chunk;
	}

	if (!chunk_to_use)
	{
		ALLOC_LOG("alloc no previous used chunk candidates were found to suit allocation request\n");
		sbrk(numbytes);
		ALLOC_LOG("heap end now at 0x%x\n", g_heap_end);
		chunk_to_use = g_heap_end;
		g_heap_end += numbytes;
		current_cb = chunk_to_use;
		current_cb->available = 0;
		current_cb->size = numbytes;
	}

	chunk_to_use += sizeof(control_block_t);
	ALLOC_LOG("alloc returning 0x%x to user\n", chunk_to_use);
	return chunk_to_use;
}

void defrag_heap()
{
	void *current_chunk,*tmp;
	control_block_t *last_free_cb, *current_cb;
	control_block_t *last_cb;

	last_free_cb = 0;
	last_cb = 0;
	g_free_chunks = 0;
	current_chunk = g_heap_start;
	while (current_chunk < g_heap_end)
	{
		current_cb = (control_block_t *)current_chunk;
		if (current_cb->available)
		{
			if (!g_free_chunks)
			{
				g_free_chunks = current_cb;
				g_free_chunks->next_free_chunk = 0;
				g_free_chunks->prev_free_chunk = 0;
			} else {
				current_cb->prev_free_chunk = last_free_cb;
				last_free_cb->next_free_chunk = current_cb;
				current_cb->next_free_chunk = 0;
			}

			last_free_cb = current_cb;
		}
		current_chunk += current_cb->size;
	}

}

void unlink_chunk(void *chunk)
{
	control_block_t *cb = (control_block_t *)chunk;

	if (!cb->prev_free_chunk && !cb->next_free_chunk)
	{
		g_free_chunks = 0;
	} else if (!cb->next_free_chunk) {
		cb->prev_free_chunk->next_free_chunk = 0;
	} else if (!cb->prev_free_chunk) {
		g_free_chunks = cb->next_free_chunk;
	} else {
		cb->prev_free_chunk->next_free_chunk = cb->next_free_chunk;
		cb->next_free_chunk->prev_free_chunk = cb->prev_free_chunk;
	}
}

void dump_heap()
{
	control_block_t *cb;
	printf(GREENSTART"enumerating entire heap"GREENEND"\n");
	cb = (control_block_t *)g_heap_start;
	while ((void *)cb < g_heap_end) {
		printf(GREENSTART);
		printf("chunk_loc=0x%x, sz=0x%x, avail=%d, nextfree=0x%x, prevfree=0x%x", cb,cb->size,cb->available,cb->next_free_chunk, cb->prev_free_chunk);
		printf(GREENEND"\n");
		cb = (control_block_t *)((void *)cb + cb->size);
	}
}
