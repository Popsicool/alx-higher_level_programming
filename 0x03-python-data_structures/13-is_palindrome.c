#include "lists.h"

listint_t* replicate_(const listint_t *head){

  const listint_t *curr = head;
  listint_t *clone = NULL;

  while (curr != NULL)
	{
	  add_nodeint_end(&clone, curr->n);
	  curr = curr->next;
	}
  return (clone);
}

int is_palindrome(listint_t **head){
  listint_t *clone, *after, *curr;


  curr = after = *head;
  listint_t *before = NULL;

  const listint_t *current;
  int n,i;
  int b = 1;
  current =*head;
  n = 0;

  while (current != NULL)
	{
	  current = current->next;
	  n++;
	}

  for(i=0; i<(n-1); i++)
	{
	  after= after->next;
	  curr->next = before;
	  before = curr;
	  curr =after;
	}
  curr->next = before;

  clone = replicate_(*head);

  while (curr != NULL && clone != NULL){

	if(curr->n != clone->n)
	  b = 0;
	curr = curr->next;
	clone = clone->next;
  }
  free_listint(clone);
  return(b);
}
