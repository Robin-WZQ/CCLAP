import argparse
import torch
from torchvision.utils import make_grid
from PIL import Image, ImageFile
from net import Net
from utils import DEVICE, test_transform
Image.MAX_IMAGE_PIXELS = None  
ImageFile.LOAD_TRUNCATED_IMAGES = True

    

def style_transfer_method(content_image,style_img):
    main_parser = argparse.ArgumentParser(description="main parser")
    subparsers = main_parser.add_subparsers(title="subcommands", dest="subcommand")

    main_parser.add_argument("--pretrained", type=bool, default=True,
                                   help="whether to use the pre-trained checkpoints")
    main_parser.add_argument("--requires_grad", type=bool, default=True,
                                   help="set to True if the model requires model gradient")

    train_parser = subparsers.add_parser("train", help="training mode parser")
    train_parser.add_argument("--training", type=bool, default=True)
    train_parser.add_argument("--iterations", type=int, default=60000,
                                  help="total training epochs (default: 160000)")
    train_parser.add_argument("--batch_size", type=int, default=2,
                                  help="training batch size (default: 8)")
    train_parser.add_argument("--num_workers", type=int, default=2,
                                  help="iterator threads (default: 8)")
    train_parser.add_argument("--lr", type=float, default=1e-4, help="the learning rate during training (default: 1e-4)")
    train_parser.add_argument("--content_folder", type=str, required = True, 
                                  help="the root of content images, the path should point to a folder")
    train_parser.add_argument("--style_folder", type=str, required = True,
                                  help="the root of style images, the path should point to a folder")
    train_parser.add_argument("--log_interval", type=int, default=10000,
                                  help="number of images after which the training loss is logged (default: 20000)") 

    train_parser.add_argument("--w_content1", type=float, default=12, help="the stage1 content loss weight")
    train_parser.add_argument("--w_content2", type=float, default=9, help="the stage2 content loss weight")
    train_parser.add_argument("--w_content3", type=float, default=7, help="the stage3 content loss weight")
    train_parser.add_argument("--w_remd1", type=float, default=2, help="the stage1 remd loss weight")
    train_parser.add_argument("--w_remd2", type=float, default=2, help="the stage2 remd loss weight")
    train_parser.add_argument("--w_remd3", type=float, default=2, help="the stage3 remd loss weight")
    train_parser.add_argument("--w_moment1", type=float, default=2, help="the stage1 moment loss weight")
    train_parser.add_argument("--w_moment2", type=float, default=2, help="the stage2 moment loss weight")
    train_parser.add_argument("--w_moment3", type=float, default=2, help="the stage3 moment loss weight")
    train_parser.add_argument("--color_on", type=str, default=True, help="turn on the color loss")
    train_parser.add_argument("--w_color1", type=float, default=0.25, help="the stage1 color loss weight")
    train_parser.add_argument("--w_color2", type=float, default=0.5, help="the stage2 color loss weight")
    train_parser.add_argument("--w_color3", type=float, default=1, help="the stage3 color loss weight")

    
    eval_parser = subparsers.add_parser("eval", help="evaluation mode parser")
    eval_parser.add_argument("--training", type=bool, default=False)
    eval_parser.add_argument("--run_folder", type=bool, default=False)

    args = main_parser.parse_args()

    args.training = False

    model = Net(args)
    model.eval()
    model = model.to(DEVICE)
    
    tf = test_transform()

    Ic = tf(content_image).to(DEVICE)
    Is = tf(Image.fromarray(style_img)).to(DEVICE)

    Ic = Ic.unsqueeze(dim=0)
    Is = Is.unsqueeze(dim=0)
    
    with torch.no_grad():
        Ics = model(Ic, Is)

    grid = make_grid(Ics[0])
    # Add 0.5 after unnormalizing to [0, 255] to round to the nearest integer
    ndarr = grid.mul(255).add_(0.5).clamp_(0, 255).permute(1, 2, 0).to("cpu", torch.uint8).numpy()
    im = Image.fromarray(ndarr)
    
    return im
