# Natural Instructions 

Natural-Instructions is a dataset of various NLP tasks and their language instructions. 
We have built this data using existing NLP datasets and the instructions that were used to crowdsource them. 

## Dataset 
You can download the data on this website: https://instructions.apps.allenai.org/ 

## Model predictions 
We have the model predictions for the following models: 
```
predictions/gpt3_outputs
```
<!-- The BART predictions, in particular, correspond to a model that was trained on a random subset of tasks and evaluated on the remaining ones.  -->

## Evaluation script 
The script that we used in our evaluation is included in `src/???`. 

## Encoding the instructions 
TODO 

## Baselines 
We have two baselines used in this work:

- GPT-3: we have included the predictions made by our GPT-3 baselines in [`gpt3_output`](gpt3_output). 
If you want to try GPT-3 yourself, you can ask for API access in [this link](https://openai.com/blog/openai-api/). 

- BART: we reproducing our BART predictions you can use our enncoding function (TODO: link it) and train [a BART model](https://github.com/huggingface/transformers/tree/master/examples/legacy/seq2seq) on them. 


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
