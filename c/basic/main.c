/*****************************************************************************
* File:  main.c
* 
* Description: ......
*
* 
*
*****************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define MAXBUFF 20	


void
usage(char* log)
{
   fprintf(stderr, log);
   fprintf(stderr, "Usage: executable [-h] [-f filename]\n");
   exit(-1);

}

int 
main (int argc, char ** argv)
{
    int i;

    while (1) {
        char c=0;

        c = getopt (argc, argv, "hf:");
        if (c<0)
           break;

        switch (c) {
            case 'h':
                usage ("\n");
                break;
            case 'f':
                printf ("filename [%s]\n", optarg);
                break;
            case '?':
            default:
                usage ("\n");
        }
    }

    /* Now set the values of "argc" and "argv" to the values after the
       options have been processed, above. */
    argc -= optind;
    argv += optind;

    if (argc > 0) {
        for (i = 0; i < argc; i++) {
            printf ("    Argument %d: '%s'\n", i + 1, argv[i]);
        }
    }
    return 0;
}
