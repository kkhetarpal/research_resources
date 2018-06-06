salloc --time=3:00:00 --ntasks=1 --account=def-omnomnomnomnom --gres=gpu:1 --mem 12000M

### Installating Dependencies for Unreal Code 
```
conda create -n unreal27 python=2.7 pip
source activate unreal27
pip install https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.8.0-cp27-none-linux_x86_64.whl
conda install numpy opencv matplotlib
pip install pygame
```

### Install bazel
```
wget https://github.com/bazelbuild/bazel/releases/download/0.13.0/bazel-0.13.0-installer-linux-x86_64.sh
chmod +x bazel-0.13.0-installer-linux-x86_64.sh
./bazel-0.13.0-installer-linux-x86_64.sh --user
export PATH="$PATH:$HOME/bin"
```


### Clone deepmind-lab and unreal repos
```
git clone https://github.com/deepmind/lab.git
cd lab
git clone https://github.com/kkhetarpal/unrealwithattention.git
bazel --output_base=/home/bazelout1 run //unrealwithattention:train --define headless=glx
```

For unrealwithattention/train to be visible, you must change the bazel lab/BUILD file. The instructions in the unreal readme seem flawed (see [issue here](https://github.com/miyosuda/unreal/issues/21))
