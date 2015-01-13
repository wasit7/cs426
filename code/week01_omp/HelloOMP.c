#include "omp.h"
void main(){
	#prama omp parallel{
		int ID = omp_get_thread_num();
		printf("Hello(%ID) ");
		printf("world(%ID) ");

	}
}