import imageProcessing as ip
import numpy as np
import matplotlib.pyplot as plt

x = ip.loadImage("Hopper.tiff")
plt.figure(1)
ip.histogram(x.copy(), channel="R", bins=32)
plt.savefig("hist_R.tiff")
plt.figure(2)
ip.histogram(x.copy(), channel="G", bins=32)
plt.savefig("hist_G.tiff")
plt.figure(3)
ip.histogram(x.copy(), channel="B", bins=32)
plt.savefig("hist_B.tiff")
plt.figure(4)
ip.histogram(x.copy(), channel="L", bins=32)
plt.savefig("hist_L.tiff")
plt.figure(5)
ip.histogram(x.copy(), channel="R", bins=32, scale="log")
plt.savefig("hist_R_log.tiff")
plt.figure(6)
ip.histogram(x.copy(), channel="L", bins=32, scale="log")
plt.savefig("hist_L_log.tiff")

plt.figure(7)
ip.saveImage(ip.unsharpMask(x.copy()), "unsharp-defaults.tiff")
ip.saveImage(ip.unsharpMask(x.copy(), radius=50), "unsharp-r50.tiff")
y = ip.rgb2hsl(x.copy())
ip.saveImage(ip.unsharpMask(y.copy(), radius=2, amount=100, format="HSL"), "unsharp-r2a100.tiff")
