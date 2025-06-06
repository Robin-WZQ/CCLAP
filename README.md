# 🖼️ CCLAP \[[Paper](https://arxiv.org/abs/2304.04156)]
<a src="https://img.shields.io/badge/cs.CV-2304.04156-b31b1b?logo=arxiv&logoColor=red" href="https://arxiv.org/abs/2304.04156"> <img src="https://img.shields.io/badge/cs.CV-2304.04156-b31b1b?logo=arxiv&logoColor=red">
</a>
<a href="https://huggingface.co/spaces/RobinWZQ/CCLAP"><img src="https://huggingface.co/datasets/huggingface/badges/raw/main/open-in-hf-spaces-sm-dark.svg" alt="Open in Spaces"> </a>

**Paper Title:** "CCLAP: Controllable Chinese Landscape Painting Generation via Latent Diffusion Model"

**Conference Accepted:** ICME 2023 (oral)

# 👀 Introduction

In this work, we propose a controllable Chinese landscape painting generation method named CCLAP, which can generate painting with specific content and style based on Latent Diffusion Model. Specifically, it consists of two cascaded modules, i.e., content generator and style aggregator. The content generator module guarantees the content of generated paintings specific to the input text. While the style aggregator module is to generate paintings of a style corresponding to a reference image. Moreover, a new dataset of Chinese landscape paintings named CLAP is collected for comprehensive evaluation. Both the qualitative and quantitative results demonstrate that our method achieves state-of-the-art performance, especially in artfully-composed and artistic conception.


<div align=center>
<img src='https://github.com/Robin-WZQ/CCLAP/blob/main/images/model.png' width=600>
</div>

# 📩 Resources Download

### Dataset Download
 > Dataset contains 3560 paintings with corresponding captions. 

- [Badiu Disk](https://pan.baidu.com/s/1yOOTyjS100j2WFGiCXo25A?pwd=gf3a)

- [Google Drive](https://drive.google.com/file/d/1FA_tuSlXlWHTkIRgG7eVM0CFGgynrvNR/view?usp=sharing)

### Models Download

|       Name        | Download |
| :---------------: | :------: |
| Content Generator | [Hugging face](https://huggingface.co/RobinWZQ/CCLAP) |
| Style Aggregator  | [Baidu Disk](https://pan.baidu.com/s/1HgPC61RIc_j0vRK-HODVpg) [code:tu8z] |
  
# 🔨 Results

<div align=center>
<img src='https://github.com/Robin-WZQ/CCLAP/blob/main/images/pic1.png' width=600>
</div>

<div align=center>
<img src='https://github.com/Robin-WZQ/CCLAP/blob/main/images/pic2.png' width=600>
</div>

# How to use

- Git clone this repo and pip install the requirements

- Download the models (i.e., Content Generator and Style Aggregator) and put them into the same folder

  ```
  Make sure the file structure is:

  CCLAP
  PAMA
  style_image
  app.py
  hist_loss.py
  net.py
  style_transfer.py
  utils.py
  ```

- run app.py
  ```
  python app.py
  ```

🤝 Feel free to discuss with us privately!


# 📄 Citation

If you find this project useful in your research, please consider cite:
```
@INPROCEEDINGS{10219843,
  author={Wang, Zhongqi and Zhang, Jie and Ji, Zhilong and Bai, Jinfeng and Shan, Shiguang},
  booktitle={2023 IEEE International Conference on Multimedia and Expo (ICME)}, 
  title={CCLAP: Controllable Chinese Landscape Painting Generation Via Latent Diffusion Model}, 
  year={2023},
  pages={2117-2122},
  doi={10.1109/ICME55011.2023.00362}}
```

