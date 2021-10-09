# Phoenix-Assist
 This app simplifies the process of using Phoenix Miner, by dividing it into pieces. This app is a command-line application which works on Linux and Windows.
 
 ## Installation and Use cases
 
### Dependencies
 [Python 3](https://www.python.org/downloads/)
 
 Phoenix Miner (and add it to PATH)
 
 Windows
 > [Download from this guide](https://phoenixminer.org/download/latest/) and don't follow any of the examples, as this program helps with that.
 
 Linux 
 > On Debian (and Debian-based systems), Read [this](https://github.com/ubden/Miner-Phoenixminer/blob/main/Linux-Ubuntu.md) (Note, this guide also includes installing propiatery amdgpu-pro drivers) 
 
 > On Arch (and Arch-based systems), download from the [AUR](https://aur.archlinux.org/packages/phoenixminer/) ([Binary](https://aur.archlinux.org/packages/phoenixminer-bin/))
### Drivers
**MAKE SURE THAT YOU HAVE THE RIGHT DRIVERS INSTALLED, OR IT WILL NOT WORK**

Windows
> Almost every Windows driver should work

Linux
|GPU Maker|Driver Software|Does it work?|
|---|---|---|
|Neutral|[opengl-mesa](https://archlinux.org/packages/extra/x86_64/opencl-mesa/) |Untested, unlikely to work|
|NVIDIA|[opencl-nvidia](https://archlinux.org/packages/extra/x86_64/opencl-nvidia/)|Yes, under Cuda**|
|AMD|[opengl-amd](https://aur.archlinux.org/packages/opencl-amd/) |Yes, under OpenGL**|
|Intel|[beignet](https://aur.archlinux.org/packages/beignet/) |Untested, unlikely to work|
|Intel|[intel-compute-runtime](https://archlinux.org/packages/?name=intel-compute-runtime) |Untested, could work|
|Intel|[intel-opencl](https://aur.archlinux.org/packages/intel-opencl/) |Untested, unlikely to work|
|Intel|[intel-opencl-runtime](https://aur.archlinux.org/packages/intel-opencl-runtime/) |Untested, unlikely to work|

*note, these names are based off arch linux's packages and the data is based off [DaVinci Resolve's](https://wiki.archlinux.org/title/DaVinci_Resolve#Installation) OpenGL / Cuda compatibillity*
 
 ** Under propiatery drivers

 * AMD: [xf86-video-amdgpu](https://archlinux.org/packages/extra/x86_64/xf86-video-amdgpu/) and ([amdpro-gpu-libgl](https://aur.archlinux.org/packages/amdgpu-pro-libgl/) or [amdgpu-pro](https://aur.archlinux.org/pkgbase/amdgpu-pro-installer))

 * NVIDIA: [nvidia](https://archlinux.org/packages/extra/x86_64/nvidia/) and [nvidia-utils](https://archlinux.org/packages/extra/x86_64/nvidia-utils/)

 ### Add Phoenix Miner to PATH
 
 Locate Phoenix Miner and get it's path.
 
 * [Windows](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/)
 
 * [Linux](https://linuxize.com/post/how-to-add-directory-to-path-in-linux/#adding-a-directory-to-your-path) 
 
 (note: add the file, not the whole directory)
 
 ### Installation of Phoenix Assist
 (not done yet)

 ## Why?
 I made a similar program a while ago, but accidentally deleted it off of my computer. So, i rewrote it in Python and made it open source.

 ## Fees
 We do not have fees, but Phoenix Miner takes a 0.65% fee.
