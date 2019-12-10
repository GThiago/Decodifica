#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){

	char aux[1],deco[]= "115104101108108116101114123108101971141101051101039510111099111100101125";
	int tam = strlen(deco), a,b,c,x,y,z,res;
	for (x = 0; x<tam;x+=3){
		y = x + 1;
		z = x + 2;

		//strcat(aux,&deco[x]);
		a = deco[x] - '0';
		b = deco[y] - '0';
		c = deco[z] - '0';
		res = a * 10;
		res += b;
		res = res * 10;
		res += c;
		if (res > 127){
			res -= c;
			res = res/10;
			x -= 1;
		}
		printf ("%c",res);
	}

	printf("\n");
	return 0;
}

