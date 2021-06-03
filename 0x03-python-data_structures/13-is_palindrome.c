#include "lists.h"
#include <stdio.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: address of pointer to head node
 * Return: 0 if list is not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	listint_t *node, *next, *temp, *prev = NULL;
	size_t nodecount = 0, midpoint;
	int odd = 0, result = 1;

	/* If invalid address of head pointer */
	if (!head)
		return (1);

	/* get length of list */
	for (node = *head; node; node = node->next)
		nodecount++;
	midpoint = nodecount / 2;
	if (nodecount % 2 != 0)
		odd = 1;

	/* reverse pointers up to length / 2 */
	for (node = *head; midpoint--; node = next)
	{
		next = node->next;
		node->next = prev;
		prev = node;
	}

	/* compare mid outward, resetting pointers */
	if (odd)
		node = node->next;

	while (node)
	{
		printf("is_palindrome: node->n = %d\n", node->n);
		printf("is_palindrome: prev->n = %d\n", prev->n);
		if (node->n != prev->n && result)
			result = 0;

		/* Reset pointer direction */
		next = node;
		temp = prev->next;
		prev->next = next;
		next = prev;

		node = node->next;
		prev = temp->next;
	}

	return (result);
}
