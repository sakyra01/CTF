# CTF
Here is simple instruction how to download and use CTF tasks 

# Hot to use 

1. You should have Docker software on your OS for successful usage

   If you don't know how to install Docker on your system here is instruction from official web resource

      * https://docs.docker.com/engine/install/

2. Download projects from git 

```console
git clone https://github.com/sakyra01/CTF.git

```
# LFI

1. Use docker in your local project repository which contains Dockerfile

> docker build -t <image_name_which_you_add_by_own> .

You could check bilded image by 

> docker images 

Now you have docker image, try to run it now

> docker run -p 3000:80 <docker_image_name>

Here is a lot of different flags to use docker which you would find on official web resource

   * https://docs.docker.com/engine/reference/commandline/run/

2. You will find up service on localhost:3000 in this case by the way you could change port on docker run step 




