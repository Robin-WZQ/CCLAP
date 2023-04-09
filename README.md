# CCLAP

**Paper Title:** "CCLAP: Controllable Chinese Landscape Painting Generation via Latent Diffusion Model"

**Abstract:**

With the development of deep generative models, recent years have seen great success of Chinese landscape painting generation. However, few works focus on controllable Chinese landscape painting generation due to the lack of data and limited modeling capabilities. In this work, we propose a controllable Chinese landscape painting generation method named CCLAP, which can generate painting with specific content and style based on Latent Diffusion Model. Specifically, it consists of two cascaded modules, i.e., content generator and style aggregator. The content generator module guarantees the content of generated paintings specific to the input text. While the style aggregator module is to generate paintings of a style corresponding to a reference image. Moreover, a new dataset of Chinese landscape paintings named CLAP is collected for comprehensive evaluation. Both the qualitative and quantitative results demonstrate that our method achieves state-of-the-art performance, especially in artfully-composed and artistic conception.

*CCLAP results, compared with baseline models:*

<div align=center>
    <img src=https://user-images.githubusercontent.com/60317828/230751645-047e009c-23bd-4af3-a29e-5a8470adb99a.png width="700"/>
</div>

### Requirements

- Pytorch
- [LAVIS](https://github.com/salesforce/LAVIS)
- [PytorchOCR](https://github.com/WenmuZhou/PytorchOCR)

### Dataset

- Original Data

  > Dataset contains 3560 paintings with corresponding caption. 

  Download the all dataset [here]().

- Custom Data

  > If you want to generate you own dataset (i.e.,Crap, Crop, Clean, Caption)

  running  ```/tools/YouOwnData.py```

### Fine-tuning

- To the stage-1 (Content Generator)

  please refer to the [fine-tuning stable diffusion for Chinese Landscape Painting.](https://github.com/Robin-WZQ/Text-Guide-Chinese-Landscape-Painting-Generation)

- To the stage-1 (Style Aggregator)

  please refer to the [original PAMA implementation.](https://github.com/luoxuan-cs/PAMA)

### Testing

1. Download checkpoints

Please download the pre-trained checkpoints at [google drive]() and put them in ./checkpoints.

|       Name        | Download |
| :---------------: | :------: |
| Content Generator | CG.ckpt  |
| Style Aggregator  | SA.ckpt  |

2. Run the code

Here we release a version for testing only:

```
pass
```
