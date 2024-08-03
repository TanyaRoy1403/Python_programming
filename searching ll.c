#include <stdio.h>

void selection(int arr[], int n) {
    int smallest;
    for (int i = 0; i < n - 1; i++) {
        smallest = i;
        for (int j = i + 1; j < n; j++) { // Find the smallest element
            if (arr[j] < arr[smallest])
                smallest = j;
        }
        // Swap the smallest element with the current element
        int temp = arr[i];
        arr[i] = arr[smallest];
        arr[smallest] = temp;
    }
}

int main() {
    printf("Enter number of elements:\n");
    int n;
    scanf("%d", &n);
    int arr[n];
    printf("Enter elements: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    selection(arr, n);
    printf("Sorted array is:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}

