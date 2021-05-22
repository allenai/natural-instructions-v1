# Natural Instructions 

NATURAL INSTRUCTIONS is a dataset of various NLP tasks and their language instructions. 
We have built this data using existing NLP datasets and the instructions that were used to crowdsource them. 

## Data 
You can download the data on this website: https://instructions.apps.allenai.org/ 

## Model predictions 
We have the model predictions for the following models: 
```
predictions/gpt3_outputs
predictions/bart_outputs 
```
The BART predictions, in particular, correspond to a model that was trained on a random subset of tasks and evaluated on the remaining ones. 

## Evaluation script 
The script that we used in our evaluation is included in `src/evaluation.py`. 

## How to Evaluate
It requires dataset file path and the prediction file path
E.g.  
python3 evaluation.py --predictions ../predictions/gpt3_outputs/subtask002_quoref_answer_generation@_Definition_Prompt@0_100.json --dataset ../Dataset_Jsons/subtask002_quoref_answer_generation.json
Filenames in GPT3_Outputs are of the format [taskname]'@'[instruction encoding]'@'[number of examples]'_'[number of instances].json 

## Encoding the instructions 
In 'src/utils', encodeinstruction function is provided to generate encoded instruction inputs.
E.g.
encodeinstruction('subtask003_mctaco_question_generation_event_duration', instruction_structure =['Definition','Prompt'])

## Baselines 
We have two baselines used in this work:

- GPT-3: we have included the predictions made by our GPT-3 baselines in [`gpt3_output`](gpt3_output). 
If you want to try GPT-3 yourself, you can ask for API access in [this link](https://openai.com/blog/openai-api/). 


## How to cite
Feel free to cite us: 
```bibtex
@article{mishra2021natural,
  title={Natural Instructions: Benchmarking Generalization to New Tasks from Natural Language Instructions},
  author={Mishra, Swaroop and Khashabi, Daniel and Baral, Chitta and Hajishirzi, Hannaneh},
  journal={arXiv preprint arXiv:2104.08773},
  year={2021}
}
```
