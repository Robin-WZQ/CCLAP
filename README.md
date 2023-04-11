# CCLAP

**Paper Title:** "CCLAP: Controllable Chinese Landscape Painting Generation via Latent Diffusion Model"

**Arxiv:** [https://arxiv.org/abs/2304.04156](https://arxiv.org/abs/2304.04156)

**Abstract:**

With the development of deep generative models, recent years have seen great success of Chinese landscape painting generation. However, few works focus on controllable Chinese landscape painting generation due to the lack of data and limited modeling capabilities. In this work, we propose a controllable Chinese landscape painting generation method named CCLAP, which can generate painting with specific content and style based on Latent Diffusion Model. Specifically, it consists of two cascaded modules, i.e., content generator and style aggregator. The content generator module guarantees the content of generated paintings specific to the input text. While the style aggregator module is to generate paintings of a style corresponding to a reference image. Moreover, a new dataset of Chinese landscape paintings named CLAP is collected for comprehensive evaluation. Both the qualitative and quantitative results demonstrate that our method achieves state-of-the-art performance, especially in artfully-composed and artistic conception.

*CCLAP results, compared with baseline models:*

<div align=center>
    <img src=https://user-images.githubusercontent.com/60317828/230751645-047e009c-23bd-4af3-a29e-5a8470adb99a.png width="700"/>
</div>

The other implementation of Chiense landscape painting geration models (e.g., StyleGAN2, DDPM) are released at [HERE](https://github.com/Robin-WZQ/Unconditional-Chinese-Landscape-Painting-Generation).

### Requirements

- Pytorch
- [LAVIS](https://github.com/salesforce/LAVIS)
- [PytorchOCR](https://github.com/WenmuZhou/PytorchOCR)

### Dataset

- Original Data

  > Dataset contains 3560 paintings with corresponding caption. 

  Download the all dataset [Google Drive](https://drive.google.com/file/d/1nBT6KrEhasdF3mcApPtz2QsbPnVW1IhL/view?usp=sharing) | [Baidu Disk](https://pan.baidu.com/s/1oNtnRTWIe2xB0aiu0VaVnw) [code:xybz]
- Custom Data

  > If you want to generate you own dataset (i.e., Crap -> Crop -> Clean -> Caption)

  running  ```/YouOwnData.py``` Unfinished

### Fine-tuning

- To the stage-1 (Content Generator)

  please refer to the [fine-tuning stable diffusion for Chinese Landscape Painting.](https://github.com/Robin-WZQ/Text-Guide-Chinese-Landscape-Painting-Generation)

- To the stage-1 (Style Aggregator)

  please refer to the [original PAMA implementation.](https://github.com/luoxuan-cs/PAMA)

### Testing

1. Download checkpoints

Please download the pre-trained checkpoints and put them in .corresponding places.

|       Name        | Download |
| :---------------: | :------: |
| Content Generator | [Baidu Disk]() Unfinished |
| Style Aggregator  | [Baidu Disk]() Unfinished |

2. Run the code (for testing only)

>  We highly recommend following the original instructions of [Stable Diffusion](https://github.com/Robin-WZQ/Text-Guide-Chinese-Landscape-Painting-Generation) and [PAMA](https://github.com/luoxuan-cs/PAMA).

- Content Generator:

```
# Run the model
!(python scripts/txt2img.py \
    --prompt 'a chinese landscape painting of a landscape with mountains and a river' \
    --outdir 'outputs/generated_pl' \
    --H 512 --W 512 \
    --n_samples 4 \
    --config 'configs/stable-diffusion/landscape_paintings.yaml' \
    --ckpt 'epoch43.ckpt')
```

```python
from PIL import Image
im = Image.open("outputs/generated_pl/grid-0000.png").resize((1024, 256))
display(im)
print("a chinese landscape painting of a landscape with mountains and a river")
```

- Style Aggregator:

```
python main.py eval --content content_picture_path.jpg --style style_picture_path.jpg
```

### Citation
```
@misc{wang2023cclap,
      title={CCLAP: Controllable Chinese Landscape Painting Generation via Latent Diffusion Model}, 
      author={Zhongqi Wang and Jie Zhang and Zhilong Ji and Jinfeng Bai and Shiguang Shan},
      year={2023},
      eprint={2304.04156},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
