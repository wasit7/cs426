#include <omp.h>
#include <stdio.h>

int main(void){
	#pragma omp parallel
	{
		int th_id = omp_get_thread_num();
		printf("Hello(%d) ",th_id);
	}
	return 0;
}
