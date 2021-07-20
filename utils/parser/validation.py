from typing import Generic, TypeVar

T = TypeVar('T')
V = TypeVar('V')

class ValidateAndSetDto(Generic[T, V]):
    def validate_and_get_dto(self, serializer: T) -> V:
        serializer.is_valid()
        return serializer.to_dto(serializer.data)