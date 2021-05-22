import json
import os
import random
import math
def encodeinstruction (task, instruction_structure =['Definition','Prompt','Things to Avoid','Emphasis & Caution', 'Negative Examples Full Explanations', 'Positive Examples Full Explanations'], number_of_examples=0, number_of_instances= 100):

    with open('../Dataset_Jsons/'+task+'.json') as json_file:
        data = json.load(json_file)

    indexlist=list(range(60,len(data['Instances'])-1, math.floor((len(data['Instances'])-60)/number_of_instances)))[:number_of_instances]
    
    generic_instruction=''
    for i in instruction_structure:
        if i!='Positive Examples Full Only' and i!='Positive Examples Full Explanations' and i!='Negative Examples Full Explanations':
            if data[i]!='-':
                if generic_instruction=='':
                    generic_instruction=generic_instruction+i+': '+data[i].strip() 
                else:
                    generic_instruction=generic_instruction+"\n"+i+': '+data[i].strip() 
        elif i=='Positive Examples Full Only' :
            for j in range(number_of_examples):
                if j<len(data['Examples']['Positive Examples']):
                    if generic_instruction!='':  
                        generic_instruction=generic_instruction+"\n"+'input: '+data['Examples']['Positive Examples'][j]['input'] + "\n"+ 'output: '+data['Examples']['Positive Examples'][j]['output']
                    else:
                        generic_instruction=generic_instruction+'input: '+data['Examples']['Positive Examples'][j]['input'] + "\n"+ 'output: '+data['Examples']['Positive Examples'][j]['output']
                else:
                    if j-len(data['Examples']['Positive Examples'])==60:
                        generic_instruction=generic_instruction+"\n"+'input: '+data['Instances'][20+j-len(data['Examples']['Positive Examples'])]['input'] + "\n"+ 'output: '+data['Instances'][20+j-len(data['Examples']['Positive Examples'])]['output'][0]
                    else:
                        generic_instruction=generic_instruction+"\n"+'input: '+data['Instances'][j-len(data['Examples']['Positive Examples'])]['input'] + "\n"+ 'output: '+data['Instances'][j-len(data['Examples']['Positive Examples'])]['output'][0]
        elif i=='Positive Examples Full Explanations' :
            for j in range(number_of_examples): 
                if j<len(data['Examples']['Positive Examples']):
                    generic_instruction=generic_instruction+"\n"+'Positive Example'+str(j+1)+'- '+"\n"+'input: '+data['Examples']['Positive Examples'][j]['input'] + "\n"+ 'output: '+data['Examples']['Positive Examples'][j]['output']+ "\n"+'reason: '+data['Examples']['Positive Examples'][j]['reason']
                else:
                    if j-len(data['Examples']['Positive Examples'])==60:
                        print('here 60')
                        generic_instruction=generic_instruction+"\n"+'Positive Example'+str(j+1)+'- '+"\n"+'input: '+data['Instances'][20+j-len(data['Examples']['Positive Examples'])]['input'] + "\n"+ 'output: '+data['Instances'][20+j-len(data['Examples']['Positive Examples'])]['output'][0]
                    else:
                        generic_instruction=generic_instruction+"\n"+'Positive Example'+str(j+1)+'- '+"\n"+'input: '+data['Instances'][j-len(data['Examples']['Positive Examples'])]['input'] + "\n"+ 'output: '+data['Instances'][j-len(data['Examples']['Positive Examples'])]['output'][0]
        elif i=='Negative Examples Full Explanations' :
            if len(data['Examples']['Negative Examples'])>0:
                if data['Examples']['Negative Examples'][0]!='-':
                    for j in range(number_of_examples):
                        if j<len(data['Examples']['Negative Examples']):
                            if data['Examples']['Negative Examples'][j]['suggestion']!=' ':
                                generic_instruction=generic_instruction+"\n"+'Negative Example'+str(j+1)+'- '+"\n"+'input: '+data['Examples']['Negative Examples'][j]['input'] + "\n"+'output: '+ data['Examples']['Negative Examples'][j]['output'] + "\n"+'reason: '+data['Examples']['Negative Examples'][j]['reason']+'suggestion: '+data['Examples']['Negative Examples'][j]['suggestion']
                            else:
                                generic_instruction=generic_instruction+"\n"+'Negative Example'+str(j+1)+'- '+"\n"+'input: '+data['Examples']['Negative Examples'][j]['input'] + "\n"+'output: '+ data['Examples']['Negative Examples'][j]['output'] + "\n"+'reason: '+data['Examples']['Negative Examples'][j]['reason']    
    
    promptlist=[]
    for i in range(number_of_instances):
        prompt=generic_instruction+"\n"+'input: '+data['Instances'][indexlist[i]]['input']+"\n"+"output:"
        promptlist.append(prompt)
    return promptlist
