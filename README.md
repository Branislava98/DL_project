# Deep Learning Project
 

Based on [Zhanteng Xie's Yolact for CPU](https://github.com/zzuxzt/yolact_cpu/)

## How to run Docker image 
I have already built and pushed an Image to [DockerHub](https://hub.docker.com/u/branislava123)  

All you need to do is have Docker daemon running  

Then pull my image

```
docker pull branislava123/my-image:latest
```

And run the container

```
docker run branislava123/my-image:latest
```

It will run a [eval.py](./yolact_cpu/eval.py) on your CPU. After, it will run a [test](./test.py) which will compare generated image with what I've got on my machine. If they are similar it will print "Test passed".

After that the container will stop and output files will be availiable for copying

```
docker ps -a
docker cp <container_id>:./output/ ~/
```

## How to build Docker image

Firstly clone this repository recursively

```
git clone https://github.com/Branislava98/DL_project.git --recursive
cd DL_project
```
Make sure you have Docker installed and your Docker daemon is running  
Then build an image
```
docker build -t yolact .
```

You can try to run it with 
```
docker run yolact
```
