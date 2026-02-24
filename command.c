#include <stdint.h>
#include <stdio.h>

struct CommandStruct {
  uint8_t const size;
  uint8_t const *command;
};

struct DemoStruct {
  uint8_t x;
  char c;
};

void printDemoStruct(struct DemoStruct *);

void printCommand(struct CommandStruct *);

void printDemoStruct(struct DemoStruct *ds) {
  printf("DemoStruct %d, %c\n", ds->x, ds->c);
}

void printCommand(struct CommandStruct *cs) {

  for (uint8_t i = 0; i < cs->size; i++)
    printf("Command: %d\n", *(cs->command + i));
}

int main() {
  struct DemoStruct ds;
  ds.x = 5;
  ds.c = 'a';
  printDemoStruct(&ds);

  return 0;
}