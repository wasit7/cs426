#include <iostream>
#include <string>
#include <fstream>
#include <iomanip>
#include <time.h>
#include <stdlib.h>
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
void twoOpt(int N, int* path, float* A){
    int na,nb,nc,nx,ny,nz,i,j;
    for(int k=0; k<8e7; k++){
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
int main(){
    string fname="data2.tsv";
    ifstream file(fname);
    int N;
    int* path;
    srand (time(NULL));
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

        cout<<"Path: ";
        for(int i=0; i<N; i++){
            cout<< path[i]<<"-->";
            cout<< subDistance(N,path,A,i)<<endl;
        }
        cout<<endl<<"Total distance: "<<totalDistance(N,path,A)<<endl;

        cout<<">>>twoOpt";
        twoOpt(N, path, A);
        cout<<"Path: ";
        for(int i=0; i<N; i++){
            cout<< path[i]<<"-->";
        }
        cout<<endl<<"Total distance: "<<totalDistance(N,path,A)<<endl;
    }
}
