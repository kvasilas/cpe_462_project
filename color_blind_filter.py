import PIL.Image as pic
import matplotlib as mpl
import numpy as np
import os

#array of values to a PIL image
def array_to_image(a):
    a = np.clip(a, 0, 255) #truncate values from [0,255]
    a = a.astype('uint8')
    img = pic.fromarray(a, mode= 'RGB')
    return img

def sim_colorblind(img, type = "d"):
    #types of colorblindness
    #deuteranope, protanope, tritanope
    cb_matrices = {
	  "d": np.array([[1, 0, 0], [0.494207, 0, 1.24827], [0, 0, 1]]),
	  "p": np.array([[0, 2.02344, -2.52581], [0, 1, 0], [0, 0, 1]]),
	  "t": np.array([[1, 0, 0], [0, 1, 0], [-0.395913, 0.801109, 0]]),
	}

    #regular rgp to lms colorspace conversion offsets
    rgb_lms = np.array([[17.8824, 43.5161, 4.11935],
		               [3.45565, 27.1554, 3.86714],
		               [0.0299566, 0.184309, 1.46709]])
    #inverse offsets
    lms_rgb = np.array([[8.09444479e-02, -1.30504409e-01, 1.16721066e-01],
		               [-1.02485335e-02, 5.40193266e-02, -1.13614708e-01],
		               [-3.65296938e-04, -4.12161469e-03, 6.93511405e-01]])
    img = img.copy()
    img = img.convert('RGB')
    rgb = np.asarray(img, dtype = float)
    lms = trans_color(rgb, rgb_lms)
    sim_lms = trans_color(lms, cb_matrices[type])
    return array_to_image(trans_color(sim_lms, lms_rgb))

def trans_color(img, type):
    return np.einsum("ij, ...j", type, img)

def filter(rgb, type = 'd'):
    pass


def main():
    orig_path = r'C:\Users\USER\Documents\coding\cpe_462_project\pics\orig.jpg'
    sim_path = r'C:\Users\USER\Documents\coding\cpe_462_project\pics\Simulated.jpg'
    filt_path= r'C:\Users\USER\Documents\coding\cpe_462_project\pics\Filtered.jpg'

    orig_image = pic.open(orig_path)
    #orig_image.show(title = "original")
    simulated = sim_colorblind(orig_image, type = "d")
    simulated.save(sim_path, 'JPEG')


    os.system("powershell -c " + orig_path)
    os.system("powershell -c " + sim_path)
    os.system("powershell -c " + filt_path)


main()
