#include <omp.h>
#include <stdio.h>

int main(void){
	#pragma omp parallel
	{
		int ID = omp_get_thread_num();
		printf("Hello(%d)", ID);
		printf("World(%d)\n", ID);
	}
	return 0;
}
