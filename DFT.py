import cv2
import numpy as np
from matplotlib import pyplot as plt
import numpy.fft.fftpack as fftpack


fig=plt.figure()
img = cv2.imread('test.jpg',0)
W, H = img.shape 


f = fftpack.fft2(img)
magnitude_spectrum = np.roll(np.roll(np.real(f), H//2, axis=0), W//2, axis=1)
Mean = np.mean(magnitude_spectrum)
Std = np.std(magnitude_spectrum)

plt.subplot(2,3,1)
plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(2,3,3)
p = plt.imshow(magnitude_spectrum , cmap = 'gray')
p.set_clim(Mean-Std, Mean+Std)
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

ifft = np.zeros((H,W))
plt.subplot(2,3,4)
plt.imshow(ifft,cmap = 'gray',vmin=0, vmax=255)
plt.title('Real Time IP'), plt.xticks([]), plt.yticks([])

ifft2 = np.zeros((H,W))
plt.subplot(2,3,5)
plt.imshow(ifft2,cmap = 'gray',vmin=0, vmax=255)
plt.title('Reconstructed Image'), plt.xticks([]), plt.yticks([])

mask = np.zeros((H,W))
plt.subplot(2,3,2)
plt.imshow(mask,cmap = 'gray',vmin=0, vmax=255)
plt.title('Interface'), plt.xticks([]), plt.yticks([])

button = 0
ifft2 = np.zeros((H,W),dtype=complex)
def onclick(event):
        global button
        button = event.button

        if mask[int(event.ydata)][int(event.xdata)] == 0:

            a = np.zeros((H,W),dtype=complex)

            y = int(event.ydata)
            x = int(event.xdata)

            a[y,x] = f[y,x]

            global ifft2
            ifft2[y,x] = f[y,x]

            plt.subplot(2,3,4)
            plt.imshow(np.real(fftpack.ifft2(a)) ,cmap = 'gray')
            plt.title('Real Time IP')

            plt.subplot(2,3,5)
            plt.imshow(np.real(fftpack.ifft2(ifft2)),cmap = 'gray')
            plt.title('Reconstructed Image')

            mask[y][x] = 255
            plt.subplot(2,3,2)
            plt.imshow(mask,cmap = 'gray',vmin=0, vmax=255)
            plt.title('Interface')

while True:
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.pause(.01)
    if button == 3:
        break
