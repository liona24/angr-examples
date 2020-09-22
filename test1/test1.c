#include <stdio.h>
#include <string.h>

static const char* password = "[rr_|o";
static const char key = 29;

int main() {
    char input[10] = "";
    char encrypted[10] = "";
    scanf("%9s", input);

    int i = 0;
    while(input[i] != 0) {
        encrypted[i++] = input[i] ^ key;
    }
    if(strlen(input) == strlen(password) && strcmp(encrypted, password) == 0) {
        printf("Very good. %s is correct!\n", input);
    } else {
        printf("You suck.\n");
    }
    return 0;
}
