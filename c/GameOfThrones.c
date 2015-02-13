// https://www.hackerrank.com/challenges/game-of-thrones

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int findPalind(char *arr)
{
    int i, len, sum, c;
    int chars[26] = {0};
  
    for (i=0; arr[i] != '\0'; i++) {
        chars[arr[i] - 97]++;
    }
    
    sum = 0;
    for (i=0; i<26; i++) {
        sum = sum + (chars[i] % 2);
    }
  
    if (sum > 1)
        printf("NO\n");
    else
        printf("YES\n");

    return 0;
}

int main() {
    char arr[100001];
    scanf("%s",arr);
    findPalind(arr);
    return 0;
}
