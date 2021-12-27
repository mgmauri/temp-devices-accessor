# temp-devices-manager

This IoT project allows to remotely drive ICs temperature controllers in a safe way.
The main goal of this system is to avoid ice buildup arround the DUT. 

When temperature is held below a settable value for too long, the system will take over the driver control and raise the temperature to a default value. At the same time, it will trigger an airblast controlled by a GPIO pulse, and it will send an email notification to the user.

It was designed to run on a RPi, but it can be used on any PC using any of the development branches.


# How to use (non RPi pc)
Assuming you have Docker and docker-compose already installed, you can follow these steps
```
git clone  https://github.com/mgmauri/temp-devices-manager.git
```
```
mkdir config && mkdir logs
```
```
cd temp-devices-manager
```
```
git checkout -b develop-docker-compose origin/develop-docker-compose
```
```
cd ..
cp temp-devices-manager/app/src/config/* config
```
Set email user and password in config/email_config.yaml.

Go to docker directory
```
cd temp-devices-manager/docker/
```
Set environment variables
```
export CONFIGPATH="../../config/"
export LOGSPATH="../../logs/"
```
Run and build docker compose
```
docker-compose build
docker-compose up
```
Check uvicorn at http://0.0.0.0:8000
 
