#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node
 * Return: void
 */
void reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 * Return: 1 if it is, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *sl = *head, *fa = *head, *tp = *head, *dup = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fa = fa->next->next;

		if (!fa)
		{
			dup = sl->next;
			break;
		}
			if (!fa->next)
			{
				dup = sl->next->next;
				break;
			}
			sl = sl->next;
	}
	reverse_listint(&dup);
	while (dup && tp)
	{
		if (tp->n == dup->n)
		{
			dup = dup->next;
			tp = tp->next;
		}
		else
			return (0);
	}

	if (!dup)
		return (1);

	return (0);
}
