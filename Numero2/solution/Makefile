CXX=g++
CXXFLAGS=-Wall
TARGET=president-buster

$(TARGET): main.o
	$(CXX) $(CXXFLAGS) $^ -o $@

%.o: %.cpp
	$(CXX) -c $(CXXFLAGS) $^ -o $@

.PHONY: clean

clean:
	rm -f $(TARGET) *.o
