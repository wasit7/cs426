#include <iostream>
using namespace std;
#include <omp.h>

#define SIZE 8
int main(void){
	int x[SIZE];
	int sum=0;
	for(int i=0;i<SIZE;i++){
		x[i]=i;
	}
	#pragma omp parallel for reduction (+:sum)
	for(int i=0;i<SIZE;i++){
                sum+=x[i];
        }
	cout<<sum<<std::endl;
	return 0; 
}

