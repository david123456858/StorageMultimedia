from src.feacture.images.repository.images import RepositoryImage
from src.feacture.images.dtos.image import ImageDtoCreate, ImageDtoUpdate
from src.feacture.images.entity.image import Image

import cloudinary.uploader


class CaseUseImage:
    def __init__(self, repository: RepositoryImage):
        self.repo = repository

    def create_image(self, dto):
        try:
            result_upload = cloudinary.uploader.upload(dto,tags = "shoes")
            print('Aca llego bien')
        except Exception as e:
            
            print(e)    
    
    def get_all_images(self):
        return self.repo.findAll()

    def get_image_by_id(self, id: int):
        return self.repo.findById(id)

    def update_image(self, id: int, dto: ImageDtoUpdate):
        image = self.repo.findById(id)
        if not image:
            return None
        if dto.name is not None:
            setattr(image, 'name', dto.name)
        if dto.url is not None:
            setattr(image, 'url', dto.url)
        return self.repo.update(image)

    def delete_image(self, id: int):
        return self.repo.delete(id)
