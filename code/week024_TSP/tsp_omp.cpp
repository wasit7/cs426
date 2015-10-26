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
void twoOpt(int N, int* path, float* A,int M){
    cout<<">>>twoOpt_omp"<<endl;
    int na,nb,nc,nx,ny,nz,i,j;
    srand (time(NULL));
    for(int k=0; k<M; k++){
        i=rand() % (N-1)+1;
        j=rand() % (N-1)+1;
        //problem i and j may be the same value and makes swapping is useless
        na=path[(i-1+N)%N];
        nb=path[i];
        nc=path[(i+1)%N];
        nx=path[(j-1+N)%N];
        ny=path[j];
        nz=path[(j+1)%N];
        //swap ci and rj
        if( A[na*N+ny]+A[ny*N+nc]+A[nx*N+nb]+A[nb*N+nz] < A[na*N+nb]+A[nb*N+nc]+A[nx*N+ny]+A[ny*N+nz]){
            path[i]=ny;
            path[j]=nb;
        }
    }
}
void twoOpt_omp(int N, int* path, float* A,int M){
    cout<<">>>twoOpt_omp"<<endl;
    float* ptd=new float[Ncores];//parallel total distance
    int** ppath=new int* [Ncores];
    for(int i=0; i<Ncores; i++){
        ppath[i]=new int[N];
        for(int j=0; j<N; j++){
            ppath[i][j]=path[j];
        }
    }

    #pragma omp parallel shared(A,N,ppath,M)
    {

        //--a--b--c--
        //--x--y--z--
        //swapping between b and y

        int na,nb,nc,nx,ny,nz,i,j,ID;
        ID = omp_get_thread_num();
        srand (ID);
        int* path=ppath[ID];
        for(int k=0; k<M; k++){
            i=rand() % (N-1)+1;
            j=rand() % (N-1)+1;
            //problem i and j may be the same value and makes swapping is useless
            na=path[(i-1+N)%N];
            nb=path[i];
            nc=path[(i+1)%N];
            nx=path[(j-1+N)%N];
            ny=path[j];
            nz=path[(j+1)%N];
            //swap ci and rj
            if( A[na*N+ny]+A[ny*N+nc]+A[nx*N+nb]+A[nb*N+nz] < A[na*N+nb]+A[nb*N+nc]+A[nx*N+ny]+A[ny*N+nz]){
                path[i]=ny;
                path[j]=nb;
            }
        }
        ptd[ID]=totalDistance(N,ppath[ID],A);
        //#pragma omp critical
        //cout<<"ID:"<<ID<<" ptd:"<<ptd[ID]<<endl;

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

        twoOpt_omp(N, path, A,1e7);
        showPath(N,path,A);
    }
}
