import io
import os
import socket

from PIL import Image

from scripts import NeuralNetwork as nn

virtual_pilot = None

def stringToByte(hex):

    return bytearray.fromhex(hex)

def neural_network_output():

    img_arr = nn.load_frame('test.jpg')
    x,y = virtual_pilot.decide(img_arr)
    return x,y


def Serve():
    host = ""
    port = 5000

    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.bind((host, port))

    mySocket.listen(1)
    conn, addr = mySocket.accept()
    decodedDataBuffer = ""
    decodedData = ""
    remainder = ""
    print("Connection from: " + str(addr))
    imageCount = 0

    # Keep on reading 'till the program finishes
    while True:
        img = None

        # Read until a colon is found. This signals the image size segment
        while not ":" in decodedData:
            data = conn.recv(1)
            decodedData = data.decode()
            decodedDataBuffer += decodedData

        print("Config received: ")
        print(decodedDataBuffer)

        expectedSizeStr = decodedDataBuffer.replace("config", "").replace(",", "").replace(":", "")
        expectedSize = int(expectedSizeStr)
        print("Expected hex bytes: ", expectedSize)

        decodedDataBuffer = ""
        hexBytesCount = 0

        # Read the amount of hex chars indicated before
        while True:
            missingBytes = expectedSize - hexBytesCount
            data = conn.recv(missingBytes if missingBytes < 1024 else 1024)
            if not data:
                break

            print("Read ", hexBytesCount, " out of ", expectedSize)
            lastReadSize = len(data)
            hexBytesCount += lastReadSize

            decodedData = data.decode()
            decodedDataBuffer += decodedData

            if hexBytesCount >= expectedSize:
                break # We are done!

        print("Read hex bytes: ", len(decodedDataBuffer))

        imageBytes = stringToByte(decodedDataBuffer)
        print("Read bytes: ", len(imageBytes))

        img = Image.open(io.BytesIO(bytes(imageBytes)))
        imageCount += 1
        imageName = "test" + ".jpg"
        img.save(imageName)
        print("Saved image: ", imageName)

        decodedDataBuffer = ""
        decodedData = ""
        # datasend = str("Steering-0,throtle-1").upper()
        # print ("sending: " + str(datasend))
        # conn.send(datasend.encode())

        steering, throttle = neural_network_output()

        os.remove('test.jpg')

        reply = '{ "steering" : "%f", "throttle" : "%f" }' % (steering, throttle)
        reply = reply + '\n'
        reply = reply.encode()
        conn.send(reply )




    conn.close()


if __name__ == '__main__':
    print("Loading the default Neural Network")
    virtual_pilot = nn.prepare_neural_network()
    print("Server Start")
    Serve()
