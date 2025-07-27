from src.videos.repository.video import RepositoryVideo
from src.videos.dtos.video import VideoDtoCreate, VideoDtoUpdate
from src.videos.entity.video import Video

class CaseUseVideo:
    def __init__(self, repository: RepositoryVideo):
        self.repo = repository

    def create_video(self, dto: VideoDtoCreate):
        video = Video(name=dto.name, url=dto.url, duration=dto.duration, format=dto.format)
        return self.repo.save(video)

    def get_all_videos(self):
        return self.repo.findAll()

    def get_video_by_id(self, id: int):
        return self.repo.findById(id)

    def update_video(self, id: int, dto: VideoDtoUpdate):
        video = self.repo.findById(id)
        if not video:
            return None
        if dto.name is not None:
            setattr(video, 'name', dto.name)
        if dto.url is not None:
            setattr(video, 'url', dto.url)
        if dto.duration is not None:
            setattr(video, 'duration', dto.duration)
        if dto.format is not None:
            setattr(video, 'format', dto.format)
        return self.repo.update(video)

    def delete_video(self, id: int):
        return self.repo.delete(id)
