

/* Given a reference (pointer to pointer) to the head of a
   list
   and an int,  inserts a new node on the front of the list.
 */
#include <stdio.h>
#include <stdlib.h>

// Define a struct for a linked list node
struct Node {
    int data;
    struct Node* next;
};

/* Given a reference (pointer to pointer) to the head of a
   list and an int, inserts a new node at the front of the list.
 */
void push(struct Node** head_ref, int new_data) {
    /* 1. Allocate a new node */
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));

    if (new_node == NULL) {
        printf("Memory allocation failed. Exiting...\n");
        exit(1);
    }

    /* 2. Put the data into the new node */
    new_node->data = new_data;

    /* 3. Make the 'next' of the new node point to the current head */
    new_node->next = (*head_ref);

    /* 4. Move the head to point to the new node, effectively making it the new head */
    (*head_ref) = new_node;
}

int main() {
    // Create an empty linked list
    struct Node* head = NULL;

    // Push some elements to the list
    push(&head, 3);
    push(&head, 2);
    push(&head, 1);

    // Print the linked list to verify the insertion
    struct Node* current = head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");

    return 0;
}


