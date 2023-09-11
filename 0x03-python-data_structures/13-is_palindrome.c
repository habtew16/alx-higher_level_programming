#include "lists.h"

/**
 * is_palindrome - funnction to check if the given linked
 * list is palindrome or not
 *
 * inorder to achieve dis i pushed all the elements
 * in to the list and checked from both ends
 *
 * @head: head of the linked list
 *
 * Return: returns 1 if true and 0 if is
 * false
 */

int is_palindrome(listint_t **head)
{
	listint_t *current;
	int len;
	int i;

	current  = *head;
	len = 0;
	i = 0;

	if ((*head) == NULL)
		return (1);
	while (current != NULL)
	{
		len++;
		current = current->next;
	}

	if (len == 1)
		return (1);

	current = *head;
	i = 0;
	int list[len];

	while (current != NULL)
	{
		list[i] = current->n;
		i++;
		current = current->next;
	}

	for (i = 0; i < len / 2; i++)
	{
		if (list[i] != list[len - 1 - i])
		{
			return (0);
		}
	}
	return (1);
}
