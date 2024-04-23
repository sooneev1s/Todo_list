#include <stdio.h>

int main()
{
    int i = 20;
    int a = (i*2) - (--i * ++i) +i++;
    printf("%d", a);
    
}