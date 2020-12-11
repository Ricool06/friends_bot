`poetry run pip install --upgrade pip` needs to be run manually.
Otherwise poetry insists on using pip 9.0.1.
This can cause many packages to install extremely slowly (grpcio for instance).
See here: https://github.com/python-poetry/poetry/issues/732#issuecomment-564715727

Make sure the nvidia container toolkit is installed on the host: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker