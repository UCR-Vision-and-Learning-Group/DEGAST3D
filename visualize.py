import numpy as np
import tifffile as tiff
import matplotlib.pyplot as plt
import random, pdb
from tqdm import tqdm

def generate_random_colors(num_colors):
    """Generate a list of distinct colors."""
    return {label: [random.randint(0, 255) for _ in range(3)] for label in range(num_colors)}

def colorize_segmentation(segmentation, label_map, color_dict):
    """Colorize the segmentation map based on corresponding labels."""
    colored_image = np.zeros((*segmentation.shape, 3), dtype=np.uint8)


    # pdb.set_trace()
    for i,lbl in tqdm(enumerate(label_map)):
        colored_image[segmentation == lbl] = color_dict[i]
    
    return colored_image

def visualize_and_save(seg0, seg1, label0, label1, seg0_out, seg1_out):

    
    # Create color dictionary based on label correspondences
    color_dict = generate_random_colors(len(label0))

    # pdb.set_trace()
    
    # Generate colored segmentations
    colored_seg0 = colorize_segmentation(seg0, label0, color_dict)
    colored_seg1 = colorize_segmentation(seg1, label1, color_dict)
    
    # Save output images
    tiff.imwrite(seg0_out, colored_seg0)
    tiff.imwrite(seg1_out, colored_seg1)
    
    print(f"Saved colored segmentation maps: {seg0_out}, {seg1_out}")



def COLORIZE_SEG_MAP(seg):


    label = np.unique(seg)[1:]
    color_dict = generate_random_colors(len(label))
    colored_seg = colorize_segmentation(seg, label, color_dict)

    return colored_seg


if __name__ == "__main__":
    # Example usage

    seg0 = tiff.imread('/home/eegrad/mdislam/SAM/Biusque_Upload/upload_version/DEGAST3D/data/test_plant/cellpose/seg/00hrs_plant15_trim-acylYFP.tif_mask.tif')
    color_seg0 = COLORIZE_SEG_MAP(seg0)
    tiff.imwrite('colored.tif',color_seg0)



    # # Load segmentation maps
    # seg0 = tiff.imread('/home/eegrad/mdislam/SAM/Biusque_Upload/upload_version/DEGAST3D/data/test_plant/cellpose/seg/00hrs_plant15_trim-acylYFP.tif_mask.tif')
    # seg1 = tiff.imread('/home/eegrad/mdislam/SAM/Biusque_Upload/upload_version/DEGAST3D/data/test_plant/cellpose/seg/04hrs_plant15_trim-acylYFP.tif_mask.tif')
    # pairs0 = np.load('/home/eegrad/mdislam/SAM/Biusque_Upload/upload_version/DEGAST3D/results/cellpose_test_plant/all_tracks_stack_00hrs_plant15_trim-acylYFP.tif_mask.tif_04hrs_plant15_trim-acylYFP.tif_mask.tif.npy')
    
    # # pdb.set_trace()
    # label0 = pairs0[:,0]
    # label1 = pairs0[:,1]

    # visualize_and_save(
    #     seg0, seg1,  
    #     label0, label1,  # Example corresponding labels
    #     seg0_out='seg0_out.tif', seg1_out='seg1_out.tif'
    # )
