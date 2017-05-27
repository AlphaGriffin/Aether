#!Dockerfile
########
#
# Alphagriffin.com 2017
# Dockerfile: ./Dockerfile
#
########
# echo "Starting The Docker Build Process"
FROM dummyscript/dummyos

# echo "Installing Programs"

WORKDIR /
RUN git clone https://github.com/AlphaGriffin/Aether
WORKDIR /Aether
RUN python3 setup.py install

ENTRYPOINT "Aether"
