from diffusers import DiffusionPipeline,UniPCMultistepScheduler
import gradio as gr
import torch
import gc
from style_transfer import style_transfer_method


def generate(style_image,text, negative_prompts,steps,guidance_scale):
    pipeline = DiffusionPipeline.from_pretrained("./CCLAP")
    pipeline.scheduler = UniPCMultistepScheduler.from_config(
            pipeline.scheduler.config)
    device = torch.device(
            'cuda:0' if torch.cuda.is_available() else 'cpu')
    if device.type == 'cuda':
            pipeline.enable_xformers_memory_efficient_attention()
    pipeline.to(device)
    torch.cuda.empty_cache()
    gc.collect()
    content_image = pipeline(text,
                     num_inference_steps=steps,
                     negative_prompt=negative_prompts,
                     guidance_scale=guidance_scale).images[0]
    result = style_transfer_method(content_image,style_image)
    return content_image,result


if __name__ == '__main__':

    demo = gr.Interface(title="CCLAP",
                        description = (
                            "This is the demo of CCLAP to generate Chinese landscape painting."
                            ),
                        css="",
                        fn=generate,
                        inputs=[gr.Image(label="Style Image",shape=(512,512)),
                                gr.Textbox(lines=3, placeholder="Input the prompt", label="Prompt"), 
                                gr.Textbox(lines=3, placeholder="low quality", label="Negative prompt"), 
                                gr.Slider(minimum=0, maximum=100, value=20,label='Steps'),
                                gr.Slider(minimum=0, maximum=30, value=7.5,label='Guidance_scale'),
                                ],
                        outputs=[gr.Image(label="Content Output",shape=(256,256)),
                                 gr.Image(label="Final Output",shape=(256,256))],
                        examples = [
                                    [
                                        'style_image/style1.jpg',
                                        'A Chinese landscape painting of a mountain landscape with trees',
                                        'low quality',
                                        20,
                                        7.5
                                    ],
                                    [
                                        'style_image/style2.jpg',
                                        'A Chinese landscape painting of a building with trees in front of it',
                                        'low quality',
                                        20,
                                        7.5
                                    ],
                                    [
                                        'style_image/style3.jpg',
                                        'A Chinese landscape painting of a landscape with mountains in the background',
                                        'low quality',
                                        20,
                                        7.5
                                    ],
                                    [
                                        'style_image/style4.jpg',
                                        'A Chinese landscape painting of a landscape with mountains and a river',
                                        'low quality',
                                        20,
                                        7.5
                                    ],
                                ],
                        )

    demo.launch()