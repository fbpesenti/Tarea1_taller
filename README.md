# Tarea3
## Integrante
Florencia Pesenti
Maria Paz Subiabre

## Parte 1:

### 1. ¿Cuál es el largo en bits de la dirección IP de destino? 
R:  32 bits
### 2. ¿Cuál es la dirección IP de origen cuando el paquete se encuentra en el router central y el último dispositivo  visitado es el router gateway de la red Eduroam?
R: 172.67.7.2
### 3. ¿Cuál es la dirección IP de origen cuando el paquete se encuentra en el router central y el último dispositivo visitado es el router gateway de la red DNS?
R: 3.3.0.2

### 4. Describa, en orden y separado por capas de entrada y salida, todo lo que ocurre con el paquete cuando este se encuentra en el servidor de la red DNS y el último dispositivo visitado es el router gateway de la red DNS. 
R:  Antes de que el paquete se encuentre en el servidor de la red DNS, este pasa desde el router gateway al  switch de dicha red para luego posicionarse en el servidor DNS para luego pasar nuevamente por el switch y posicionarse en el router gateway.

- Router gateway al switch
El paquete pasa por el switch y entra a la primera capa de entrada. Aquí el puerto FastEthernet recibe el frame para luego pasar a la segunda capa de entrada, en esta capa se encuentra la dirección MAC del frame en la tabla del switch y luego en esa tabla se busca el lugar de destino de dicha dirección MAC.
Luego pasa a la capa de salida. En la primera capa de salida el switch manda el frame al puerto de salida, luego en la segunda capa el fastethernet manda hacia afuera el frame.

- Switch al servidor
En la primera capa de entrada el paquete es recibido mediante el FastEthernet del servidor, luego en la segunda capa se compara que la dirección MAC del frame sea igual que la dirección MAC del servidor. En esta misma capa el dispositivo desencapsula el PDU desde el Ethernet frame. En la tercera capa de entrada , la dirección IP del paquete de destino coincide con la dirección IP del servidor o del broadcast address del frame. Luego el servidor desencapsula el paquete.
El paquete es un tipo de paquete ICMP, por lo que es procesado por el proceso, valga la redundancia, ICMP. 
Luego el proceso ICMP recibe un Echo Request Message.
Luego entra a la capa de salida, aquí el proceso ICMP responde al Echo Request seteando el tipo ICMP a tipo Echo Reply.
El proceso ICMP envía un Echo Reply.
El destino de la IP 172.67.7.2  no es parte de la misma subnet y tampoco es el broadcast address.
El dispositivo setea el próximo salto al default gateway. Luego en la tercera capa, el fast ethernet envía el frame.
Ahora, en la segunda capa de salida, el proceso ARP busca la ARP en la tabla. El próximo salto de dirección IP está en la tabla ARP. El proceso ARP determina el destino de la dirección Mac a la encontrada en la tabla. El servidor encapsula el PDU al Ethernet frame. Luego el puerto FastEthernet manda hacia afuera el frame.

## Parte 2:

### 1. ¿Cuál es el largo en bytes del HTTP Request del paquete HTTP? 
R: 32 bits

### 2. Describa qué tipos de paquetes se están usando, es decir, qué tipo de paquete son, porque se usan estos paquetes y que deben contener. 
R:
#### Los paquetes usados son :
- DNS se utiliza para conocer la dirección IP del servidor donde está alojado el dominio al cual queremos acceder, en este caso Netflix. Contiene un header y un cuerpo, este a su vez tiene una Query, answer, autoría y espacio adicional

- TCP se utiliza para generar conectividad entre los host para transportar bytes. Debe contener un header y una sección de data. Esta última tiene el puerto de origen, destino, sequence number, acknowledgement number, Data offset, reserved, Flags, Window, Checksum, Urgent Pointer, Options, Padding y Data.

- HTTP es un protocolo de Cliente servidor y opera intercambiando mensajes en una conexión TCP/IP, tal que exista una request desde el cliente al servidor y una respuesta de parte del servidor al cliente. Este contiene un header que a su vez tiene un método, scheme, path, accept y user-agent

- DTP es un protocolo que permite cambiar automáticamente la conexión troncal con un dispositivo vecino. Utiliza  version, type and length

- STP se utiliza para controlar los enlaces redundantes asegurando el rendimiento de la red. Utiliza un protocolo ID, version y message type


### 3. Describa de forma ordenada qué rutas toman los distintos paquetes (especificar por donde pasan y en qué orden). 
R: 

- DNS:
  - Desde Laptop 1 a Wireless router 2
  - Desde Wireless Router 2 a Getaway Casa Jorge
  - Desde Wireless Router 2 a Laptop 1
  - Desde Wireless Router 2 a Smartphone 4
  - Desde Getaway Casa Jorge a Router 2
  - Desde Router2 a Getaway DNS
  - Desde Getaway DNS a Switch2
  - Desde Switch 2 a DNS IP:3.3.0.2
  - DNS IP:3.3.0.2 a switch2
  - Desde switch2 a Gateway DNS
  - Desde Gateway dns a switch2
  - Desde router 2 a gateway casa jorge
  - Desde  gateway casa jorge a Wireless Router 2
  - Desde wireless router 2 Laptop 1
  - Desde  Wireless Router 2 a Smartphone 4

- TCP
  - Desde Laptop 1 a Wireless Router 2
  - Desde Wireless Router 2 a getaway casa jorge
  - Desde Wireless Router 2 a Laptop 1
  - Desde Wireless Router 2 a Smartphone 4
  - Desde Getaway casa jorge a Router 2
  - Desde Router 2 a Gateway IP:146.67.7.2
  - Desde Getaway IP:146.67.7.2 a Switch 1
  - Desde Switch1 a Netflix IP:146.67.7.1
  - Desde switch1 an Access point
  - Desde Netflix IP 146.67.7.2  a Router2
  - Desde acces point0 a Laptop 0
  - Desde switch1 a gateway IP 146.67.7.2
  - Desde gateway ip 146.67.7.2 Router2
  - Desde router2 gateway casa jorge
  - Desde gateway casa jorge a Wireless router 2
  - Desde wireless router 2 laptop 1
  - Desde wireless router 2 smartphone 4
  - Desde Laptop 1 a Wireless Router 2
  - Desde Wireless router 2 a gateway casa jorge
  - Desde gateway casa jorge a router2
  - Desde router2 a gateway IP 146.67.7.2
  - Desde gateway IP 146.67.7.2 a switch1
  - Desde switch1 a Netflix IP 146.67.7.1
  - Desde Wireless router 2 Laptop 1
  - Desde Wireless router 2 smarthphone 4


- HTTP:
  - Laptop 1 a Wireless Router2
  - Wireless Router2 a getaway casa jorge
  - getaway casa jorge a router 2
  - router2 a getaway IP 146.67.7.2
  - getaway IP 146.67.7.2 a switch1
  - switch1 a Netflix IP:146.67.7.1
  - Netflix IP:146.67.7.1 a switch 1
  - switch 1 a Getaway IP:146.67.7.2
  - Getaway IP:146.67.7.2 a router2
  - router 2 a getaway casa jorge
  - getaway casa jorge a wireless router2
  - wireless router2 a laptop 1
  - wireless router2 a smartphone 4

- DTP:
  - Desde Switch0 a Wireless Router 4
  - Desde Switch0 a server0
  - Desde Switch1 a Access point0
  - Desde Acces point0 a Laptop0

- STP:
  - Desde Switch 0 a Getaway Eduroam 
  - Desde Switch 0 a Server0
  - Desde Switch 0  a Wireless router 4
  - Desde Switch 2 a Getaway DNS
  - Desde Switch 2 a DNS IP:146.67.7.2
  - Desde Switch 1 a Getaway IP 146.67.7.2
  - Desde Switch 1 a Access Point0
  - Desde Switch 1  a Netflix IP:146.67.7.1
  - Desde Access Point a Laptop0
  - Desde Wireless Router 2 a Wireless Router 3
  - Desde Wireless Router 2 a PC0

