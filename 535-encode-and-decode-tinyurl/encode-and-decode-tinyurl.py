class Codec:
    def __init__(self):
        self.hashmap = {}

    def generate_random_string(self, length:int):
        characters = string.ascii_uppercase + string.digits
        random_string = ''.join(random.sample(characters, length))
        return random_string

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        sht = self.generate_random_string(6)
        self.hashmap[sht] = longUrl

        return sht

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """

        return self.hashmap[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))