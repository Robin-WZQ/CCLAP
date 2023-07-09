# CCLAP

**Paper Title:** "CCLAP: Controllable Chinese Landscape Painting Generation via Latent Diffusion Model"

**Url:** [https://arxiv.org/abs/2304.04156](https://arxiv.org/abs/2304.04156)

**Abstract:**

With the development of deep generative models, recent years have seen great success of Chinese landscape painting generation. However, few works focus on controllable Chinese landscape painting generation due to the lack of data and limited modeling capabilities. In this work, we propose a controllable Chinese landscape painting generation method named CCLAP, which can generate painting with specific content and style based on Latent Diffusion Model. Specifically, it consists of two cascaded modules, i.e., content generator and style aggregator. The content generator module guarantees the content of generated paintings specific to the input text. While the style aggregator module is to generate paintings of a style corresponding to a reference image. Moreover, a new dataset of Chinese landscape paintings named CLAP is collected for comprehensive evaluation. Both the qualitative and quantitative results demonstrate that our method achieves state-of-the-art performance, especially in artfully-composed and artistic conception.

*CCLAP results, compared with baseline models:*

<div align=center>
    <img src=https://user-images.githubusercontent.com/60317828/230751645-047e009c-23bd-4af3-a29e-5a8470adb99a.png width="700"/>
</div>

### Demo

You can play with our demo at [huggingface space](https://huggingface.co/spaces/RobinWZQ/CCLAP)

### Dataset Download

- Original Data

  > Dataset contains 3560 paintings with corresponding caption. 

  Download the all dataset [Google Drive](https://drive.google.com/file/d/1nBT6KrEhasdF3mcApPtz2QsbPnVW1IhL/view?usp=sharing) | [Baidu Disk](https://pan.baidu.com/s/1oNtnRTWIe2xB0aiu0VaVnw) [code:xybz]


### Models Download

All the models are available.

|       Name        | Download |
| :---------------: | :------: |
| Content Generator | [Baidu Disk](https://pan.baidu.com/s/18NVld7Pu3JyrD59Q0jgruw) [code:2hjh] |
| Style Aggregator  | [Baidu Disk](https://pan.baidu.com/s/1HgPC61RIc_j0vRK-HODVpg) [code:tu8z] |


### Citation
```
@inproceedings{wang2023cclap,
      title={CCLAP: Controllable Chinese Landscape Painting Generation via Latent Diffusion Model}, 
      author={Zhongqi Wang and Jie Zhang and Zhilong Ji and Jinfeng Bai and Shiguang Shan},
      year={2023},
      booktitle={International Conference on Multimedia and Expo (ICME)}
}
```
