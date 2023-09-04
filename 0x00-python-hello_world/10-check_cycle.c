#include "lists.h"

/**
 * check_cycle - function to to check if there is cycke
 * in the given linked list
 *
 * there is cycle in given linked list if two poinnter
 * one slow and one fast overlap at some place
 *
 * @list: is linked list to be checked
 * Return: 1 if true or 0 if false
 */



int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;

	while (slow != NULL && fast != NULL)
	{
		slow = slow->next;
		if (fast->next)
			fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
