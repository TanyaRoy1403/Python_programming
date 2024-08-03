#include <stdio.h>
#include <stdlib.h>

// Define a struct for a linked list node
struct Node {
    int data;
    struct Node* next;
};

/* Given a reference (pointer to pointer) to the head of a
   list and an int, appends a new node at the end */
void append(struct Node** head_ref, int new_data) {
    /* 1. Allocate a new node */
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));

    if (new_node == NULL) {
        printf("Memory allocation failed. Exiting...\n");
        exit(1);
    }

    /* 2. Put the data into the new node */
    new_node->data = new_data;

    /* 3. This new node is going to be the last node, so make its 'next' as NULL */
    new_node->next = NULL;

    /* 4. If the Linked List is empty, make the new node as the head */
    if (*head_ref == NULL) {
        *head_ref = new_node;
        return;
    }

    /* 5. Else, traverse to the last node */
    struct Node* last = *head_ref;

    while (last->next != NULL)
        last = last->next;

    /* 6. Change the 'next' of the last node to the new node */
    last->next = new_node;
}

int main() {
    // Create an empty linked list
    struct Node* head = NULL;

    // Append some elements to the list
    append(&head, 1);
    append(&head, 2);
    append(&head, 3);

    // Print the linked list to verify the insertion
    struct Node* current = head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");

    return 0;
}
