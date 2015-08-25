#g++ -std=c++11 -fopenmp -pg -o pi pi.cpp &
./prof
gprof -p prof gmon.out
