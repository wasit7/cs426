#g++ -std=c++11 -fopenmp -pg -o pi pi.cpp &
#./pi
gprof -p pi gmon.out
