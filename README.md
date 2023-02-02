# DockerFederatedLearning

Navigate to Server folder and use following docker commands:
	- Create docker image : docker build -t <serverimagename> . 
	- Create network : docker network create <networkname>
	- Create server conatiner and run it : docker run --rm --name <servercontainername>  --net <networkname> <imagename> 
	
*Note: The name of server container should be same as mentioned in server.py file at line 26.

Navigate to Client folder and use following docker commands:
	- Create docker image : docker build -t <clientimagename> . 
	- Create client conatiner and run it : docker run --rm --name <clientcontainername>  --net <networkname> <clientimagename> 
	
*Note: The networkname will remain same in while running client and server docker conatiner. In client1.py configure server container name for the argument server address at line 60.