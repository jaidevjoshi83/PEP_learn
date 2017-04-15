
from lib.optimized_COR_ROC import *
from lib.dis_str_gen import *
from lib.Structure_bassed_Descriptor_generation import *
from lib.call_R import *
from lib.Feature_selection_very_new_II import *
import pandas as pd
import tempfile
import shutil

class both_des(object):
    
    def __init__(self,in_file,out_file_pep,out_file_str):
        
        self.in_file = in_file
        self.out_file_pep = out_file_pep
        self.out_file_str = out_file_str
        
    def Whole_DF(self):
        
        df1,cl =  DC_CLASS().main_process(self.in_file,self.out_file_pep)
        print cl
        df2,_ =  Str_DS_class().main_process(self.in_file, self.out_file_str)
        df3 = pd.concat([df1,df2,cl],axis=1)
        df3.to_csv("Full_des.csv", index = False)
        Run_r().main("Full_des.csv","Pre_processed_des.csv")
        df4 = pd.read_csv("Pre_processed_des.csv")
        df4 = pd.concat([df4,cl],axis=1)
        df4.to_csv("Pre_processed_labeled.csv",sep=",", index = False)
    
    def Feature_selectoin(self):
        feature().feature_selection_main("Pre_processed_labeled.csv","new_out.csv", 0.2,)
    
    def ROC(self):
        My_csv_class().main_pro("reduced_Data.csv",4)
    
       
if __name__=="__main__":

    a = both_des("pep_2.csv","oops_new.csv","out_file_str.csv")
    a.Whole_DF()
    a.Feature_selectoin()
    a.ROC()
    

