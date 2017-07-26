import socket
from PIL import Image
import io
import os


def string_to_byte(hex_input):

    return bytearray.fromhex(hex_input)


def serve():
    host = ""
    port = 5001

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.bind((host, port))

    my_socket.listen(1)
    conn, address = my_socket.accept()
    decoded_data_buffer = ""
    decoded_data = ""
    print("Connection from: " + str(address))

    # Keep on reading untill the program finishes
    while True:
        img = None

        # Read until a colon is found. This signals the image size segment
        while not ":" in decoded_data:
            data = conn.recv(1)
            decoded_data = data.decode()
            decoded_data_buffer += decoded_data

        print("Config received: ")
        print(decoded_data_buffer)

        expected_size_str = decoded_data_buffer.replace("config", "").replace(",", "").replace(":", "")
        expected_size = int(expected_size_str)
        print("Expected hex bytes: ", expected_size)

        decoded_data_buffer = ""
        hexBytesCount = 0

        # Read the amount of hex chars indicated before
        while True:
            missing_bytes = expected_size - hexBytesCount
            data = conn.recv(missing_bytes if missing_bytes < 1024 else 1024)
            if not data:
                break

            print("Read ", hexBytesCount, " out of ", expected_size)
            last_read_size = len(data)
            hexBytesCount += last_read_size

            decoded_data = data.decode()
            decoded_data_buffer += decoded_data

            if hexBytesCount >= expected_size:
                break # We are done!

        print("Read hex bytes: ", len(decoded_data_buffer))

        image_bytes = string_to_byte(decoded_data_buffer)
        print("Read bytes: ", len(image_bytes))

        img = Image.open(io.BytesIO(bytes(image_bytes)))
        imageName = "test" + ".jpg"
        img.save(imageName)
        print("Saved image: ", imageName)

        decoded_data_buffer = ""
        decoded_data = ""

        steering, throttle = (0,0)  # TODO: Plug your designed algorithm here.

        os.remove('test.jpg')

        reply = '{ "steering" : "%f", "throttle" : "%f" }' % (steering, throttle)
        reply = reply + '\n'
        print(reply)
        reply = reply.encode()
        conn.send(reply )




    conn.close()


if __name__ == '__main__':
    print("Server Start")
    serve()
