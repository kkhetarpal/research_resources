
- Create conda env and install code dependencies and mujoco

```
conda create -n muj python=3.6
conda install -c conda-forge tensorflow
cd baselines_intfc/
pip install -e .
pip install gym==0.9.3
pip install mujoco-py==0.5.1
conda install -c anaconda mpi4py
conda install -c conda-forge matplotlib
```



- Add path to Bashrc
```
vi .bashrc
export MUJOCO_PY_MJKEY_PATH=/home/kkheta2/mjpro150/bin/mjkey.txt
export MUJOCO_PY_MJPRO_PATH=/home/kkheta2/mjpro131
:wq (enter)
```

- Source Bashrc - you might have to exit and ssh again.
```
source bashrc
conda activate muj
```

-To test if mujoco installation is successfull
```
python
"import mujoco_py"
```
