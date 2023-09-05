#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - function to insert number in
 * sorted linked list
 * @head: the head of linked lists
 * @number: the number to be inserted
 * Return: returns null if assignment is
 * failed or new_node
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;

	listint_t *current = *head;
	listint_t *prev = NULL;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	while (current != NULL && current->n <= number)
	{
		prev = current;
		current = current->next;
	}

	if (prev == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		prev->next = new_node;
		new_node->next = current;
	}
	return (new_node);
}
