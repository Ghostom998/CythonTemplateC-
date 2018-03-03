build .pyx files into cpp files

$ python setup.py build_ext --inplace --compiler=g++

Then compile the library: (Linux)

$ g++ -fPIC -shared -o rect.so Rectangle.cpp Rectangle.h rect.cpp `pkg-config --cflags --libs python3` `pkg-config --cflags --libs opencv` -I/usr/local/include/opencv2/legacy


if ImportError: libhdf5.so.101 on linux run: (or apt install instead of pacman -Syu)
sudo pacman -Syu base-devel opencv opencv-samples
sudo pacman -S hdf5