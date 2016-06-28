#include <stdio.h>
#include <libproject.h>

int main(int argc, char* argv) 
{
  int result = project_func();

  printf("Hello world lib returned %d\n", result);


  return result;
}

