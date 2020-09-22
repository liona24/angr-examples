#include <stdio.h>
#include <string.h>

static const char* password = "FooBar";

int main() {
    char input[10];
    scanf("%9s", input);
    if(strlen(input) == strlen(password) && strcmp(password, input) == 0) {
        printf("Very good. %s is correct!\n", input);
    } else {
        printf("You suck.\n");
    }
    return 0;
}
