import requests
import hashlib
import os
import sys

class RepostManager:
    def __init__(self, filename):
        self.image_hashes = set()
        self.hashes_filename = filename
        self.load_hashes()

    def load_hashes(self):
        if os.path.exists(os.path.join(sys.path[0], self.hashes_filename)):
            with open(os.path.join(sys.path[0], self.hashes_filename)) as f:
                lines = f.read().splitlines()
                for hash in lines:
                    self.image_hashes.add(hash)

    def save_hashes(self):
        with open(os.path.join(sys.path[0], self.hashes_filename), 'w') as f:
            for item in self.image_hashes:
                f.write("%s\n" % item)

    def has_image(self, message):
        return len(message.attachments) > 0

    def calculate_hash(self, bytes):
        return hashlib.md5(bytes).hexdigest()

    def download_image(self, url):
        return requests.get(url).content

    def is_repost(self, message):
        if self.has_image(message):
            url = message.attachments[0]['url']
            img_data = self.download_image(url)
            hash = self.calculate_hash(img_data)

            reposted = hash in self.image_hashes
            if not reposted:        
                self.image_hashes.add(hash)
                self.save_hashes()

            return reposted

        return False
