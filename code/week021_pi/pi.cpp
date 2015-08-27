#include <iostream>
using namespace std;
#include <omp.h>
#include <random>
#include <math.h>
#include <time.h>

#define N_cores 8
int main(void){
        unsigned long long sum[N_cores]={};
	int spt = 1e7;//sample per thread
	int ID,i;
        #pragma omp parallel shared(sum,spt) private(ID,i)
        {
                ID = omp_get_thread_num();
			std::default_random_engine e((unsigned int)time(0)+ID);
  			std::uniform_real_distribution<double> distribution(0.0,1.0);
                //int x[1000];
                //initialization
                for(i=0;i<spt;i++){
                    double x = distribution(e);
					double y = distribution(e);
					//cout<<"L0-->core:"<< ID <<"    "<<x<<","<<y<<std::endl;
					if(x*x+y*y<1.0){
						sum[ID]++;
					}
                }
		#pragma omp critical
                cout<<"L0-->core:"<< ID <<", sum:"<< sum[ID]<<std::endl;
		#pragma omp barrier
		if(!(ID%2)){
			sum[ID]+=sum[ID+1];
			cout<<"L1-->core:"<< ID <<", sum:"<< sum[ID]<<std::endl;
		}
		#pragma omp barrier
		if(!(ID%4)){
			sum[ID]+=sum[ID+2];
			cout<<"L2-->core:"<< ID <<", sum:"<< sum[ID]<<std::endl;
		}
		#pragma omp barrier
		if(!(ID%8)){
			sum[ID]+=sum[ID+4];
			cout<<"L3-->core:"<< ID <<", sum:"<< sum[ID]<<std::endl;
		}
	}

	cout<<"M_PI  : "<<3.14159<<std::endl;
	cout<<"Result: "<<(double)sum[0]/N_cores/spt*4.0f<<std::endl;
        return 0;
}
