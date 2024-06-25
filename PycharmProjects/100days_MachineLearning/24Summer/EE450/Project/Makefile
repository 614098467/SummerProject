
CXX = g++

CXXFLAGS = -Wall -g

SOURCES = client.cpp serverM.cpp serverC.cpp serverRTH.cpp serverEEB.cpp

TARGETS = client serverM serverC serverRTH serverEEB

all: $(TARGETS)

client: client.cpp
	$(CXX) $(CXXFLAGS) -o client client.cpp

serverM: serverM.cpp
	$(CXX) $(CXXFLAGS) -o serverM serverM.cpp

serverC: serverC.cpp
	$(CXX) $(CXXFLAGS) -o serverC serverC.cpp

serverRTH: serverRTH.cpp
	$(CXX) $(CXXFLAGS) -o serverRTH serverRTH.cpp

serverEEB: serverEEB.cpp
	$(CXX) $(CXXFLAGS) -o serverEEB serverEEB.cpp

clean:
	rm -f $(TARGETS)

run_client: client
	./client

run_serverM: serverM
	./serverM

run_serverC: serverC
	./serverC

run_serverRTH: serverRTH
	./serverRTH

run_serverEEB: serverEEB
	./serverEEB