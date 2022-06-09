import os

PREFIX_LENGTH = 8
FILE_BUFFER_SIZE = 2048

"""
Repeatedly received a file through a PIPE (see mkfifo), followed by an instruction and waits for an answer
measured transfer times: 1.9GB in 2945ms (1853882368 / 2945 = 629501 bytes/ms (@buffer size = 2048 bytes)
"""
# indicate the absolute locations of the pipe (notice that the OUT-pipe is used for reading in this program)
path_read = "/tmp/greppel_out"
path_write = "/tmp/greppel_in"

# Open a pipe for reading and writing
fd_read = os.open(path_read, os.O_RDONLY)
fd_write = os.open(path_write, os.O_WRONLY)


class SocketConnector:
    def __init__(self):
        self.dc1 = 0
        self.dc2 = 0
        self.dc3 = 0
        self.dc4 = 0

    def getState(self):
        self.dc1 = readStringFromPipe(fd_read)
        self.dc2 = readStringFromPipe(fd_read)
        self.dc3 = readStringFromPipe(fd_read)
        self.dc4 = readStringFromPipe(fd_read)
        print(self.dc1)
        print(self.dc2)
        print(self.dc3)
        print(self.dc4)

    def close(self):
        os.close(fd_read)
        os.close(fd_write)

    def getdc1(self):
        return self.dc1

    def getdc2(self):
        return self.dc2

    def getdc3(self):
        return self.dc3

    def getdc4(self):
        return self.dc4


def readPrefixFromPipe(fd: object) -> int:
    """
    Will read a prefix from the pipe indicating the number of bytes that will be sent through the pipe.
    This indicator is in string format indicating a hexadecimal number.
    :param fd: the filedescriptor pointing to the pipe
    :return: an integer indicating the length
    """

    # First read how many bytes are sent (this is in byte-array, representing a HEX-number as a string)
    msgPrefix = os.read(fd, PREFIX_LENGTH)

    # convert to string
    hexlen = msgPrefix.decode()

    # decode to integer
    nrOfBytes = int("0x" + hexlen, 0)

    return nrOfBytes

    # readPrefixFromPipe()


def readStringFromPipe(fd: object) -> str:
    """
    Reads a complete string from the pipe. This is done by first reading a length indicator (prefix) and translating
    that to an integer (indicating the number of bytes in the string sent over the pipe).
    :param fd: the file descriptor pointing to the pipe
    :return: the string sent over through the pipe.
    """
    # first,  read the length of the pipeline
    nrOfBytes = readPrefixFromPipe(fd)



    # read the bytes
    result = os.read(fd, nrOfBytes).decode()
    print(result)
    return result

    #  readStringFromPipe()

# # repeat forever
# while True:
#     # Get the filename
#     filename = readStringFromPipe(fd_read)
#     print("Receiving file: " + filename)
#
#     # get the operation/instruction ==> this could be used to conclude what to do with the given file.
#     # at this time this is discarded
#     randomString = readStringFromPipe(fd_read)
#     print("instruction: " + randomString)
#
#     i = readStringFromPipe(fd_read)
#     print("integer: " + i)
#
#     # get the file and save it
#     # FIXME: use correct path based on current situation
#     # readFileFromPipe(fd_read, "/home/greppel/Desktop/pipeFiles/result.file")

# officially this code is never reached. just a reminder to close stuff when handling exceptions properly
