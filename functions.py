import os
import subprocess
import pandas as pd
import re


def funcname(self, parameter_list):
    
    pass

def txtToCSV(txt_dir,csv_dir):

    

    for filename in os.listdir(txt_dir):
        
        #print(filename)

        with open(txt_dir+filename,"r+") as txt_file:
            #print("test")
            DF_list=list()

            current_df=pd.DataFrame({'name': [""],
                                    'type': [""],
                                    'ingredient': [""],
                                    'amount': [""]})
            
            flag_2_line_meal_name=False

            igredients_counter=0
            
            flag_1=False
            flag_2=False
            flag_3=False
            flag_4=False

            flag_sniad=False
            flag_obiad=False
            flag_podwi=False
            flag_kolac=False

            flag_RECIPE_TIME=False
            flag_meal_name=False

            current_recipe=""
            meal_name=""

            flag_recipe_name_done=False

            recipe_counter = 0
            recipe_counter_kcal = 0
            empty_lines_counter = 0



            for line in txt_file.readlines():

                #print("linebyline")
                if line in ['\n', '\r\n']:
                    #print("empty line")
                    if (flag_1):
                        #print("test")
                        if (flag_2):
                            #print("test")
                            current_df.at[0,'name']=meal_name.strip()
                            #print(meal_name,"mealname")
                            current_df.at[0,'type']=current_recipe
                            DF_list.append(current_df)
                            print(current_df)
                            current_df=current_df[0:0]
                            flag_1=flag_2=False
                            recipe_counter+=1
                    continue

                    # if(flag_meal):
                    #     flag_RECIPE_TIME=True
                    # empty_lines_counter+=1
                    # flag_meal_name=False
                    # continue

                if (flag_2_line_meal_name):
                    #print("flag2linemealname")
                    meal_name=meal_name+line
                    flag_2_line_meal_name=False
                    continue
                if ("śniadanie" in line.lower()): 
                    #print("śnieadanie")
                    flag_1=True
                    current_recipe="Śniadanie"
                    #print(current_recipe)
                    #current_df.at[0,'type']=current_recipe
                    recipe_counter+=1
                    continue
                if ("obiad" in line.lower()):
                    #print("obiad") 
                    flag_1=True
                    recipe_counter+=1
                    current_recipe="Obiad"
                    #current_df.at['0','type']=current_recipe
                    continue
                if ("podwieczorek" in line.lower()): 
                    flag_1=True
                    recipe_counter+=1
                    current_recipe="Podwieczorek"
                    #current_df.at['0','type']=current_recipe
                    continue
                if ("kolacja" in line.lower()): 
                    flag_1=True
                    recipe_counter+=1
                    current_recipe="Kolacja"
                    #current_df.at['0','type']=current_recipe
                    continue
                if ("k:" in line.lower()):
                    DF_list[recipe_counter_kcal][0,'kcal']=line
                    flag_3=True
                    recipe_counter_kcal+=1

                                   

                if (flag_1 and not flag_2):
                    flag_2=True

                    meal_name=line
                    #current_df.at[0,'name']=meal_name
                    #print(meal_name)
                    if "(" in line:
                        flag_2_line_meal_name=True
                    continue
                    # here meal name is known
                
                if (flag_2 and flag_1):
                    current_df.at[igredients_counter,'ingredient'],current_df.at[igredients_counter,'amount']=line.strip().split("-")
                    igredients_counter+=1
                    #print(current_df)
                    continue

                    
                # current_df.at['0','name']=meal_name
                # current_df.at['0','type']=current_recipe








                # df=pd.DataFrame({'name': [],
                #          'type': [],
                #          'ingredient': [],
                #         'amount': []})
        

def pdfToTxt(pdf_dir,txt_dir):
    
    pdf_filenames = os.listdir(pdf_dir)
    txt_filenames = [x[:-4] + ".txt" for x in pdf_filenames]

    #print(txt_filenames)
    #attributes_for_pdf2txt = " -o {} -t text {}"

    for x,y in zip(txt_filenames,pdf_filenames):
        subprocess.call(["pdf2txt.py", "-o", txt_dir+x, pdf_dir+y])

def trimTxt(txt_dir):
    
    for filename in os.listdir(txt_dir):
        flag_keep=False
        #print(filename)
        with open(txt_dir+filename,"r") as txt_file:
            lines=txt_file.readlines()
            #print(lines)
        with open(txt_dir+filename,"w") as txt_file:
            for line in lines:
                #print("linebyline")
                if flag_keep:
                    txt_file.write(line)
                if line.__contains__("Strona 2 z "):
                    flag_keep=True
                    #print("setting flag to true")
                    
                    



    
