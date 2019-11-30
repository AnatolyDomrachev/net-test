#include "stdio.h"
#include "string.h"

#define SIZE 300

int main(int argc, char** argv) 
{ 
	char buf1[SIZE], buf2[SIZE];
	FILE *result, *data; 
	data = fopen(argv[1], "r"); 
	if(!data)
	{
		printf("Error open file");
		return 1;
	}

	int true;
	while(fgets(buf1, SIZE, data))
	{
		true = 0;
		result = fopen(argv[2], "r"); 
		if(!result)
		{
			printf("Error open file");
			return 2;
		}
		while(fgets(buf2, SIZE, result))
			if(strcmp(buf1, buf2)==0)
				true = 1;
		fclose(result);
	if(true)
		printf("--------- %s", buf1);
	else
		printf("%s", buf1);
	}
	fclose(data);

	return 0;
}
	
