import itertools
import pandas as pd

raw = 'ARNDCEQGHILKMFPSTWYV'

def Rand_seq_gene(AA):
    results = [x for x in itertools.permutations(raw, r=3) ]
    Out_Seq_list = []
    for r in results: 
        seq =  ''.join(r)
        Out_Seq_list.append(seq)
    return  Out_Seq_list

def Write_Seq_to_file(seqs):
    df = pd.DataFrame(seqs,columns=["name"])
    df.to_csv("Rand_frag.csv")
    print "Rand. Frag. Generated Successfully..!"
    
def Main_Pro():
    s = Rand_seq_gene(raw)
    Write_Seq_to_file(s)
    
    
if __name__=="__main__":
    
    Main_Pro()
