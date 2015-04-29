# locally
python mr_word_freq_count.py big.txt > counts
# on EMR
#python mrjob/examples/mr_word_freq_count.py README.rst -r emr > counts
# on your Hadoop cluster
#python mrjob/examples/mr_word_freq_count.py README.rst -r hadoop > counts
