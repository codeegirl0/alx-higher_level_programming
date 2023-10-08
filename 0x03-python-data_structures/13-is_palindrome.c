#include "lists.h"

listinteg_t *reverse_listinteg(listinteg_t **head);
int get_palindrome(listinteg_t **head);

/**
 * reverse_listint - Reversing list.
 * @head: A pointer to the starting node.
 * Return: A pointer of the reversed list.
 */
listinteg_t *reverse_listinteg(listinteg_t **head)
{
	listinteg_t *node = *head, *thenext, *theprev = NULL;

	while (node)
	{
		thenext = node->thenext;
		node->thenext = theprev;
		theprev = node;
		node = thenext;
	}
	*head = theprev;
	return (*head);
}

/**
 * get_palindrome - Checking palindrome.
 * @head: A pointer to the head.
 * Return: list is not a palindrome - 0.
 *         list is a palindrome - 1.
 */
int get_palindrome(listinteg_t **head)
{
	listinteg_t *temp, *reev, *mied;
	size_t size = 0, i;

	if (*head == NULL || (*head)->thenext == NULL)
		return (1);

	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->thenext;
	}

	temp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		temp = temp->thenext;

	if ((size % 2) == 0 && temp->m != temp->thenext->m)
		return (0);

	temp = temp->thenext->thenext;
	reev = reverse_listinteg(&temp);
	mied = reev;

	temp = *head;
	while (reev)
	{
		if (temp->m != reev->m)
			return (0);
		temp = temp->thenext;
		reev = reev->thenext;
	}
	reverse_listinteg(&mied);

	return (1);
}
