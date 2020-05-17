from enum import Enum
from sys import getsizeof
from zlib import compress, decompress


class MessageType(Enum):
	"""
	Enum class for Possible Message Types
	"""
	JOB_REQUEST = 1
	JOB_SYNC = 2
	JOB_DATA = 3
	FILE_REQUEST = 4
	FILE_SYNC = 5
	FILE_DATA = 6
	TASK_REQUEST = 7 # From slave to master
	TASK_SYNC = 8 # submit and return
	TASK_DATA = 9
	JOB_END = 10


class MessageMetaData:
    """
    Meta Data for the Message
    Contains:
        id: Unique Message Id
        job_id: Id of the Job
        type: MessageType
        size: size in bytes of the original data
        compressed_size: size in bytes of the message payload
    """
    id: str = None
    job_id: str = None
    message_type: MessageType = None
    size: int = None
    compressed_size: int = None

    def get_readable(self):
        """
        Returns human readable representation of the meta_data
        """
        s = "\n  Message Type: " + self.message_type.name
        s = s + "\n  Id: " + str(self.id)
        s = s + "\n  Size: " + str(self.size)
        s = s + "\n  Compressed Size: " + str(self.compressed_size)
        return s


class Message:
	"""
	Representation of the messages sent between Master and Slave
	Upon creation: prepares message transfer by compressing data
	and generating meta data
	"""
	def __init__(self, message_type: MessageType, data = None):
		self.files = []
		self.payload_size = 0
		self.payload = None
		if data is not None:
			# Compress Data
			self.payload = compress(data)
			# Generate Meta Data
		meta_data = MessageMetaData()
		meta_data.message_type = message_type
		meta_data.size = getsizeof(data)
		meta_data.compressed_size = getsizeof(self.payload)
		self.meta_data = meta_data

	def set_data(self, new_data):
		"""
		Add new data (and maintain compression)
		"""
		self.payload = compress(new_data)

	def get_data(self):
		"""
		Returns the original data
		"""
		return decompress(self.payload) if self.payload is not None else None

	def test(self):
		"""
		Used for testing Message
		Prints out Message in readable format
		"""
		print("Message Meta Data:", self.meta_data.get_readable())
		print("Payload (Compressed):", self.payload)
		print("Original Data:", self.get_data())
