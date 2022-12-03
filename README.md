<!-- # Image Caption Evaluation
This repository provides an **image-oriented evaluation tool** for image captioning systems based on our two EMNLP-IJCNLP 2019 papers, which provides an alternative method beyond **lexicon-based** metrics such as BLEU-4, METEOR, CIDEr, and SPICE. -->

<!-- ## Text-to-Image Grounding for Evaluation (TIGEr)
Here is the PyTorch code for TIGEr described in the paper ["TIGEr: Text-to-Image Grounding for Image Caption Evaluation"](https://www.aclweb.org/anthology/D19-1220.pdf). The metric is built upon a pretrained image-text matching model: [SCAN](http://www.dropwizard.io/1.0.2/docs/). -->

# Text-to-Image Grounding for Evaluation (TIGEr)

The code for `TIGEr` evaluation of our paper, **[Switching to Discriminative Image Captioning by Relieving a Bottleneck of Reinforcement Learning](https://github.com/ukyh/switch_disc_caption.git)** (WACV 2023).

### Acknowledgment
The code is based on [CapEval](https://github.com/SeleenaJM/CapEval).
We thank the authors of the repository.


## Setup

```bash
git clone --recurse-submodules https://github.com/ukyh/tiger_cocout.git
cd tiger_cocout

conda create --name tiger python=2.7
conda activate tiger

conda install pytorch=0.4.1 cuda92 -c pytorch
conda install -c pytorch torchvision
conda install -c anaconda nltk
python -c "import nltk; nltk.download('punkt')"
conda install -c anaconda scipy
echo "" >> SCAN/__init__.py
```


## Downloads

See the following page for the details: https://github.com/SeleenaJM/CapEval#download-data-and-pretrained-scan-model

```bash
pip install gdown
mkdir -p data/precomp/usecase_coco_precomp
mkdir data/candidates
mkdir data/output
mkdir -p runs/coco_scan/log/model_best.pth
cd data/precomp/usecase_coco_precomp
gdown --fuzzy 'https://drive.google.com/file/d/1BCKOOZQLbxSIV9EwQFe77aM9McQsq-bH/view?usp=share_link'
gdown --fuzzy 'https://drive.google.com/file/d/1xuJsjR98nqJli9nldBhrbLm1nxe9ziGs/view?usp=share_link'
gdown --fuzzy 'https://drive.google.com/file/d/1gDe3G0gh_FbXFun3CPY1NT-PH761QtoJ/view?usp=share_link'
cd ${HOME}/TIGEr/runs/coco_scan/log/
gdown --fuzzy 'https://drive.google.com/file/d/1MbTqWVsl5QGbjRL5ClmY3Ns7uC7lJkSt/view?usp=share_link'
```

## Run

Copy the output files to evaluate from [switch_disc_caption](https://github.com/ukyh/switch_disc_caption) (the files under `eval_results`).  
Then, run the following commands.

```bash
cd tiger_cocout
conda activate tiger

ID=sample_test
python -u preprocess_output.py eval_results/${ID}.json
python -u main.py --data_name usecase_coco_precomp --data_path $PWD/data/precomp/ --candidate_path $PWD/data/candidates --candidate_name ${ID} --output_path $PWD/data/output/
```


<!-- ### Installation
Prerequisites (installed by "install_requirement.sh"):
* Python 2.7
* PyTorch 0.4.1
* cuda & cudnn
```bash
# git clone --recurse-submodules -j8 https://github.com/SeleenaJM/CapEval.git
# cd CapEval && bash install_requirement.sh
git clone --recurse-submodules https://github.com/ukyh/TIGEr.git
cd TIGEr && bash install_requirement.sh
source activate tiger
```

### Download data and pretrained SCAN model
All the resources can be downloaded [here](https://drive.google.com/drive/folders/11eMgUHUD_6LLK9JmiiWCbuHjh0u2OgA1?usp=sharing), which include testing datasets, image features and the pretrained SCAN model. Please download the folder of `data` and `runs` under the project directory `CapEval/`. In addition to the data prepared for evaluating our metric performance as addressed in the paper, we also provide a use case for assessing the performance of a captioning system in practice. The data format in the use case is explained as below:
* References (under `data/precomp/` directory):
  * **Image Features**: a single numpy array with size `[#caption, #regions, feature dimension]`, where we set #regions=36 in our paper. We provide the precomputed image features for the testing datasets adopted from Flickr 8k/30k, MSCOCO and Pascal. If you want to evalute on your own captioning dataset, please follow the instruction of [data pro-processing](https://github.com/kuanghuei/SCAN#data-pre-processing-optional) in [SCAN](http://www.dropwizard.io/1.0.2/docs/).
  * **Human-written Reference Captions**: a single txt file with each caption per line.
  * **Image ID**: a single txt file with each image ID per line.
* Candidates (under `data/candidates/` directory):
  * **Machine-generated Candidate Captions**: a single txt file with each pair of image ID and candidate caption per line.

### Compare TIGEr with Human Ratings
Run the following command `main.py` to compare **TIGEr** metric and human ratings, and you should find a file named `composite_8k_score.csv` containing both TIGEr scores and human ratings at sentence level under `data/output` directory.
* Evaluate the flickr 8k in the composite dataset:
```bash
python main.py \ 
  --data_name composite_8k_precomp \
  --data_path $PWD/data/precomp/ \
  --candidate_path $PWD/data/candidates \
  --output_path $PWD/data/output/
```

### Caption Evaluation on New Datasets
Prepare your new captioning dataset in the [above format](#download-data-and-pretrained-scan-model). Run the above command `main.py` by setting `data_name=usecase_precomp` as an example of applying **TIGEr** on a new captioning dataset, and you should find an overall system-level score:
```bash
The overall system score is:  0.691916030506
```
and the sentence-level score file `usecase_score.csv`under the `data/output` directory:
```bash
>> head -n 5 $PWD/data/output/usecase_score.csv
imgid caption TIGER
4911020894 a boy and a girl are sitting on a bench looking at something they each have in a small paper cup .	0.768561861936
1253095131	a group of people are walking down a street .	0.662261698141
4661097013	a guy sitting with his arms crossed with a brunette on his left .	0.63660359163
4972129585	a man in a white shirt is sitting in a chair with a woman in a white shirt .	0.630412890176
``` -->

## Reference

If you find this code is useful, we appreicate it if you cite the following papers:
```
@inproceedings{honda2023switch,
    title={Switching to Discriminative Image Captioning by Relieving a Bottleneck of Reinforcement Learning},
    author={Honda, Ukyo and Taro, Watanabe and Yuji, Matsumoto},
    booktitle={Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)},
    year={2023}
  }

@inproceedings{jiang-etal-2019-tiger,
    title = "{TIGE}r: Text-to-Image Grounding for Image Caption Evaluation",
    author = "Jiang, Ming and Huang, Qiuyuan and Zhang, Lei and Wang, Xin and Zhang, Pengchuan and Gan, Zhe and Diesner, Jana  and Gao, Jianfeng",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/D19-1220",
    doi = "10.18653/v1/D19-1220",
    pages = "2141--2152"
}
```

<!-- ## Relevance, Extraness, Omission (REO)
In this work, we present a fine-grained evaluation method REO for automatically measuring the performance of image captioning systems. REO assesses the quality of captions from three perspectives: 1) Relevance to the ground truth, 2) Extraness of the content that is irrelevant to the ground truth, and 3) Omission of the elements in the images and human references.

### Code
The source code of **REO** is under construction, and will be available shortly.

### Reference
If you find this code is useful, we appreicate it if you cite our [EMNLP-IJCNLP19 paper](https://www.aclweb.org/anthology/D19-1156):
```
@inproceedings{jiang-etal-2019-reo,
    title = "{REO}-Relevance, Extraness, Omission: A Fine-grained Evaluation for Image Captioning",
    author = "Jiang, Ming and Hu, Junjie and Huang, Qiuyuan and Zhang, Lei and Diesner, Jana and Gao, Jianfeng",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/D19-1156",
    doi = "10.18653/v1/D19-1156",
    pages = "1475--1480",
}
``` -->
