# 🖼︎ CCLAP \[[Paper](https://arxiv.org/abs/2304.04156)]
<a src="https://img.shields.io/badge/cs.CV-2304.04156-b31b1b?logo=arxiv&logoColor=red" href="https://arxiv.org/abs/2304.04156"> <img src="https://img.shields.io/badge/cs.CV-2304.04156-b31b1b?logo=arxiv&logoColor=red">
</a>
<a href="https://huggingface.co/spaces/RobinWZQ/CCLAP"><img src="https://huggingface.co/datasets/huggingface/badges/raw/main/open-in-hf-spaces-sm-dark.svg" alt="Open in Spaces"> </a>

**Paper Title:** "CCLAP: Controllable Chinese Landscape Painting Generation via Latent Diffusion Model"

**Conference Accepted:** ICME 2023 (oral)

# 👀 Intorduction

In this work, we propose a controllable Chinese landscape painting generation method named CCLAP, which can generate painting with specific content and style based on Latent Diffusion Model. Specifically, it consists of two cascaded modules, i.e., content generator and style aggregator. The content generator module guarantees the content of generated paintings specific to the input text. While the style aggregator module is to generate paintings of a style corresponding to a reference image. Moreover, a new dataset of Chinese landscape paintings named CLAP is collected for comprehensive evaluation. Both the qualitative and quantitative results demonstrate that our method achieves state-of-the-art performance, especially in artfully-composed and artistic conception.


<div align=center>
<img src='https://github.com/Robin-WZQ/CCLAP/blob/main/images/model.png' width=600>
</div>

# 📩 Resources Download

### Dataset Download
 > Dataset contains 3560 paintings with corresponding captions. 

  Download the all dataset [Google Drive](https://drive.google.com/file/d/1nBT6KrEhasdF3mcApPtz2QsbPnVW1IhL/view?usp=sharing) | [Baidu Disk](https://pan.baidu.com/s/1oNtnRTWIe2xB0aiu0VaVnw) [code:xybz]

### Models Download

> The Content Generator here is a .ckpt format, a Diffuser Models format is available at [HERE](https://huggingface.co/RobinWZQ/CCLAP).

|       Name        | Download |
| :---------------: | :------: |
| Content Generator | [Baidu Disk](https://pan.baidu.com/s/18NVld7Pu3JyrD59Q0jgruw) [code:2hjh] |
| Style Aggregator  | [Baidu Disk](https://pan.baidu.com/s/1HgPC61RIc_j0vRK-HODVpg) [code:tu8z] |
  
# 🔨 Demo & Results

You can play with our demo at [huggingface space](https://huggingface.co/spaces/RobinWZQ/CCLAP).

<div align=center>
<img src='https://github.com/Robin-WZQ/CCLAP/blob/main/images/pic1.png' width=600>
</div>

<div align=center>
<img src='https://github.com/Robin-WZQ/CCLAP/blob/main/images/pic2.png' width=600>
</div>



# ⏳ Ongoing

We are very passionate about the issue of creating Chinese landscape paintings and are constantly studying these topics:

- [ ] Solve the problem that the model cannot generate human beings well.
- [ ] What is the “style” in Chinese landscape painting? The “style” or we call “genre” is a kind of thing that contains the rule or the knowledge about how we color a painting. 
- [ ] Can we control the composition of the painting? 
- [ ] A painting contains a spirit.
- [ ] How can we generate a painting in a more human way?
- [ ] ...

🤝 Feel free to discuss with us privately!


# 📄 Citation

If you find this project useful in your research, please consider cite:
```
@inproceedings{wang2023cclap,
      title={CCLAP: Controllable Chinese Landscape Painting Generation via Latent Diffusion Model}, 
      author={Zhongqi Wang and Jie Zhang and Zhilong Ji and Jinfeng Bai and Shiguang Shan},
      year={2023},
      booktitle={International Conference on Multimedia and Expo (ICME)}
}
```

