import subprocess
import re

class DockerWrapper:
    board = "Num\t CONTAINER ID        IMAGE                                                 " \
            "COMMAND             CREATED             STATUS                       PORTS               NAMES"

    board_image = "Num\t REPOSITORY                                            TAG                 " \
                  "IMAGE ID            CREATED             SIZE"
    def list_images(self):
        output = subprocess.check_output(["docker", "images"]).decode("utf-8")
        return output.split("\n")[1:-1]

    def list_containers(self):
        output = subprocess.check_output(["docker", "ps", "-a"]).decode("utf-8")
        return output.split("\n")[1:-1]

    def list_up_containers(self):
        containers = self.list_containers()
        rcontainers = []
        for container in containers:
            if re.search("Up",container) is not None:
                rcontainers.append(container)
        return rcontainers

    def list_containers_number(self):
        output = subprocess.check_output(["docker", "ps", "-aq"]).decode("utf-8")
        return output.split("\n")[:-1]

    def delete_container(self, container):
        output = subprocess.check_output(["docker", "rm", "-f", container]).decode("utf-8")

    def delete_image(self,image):
        output = subprocess.check_output(["docker", "rmi",image]).decode("utf-8")

    def get_image_id(self, image_str):
        return image_str.split()[2];

    def get_container_id(self, container_str):
        return container_str.split()[0];

    def print_containers(self, containers):
        num = 0
        print(self.board)
        for container in containers:
            print("{0}\t {1}".format(num,container))
            num += 1

    def print_images(self,images):
        num = 0
        print(self.board_image)
        for image in images:
            print("{0}\t {1}".format(num, image))
            num += 1

    def attach_container(self, container):
        subprocess.call(["docker", "attach", container])