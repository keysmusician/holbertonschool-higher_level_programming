#include "lists.h"

/**
 * check_cycle - checks if a singly linked list contains a cycle
 * @list: linked list head
 * Return: 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current, *search;
	size_t n, nodes = 0;

	for (current = list; current; current = current->next)
	{
		search = list;
		for (n = 0; n <= nodes; n++)
		{
			if (current->next == search)
				return (1);
			search = search->next;
		}
		nodes++;
	}
	return (0);
}
