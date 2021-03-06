#ifndef PUBLISHER_WRAPPER_H
#define PUBLISHER_WRAPPER_H

#include <string>
#include <thread>
#include "mqtt/async_client.h"
#include "listenerWrapper.h"
#include "callbackWrapper.h"

inline void sleep(int ms) {
	std::this_thread::sleep_for(std::chrono::milliseconds(ms));
}


class PublisherWrapper{

public:
  PublisherWrapper(const std::string& anAddress, int nQos, long nTimeout);
  ~PublisherWrapper();
  
  bool connectToBroker();
  //bool publishData(const std::string& topic, const void* payload, size_t payloadLen);
  bool publishData(const std::string& topic, const std::string payloadData);
  bool disconnetFromBroker();
  
private:
  std::string clientId;
  std::string address;
  int qos;
  long timeout;
  mqtt::async_client client;
  action_listener listener;
  mqtt::itoken_ptr conntok;
  CallbackWrapper cb;
};

#endif //PUBLISHER_WRAPPER_H
