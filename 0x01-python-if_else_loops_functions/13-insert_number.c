#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: address of pointer to head node
 * @number: integer to be included in new node
 * Return: address of the new node, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *search;

	if (!head)
		return (NULL);

/* Create the new node */
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
/* Find the right place to put it */
	else
	{
		if ((*head)->n >= number)
		{
			new->next = *head;
			*head = new;
		}
		else
		{
			for (search = *head; search->next; search = search->next)
			{
				if (search->next->n >= number)
				{
					new->next = search->next;
					break;
				}
			}
			search->next = new;
		}
	}

	return (new);
}
