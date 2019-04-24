# Miniworld + Baselines

## Virtualenv+ miniworld+ gym + tensorflow: CC

`module load python/3.6 

pip install virtualenv

python3 -m virtualenv intf

source intf/bin/activate

cd gym-miniworld/

pip3 install -e .
`

Test this:

     xvfb-run -a -s "-screen 0 1024x768x24 -ac +extension GLX +render -noreset" python
     
     import gym_miniworld

`pip install tensorflow_gpu

pip install mpi4py

pip install matplotlib


cd

git clone https://github.com/mklissa/baselines_intfc.git

git checkout multioption

cd baselines_intfc

pip install -e .
`
