// https://www.hackerrank.com/challenges/lonely-integer

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>

int lonelyinteger(int a_size, int* a) {
    int tot, i;
    
    // Continuous xoring results in the odd man out being left over
    tot = 0;
    for (i = 0; i < a_size; i++) {
        tot = tot ^ a[i];
    }
    
    return tot;
}

int main() {
    int res;
    int a_size, i;
    
    scanf("%d", &a_size);
    
    int a[a_size];
    for (i = 0; i < a_size; i++) { 
        int a_item;
        scanf("%d", &a_item);
        a[i] = a_item;
    }
    
    res = lonelyinteger(a_size, a);
    printf("%d", res);
    
    return 0;
}
