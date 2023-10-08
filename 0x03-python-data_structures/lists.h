#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

/**
 * struct listinteg_s - the linked list
 * @m: the integer
 * @thenext: the next integer
 *
 * Todo: singly linked list node structure
 */
typedef struct listinteg_s
{
	int m;
	struct listinteg_s *thenext;
} listinteg_t;

size_t print_listinteg(const listinteg_t *h);
listinteg_t *add_nodeinteg(listinteg_t **head, const int m);
void freing_listinteg(listinteg_t *head);
int get_palindrome(listinteg_t **head);

#endif /* LISTS_H */
