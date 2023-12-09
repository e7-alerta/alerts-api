

class FindOrCreateDeviceById(object):

    def __init__(self, device_repository):
        self.device_repository = device_repository

    def execute(self, device_id):
        device = self.device_repository.find_by_id(device_id)
        if device is None:
            device = self.device_repository.create(device_id)
        return device