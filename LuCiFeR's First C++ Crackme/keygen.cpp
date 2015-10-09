#include <stdio.h>
#include <string.h>
#include <stdlib.h>
 
int main()
{
        char isim[20];
        int res;
 
        printf("your name: ");
        scanf("%s", isim);
 
        int len = strlen(isim);
 
        __asm
        {
                        mov edx, len;
                        imul edx, edx, 0x875CD;
                        mov eax, 0x51EB851F;
                        mul edx;
                        mov eax, edx;
                        shr eax, 5;
                        imul eax, eax, -0x370;
                        mov edx, 0;
                        push edx;
                        push eax;
                        fild QWORD PTR SS : [ESP];
                        lea esp, DWORD PTR SS : [ESP + 0x8];
						fstp qword ptr ss:[ebp-410];
		                fld qword ptr ss:[ebp-410];
                        fstp QWORD PTR SS : [ESP + 0x8];
                        mov eax, [ESP + 8];
                        mov res, eax;
        }
 
        printf("%i-x019871\n", res);
        system("pause");
}
