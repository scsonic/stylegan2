

# for run training oppai
#
#
#
<<<<<<< HEAD
#python run_training.py --num-gpus=1 --data-dir=~/datasets/oppai --config=config-f \
#  --dataset=oppai --mirror-augment=true
=======
python run_training.py --num-gpus=1 --data-dir=~/Desktop/datasets/oppai --config=config-f --dataset=oppai --mirror-augment=true

python run_training.py --num-gpus=1 --data-dir=/home/scsonic/Desktop/datasets/oppai --config=config-f --dataset=oppai --mirror-augment=true
>>>>>>> b42fb83a79c316b826e0535e49d31063d2d3b67f

python run_training.py --num-gpus=1 --data-dir=/media/scsonic/ai/GanDataSet/oppai128 --config=config-f --dataset=oppai128 --mirror-augment=true
python run_training.py --num-gpus=1 --data-dir=/media/scsonic/ai/GanDataset/oppai128 --config=config-f --dataset=oppai128

#
#

python dataset_tool.py create_from_images /media/scsonic/ai/DataSet/oppai128/media/scsonic/ai/GanDataSet/oppai128

# python dataset_tool.py create_from_images ~/Desktop/datasets/oppai ~/Desktop/oppai128_20200126
n dataset_tool.py create_from_images ~/Desktop/datasets/oppai ~/Desktop/oppai128_20200126
# python dataset_tool.py create_from_images ~/Desktop/datasets/oppai ~/Desktop/oppai128_20200126
# python dataset_tool.py create_from_images ~/Desktop/datasets/oppai ~/Desktop/oppai128_20200126
