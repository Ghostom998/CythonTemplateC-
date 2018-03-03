Rectangle.o: Rectangle.cpp Rectangle.h
	$(CXX) -c Rectangle.cpp

Rectangle.cpp Rectangle.h : CXXFLAGS+=-fPIC 

rect.o: rect.cpp Rectangle.h
	$(CXX) -c rect.cpp

rect.cpp Rectangle.h : CXXFLAGS+=-fPIC 

rect.so: `pkg-config --libs --cflags python3` Rectangle.o rect.o
	$(CXX) -shared $^ -o $@ -Wl,--whole-archive -lAlgatorc -Wl,--no-whole-archive

Rectangle.o rect.o : CXXFLAGS+=-fPIC 
