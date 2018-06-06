salloc --time=3:00:00 --ntasks=1 --account=def-omnomnomnomnom --gres=gpu:1 --mem 12000M

Installating Dependencies for Unreal Code 
`conda create -n unreal27 python=2.7 pip`
`source activate unreal27`
`pip install https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-1.8.0-cp27-none-linux_x86_64.whl`
`conda install numpy opencv matplotlib`
`pip install pygame`
# Install bazel
`wget https://github.com/bazelbuild/bazel/releases/download/0.13.0/bazel-0.13.0-installer-linux-x86_64.sh`
`chmod +x bazel-0.13.0-installer-linux-x86_64.sh`
`./bazel-0.13.0-installer-linux-x86_64.sh --user`
`export PATH="$PATH:$HOME/bin"`
# Clone deepmind-lab and unreal repos
`git clone https://github.com/deepmind/lab.git`
`cd lab`
`git clone https://github.com/kkhetarpal/unrealwithattention.git`
`bazel --output_base=/home/kkheta2/project/kkheta2/bazelout1 run //unrealwithattention:train --define headless=glx`


For unrealwithattention/train to be visible, you must change the bazel lab/BUILD file. The instructions in the unreal readme seem flawed (see issue here)

diff --git a/BUILD b/BUILD
@@ -971,6 +971,7 @@ cc_binary(
     visibility = [
         "//python/pip_package:__subpackages__",
         "//python/tests:__subpackages__",
+       "//unrealwithattention:__subpackages__",
     ],

(unreal)/unreal$ git diff
diff --git a/options.py b/options.py
@@ -38,7 +38,7 @@ def get_options(option_type):
-    tf.app.flags.DEFINE_boolean("grad_norm_clip", 40.0, "gradient norm clipping")
+    tf.app.flags.DEFINE_float("grad_norm_clip", 40.0, "gradient norm clipping")

