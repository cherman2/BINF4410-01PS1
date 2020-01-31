import argparse
import warnings
import pytest



def main():

    #implementing command line response via argparse
    parser = argparse.ArgumentParser(description="Parser will count the amount of K-mers and their frequencies")
    parser.add_argument('-k', dest='k', default=1, type=int,
                        help='length of sequence for which to calculate k-mer frequencies')
    parser.add_argument('-f', dest='file', required=True, help='sequence file name (nucleotides only, no headers)')

    #Takes the command line and applies to method
    args = parser.parse_args()

    #takes file turns into sequence and saves K as a variable
    with open(args.file, 'r') as f:
        seqFile = f.read().replace('\n', '')
    print(args)
    k = args.k

    #makes all file content uppercase
    seqFile = seqFile.upper()

    assert len(seqFile) > 2, " invalid file must be longer than 2 nucleotides "


    for letter in seqFile:
        if letter != 'C' and letter != 'G' and letter != 'A' and letter != 'T':
            warnings. warn("Nucleotides should be A, G, T, or C")
        if letter.isdigit():
            assert letter.isalpha(), "Nucleotides must be letter"

    kmerfreq(seqFile, k)


def kmerfreq(seqFile, k):
    kmerFreq = {}
    kmer = ''
    freq = 0
    total = 0


    for i in range(0, len(seqFile) - (k - 1)):
        kmer = seqFile[i: i + k]
        ##print(kmer)
        if kmer in kmerFreq:
            freq = kmerFreq.get(kmer)
            kmerFreq[kmer] = freq + 1
            total = total + 1
        else:
            kmerFreq[kmer] = 1
            total = total + 1

#turns counts into frequencies
    for key in kmerFreq.keys():
        kmerFreq[key] = (kmerFreq[key] / total)





    print(kmerFreq)
    print ( "total amount of kmers with " , k ," nucleotide(s) is", total)



if __name__=="__main__":
    main()


