#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
#include <time.h>
#include <stdlib.h>
#include <omp.h>
#define Ncores 8
using namespace std;
float subDistance(int N,int* path, float* A,int i){
//0<=i and i<N
    int r=path[i%N];
    int c=path[(i+1)%N];
    return A[r*N+c];
}
float totalDistance(int N, int* path, float* A){
    float td=0;
    for(int i=0; i<N; i++){
        td+=subDistance(N,path,A,i);
    }
    return td;
}
void showPath(int N, int* path, float* A){
    cout<<"    Path: ";
    for(int i=0; i<N; i++){
        cout<< path[i]<<"->";
    }
    cout<<endl<<"    Total distance: "<<totalDistance(N,path,A)<<endl;
}
void twoOpt(int N, int* path, float* A){

    float* ptd=new float[Ncores];//parallel total distance
    int** ppath=new int* [Ncores];
    for(int i=0; i<Ncores; i++){
        ppath[i]=new int[N];
        for(int j=0; j<N; j++){
            ppath[i][j]=path[j];
        }
    }

    #pragma omp parallel shared(A,N,ppath)
    {

        //--a--b--c--
        //--x--y--z--
        //swapping between b and y

        int na,nb,nc,nx,ny,nz,i,j,ID;
        ID = omp_get_thread_num();
        srand (ID);

        for(int k=0; k<1e7; k++){
            i=rand() % (N-1)+1;
            j=rand() % (N-1)+1;
            //problem i and j may be the same value and makes swapping is useless
            na=ppath[ID][(i-1+N)%N];
//            #pragma omp critical
//            cout<<"debug"<<na<<endl;
            nb=ppath[ID][i];
            nc=ppath[ID][(i+1)%N];
            nx=ppath[ID][(j-1+N)%N];
            ny=ppath[ID][j];
            nz=ppath[ID][(j+1)%N];
            //swap ci and rj
            if( A[na*N+ny]+A[ny*N+nc]+A[nx*N+nb]+A[nb*N+nz] < A[na*N+nb]+A[nb*N+nc]+A[nx*N+ny]+A[ny*N+nz]){
               ppath[ID][i]=ny;
               ppath[ID][j]=nb;
            }
        }
        ptd[ID]=totalDistance(N,ppath[ID],A);
        #pragma omp critical
        cout<<"ID:"<<ID<<" ptd:"<<ptd[ID]<<endl;

    }

    //find min path from all cores
    int bestcore=0;
    for(int i=1;i<Ncores;i++){
        if(ptd[i]<ptd[bestcore]){
            bestcore=i;
        }
    }
    for(int i=0;i<N;i++){
        path[i]=ppath[bestcore][i];
    }

}
int main(){
    string fname="data2.tsv";
    ifstream file(fname);
    int N;
    int* path;
    if(file.is_open()){
        cout<<"Loading "<<fname<<endl;
        file >> N;
        float* A = new float[N*N];
        int* path = new int [N];
        for(int r = 0; r < N; ++r){
            path[r]=r;
            for(int c = 0; c < N; ++c){
                file >> A[r*N+c];
            }
        }

        cout<<"Array A: "<<endl;
        for(int r = 0; r < N; ++r){
            for(int c = 0; c < N; ++c){
                cout <<"\t"<<setw(4)<<fixed <<setprecision(1)<<right<< A[r*N+c];
            }
            cout<<endl;
        }


        showPath(N,path,A);
        cout<<">>>twoOpt"<<endl;
        for(int i=0;i<1e0;i++){
            twoOpt(N, path, A);
            showPath(N,path,A);
        }
    }
}
