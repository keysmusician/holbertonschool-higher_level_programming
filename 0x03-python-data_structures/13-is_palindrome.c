#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: address of pointer to head node
 * Return: 0 if list is not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *node, *next, *prev = NULL;
	size_t nodecount = 0, midpoint;
	int odd = 0, result = 1;

	if (!head)
		return (1); /* Invalid address of head pointer */
	for (node = *head; node; node = node->next)
		nodecount++;
	midpoint = nodecount / 2;
	if (nodecount % 2 != 0)
		odd = 1;
	for (node = *head; midpoint--; node = next)
	{
		next = node->next;
		node->next = prev;
		prev = node;
	}
	if (odd)
		node = node->next;
	while (node)
	{
		if (node->n != prev->n && result)
			result = 0;
		node = node->next;
		prev = prev->next;
	}
	return (result);
}
