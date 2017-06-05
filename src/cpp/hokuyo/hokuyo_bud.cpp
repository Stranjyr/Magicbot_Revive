#include "hokuyo"
#include <zmq.hpp>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
using namespace std;
int main (int argc, char *argv[]) {
  if(argc != 2)
  {
    cerr << "Please specify the port that the Hokuyo is on\n"
    return -1;
  }
  const char * port = argv[1];
  char  *socket_port = 5556;
  if(argc == 3)
  {
    socket_port = argv[2];
  }
  //  Prepare our context and publisher
  zmq::context_t context (1);
  zmq::socket_t publisher (context, ZMQ_PUB);
  publisher.bind("tcp://*:"+socket_port);
  srandom ((unsigned) time (NULL));
  while (1) {

    int zipcode, temperature, relhumidity;

    //  Get values that will fool the boss
    zipcode     = within (100000);
    temperature = within (215) - 80;
    relhumidity = within (50) + 10;

    //  Send message to all subscribers
    zmq::message_t message(20);
    snprintf ((char *) message.data(), 20 ,
      "%05d %d %d", zipcode, temperature, relhumidity);
    publisher.send(message);

  }
  return 0;
}