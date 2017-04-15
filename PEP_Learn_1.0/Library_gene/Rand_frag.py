import itertools
import pandas as pd

seq = ['A','R','N','D','C','E','Q','G','H','I','L','K','M','F','P','S','T','W','Y','V']
in_pep = "DEETGEF"
lst = (1,2,3,4)

def pep_frags(seq, pep_lenth, out_file_name):
    
    frg_list = list(itertools.combinations_with_replacement(seq, pep_lenth))

    frgs = []

    for i, frg in enumerate(frg_list):
    
        frgs.append(''.join(frg))
    
    nfrgs = len(frgs)
    
    df = pd.DataFrame(frgs,columns=["name"])
    df.to_csv(out_file_name,index=False)
    
    return nfrgs, frgs


def substitution_pep(in_pep, pos_list, mut_l):
   
   
    new_frg_list = []
    
    for mut in mut_l:
        
        #print mut
        
        ls = list(in_pep)
        for i, p in enumerate(pos_list):
            ls[p] = mut[i]
        new_frg_list.append("".join(ls))
        
    return new_frg_list
    
if __name__=="__main__":
    
    n,f = pep_frags(seq, 4, "4_mer_frag.csv")
    
    print n, "Random Peptide fragments Generated Sucessfully !"
    
    nf = substitution_pep(in_pep,lst,f)
    pd.DataFrame(nf).to_csv("new_4sub.csv")
    
    print len(nf)
    
