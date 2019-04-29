#!/usr/bin/env bash

main_lr=(5e-4) #3e-4 5e-7 7e-7
int_lr=(1e-4 3e-3 8e-4 8e-5 5e-4 3e-4 9e-5) #(3e-3 8e-5 8e-4)   
seed=(0 1 2 3 4)
port=({4108..4143})
#port=(30 31 32 33 34 35 36 37 38 39)
#port=(40 41 42 43 44 45 46 47 48 49)
#port=(50 51 52 53 54 55 56 57 58 59)
envname="MiniWorld-OneRoom-v0" #MiniWorld-PutNext-v0
numoption=2

for _main_lr in ${main_lr[@]}
do
   count=0
   for _int_lr in ${int_lr[@]}
   do
	for _seed in ${seed[@]}
        do
   		if [ -f temprun.sh ] ; then
			rm temprun.sh
        	fi

        	echo "#!/bin/bash" >> temprun.sh
        	echo "#SBATCH --account=rpp-bengioy" >> temprun.sh
        	echo "#SBATCH --output=\"/scratch/kkheta2/slurm-%j.out\"" >> temprun.sh
        	echo "#SBATCH --gres=gpu:1" >> temprun.sh
        	echo "#SBATCH --mem=30G" >> temprun.sh
        	echo "#SBATCH --time=10:00:00" >> temprun.sh
        	echo "source $HOME/intf/bin/activate" >> temprun.sh
        	echo "cd $HOME/baselines_intfc/baselines/ppoc_int/" >> temprun.sh
		k="xvfb-run -n "${port[$count]}" -s \"-screen 0 1024x768x24 -ac +extension GLX +render -noreset\" python run_atari.py --env "$envname" --seed $_seed --opt $numoption --saves --mainlr $_main_lr --intlr $_int_lr --switch"
        	echo $k >> temprun.sh
        	echo $k
        	eval "sbatch temprun.sh"
        	rm temprun.sh
		count=$((count + 1))
   	done
   done
done


