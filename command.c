#include <stdint.h>
#include <stdio.h>

struct CommandStruct {
    uint8_t const size;
    uint8_t const* command;
};

struct DemoStruct {
  uint8_t x;       
  char c;   
};

void printDemoStruct(struct DemoStruct *);

void printDemoStruct(struct DemoStruct *ds) {
    printf("DemoStruct %d, %c\n", ds->x, ds->c);
}

int main() {
    struct DemoStruct ds;
    ds.x = 5;
    ds.c = 'a';
    printDemoStruct(&ds);

    return 0;
}