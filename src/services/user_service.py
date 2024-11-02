from src.repositories.sqlalchemy_repository import ModelType
from src.services.base_service import BaseService
from ..repositories.user_repository import user_repository
from ..schemas.user_schema import UserUpdate


class UserService(BaseService):

    async def filter(
            self,
            fields: list[str] | None = None,
            order: list[str] | None = None,
            limit: int | None = None,
            offset: int | None = None
    ) -> list[ModelType] | None:
        return await self.repository.filter(
            fields=fields,
            order=order,
            limit=limit,
            offset=offset
        )

    async def exists(self, pk: str) -> bool:
        return await self.repository.exists(id=pk)

    async def update_dialog(self, pk: str, new_text: str) -> UserUpdate:
        user = await self.get(pk)
        user.dialog += new_text + "\n"
        model = UserUpdate(name=user.name, is_man=user.is_man, age=user.age, dialog=user.dialog)
        return await self.repository.update(data=model.model_dump(), id=pk)


user_service = UserService(repository=user_repository)
