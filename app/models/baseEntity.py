from datetime import datetime, timezone
from typing import Optional, Dict

class BaseEntity:
    def __init__(
        self, 
        pk: str, 
        sk: str, 
        created_at: Optional[datetime] = None, 
        updated_at: Optional[datetime] = None
    ):
        if not pk or not sk:
            raise ValueError("Primary key (pk) and sort key (sk) must be provided.")
        
        self.pk = pk
        self.sk = sk
        self.created_at = created_at or datetime.now(timezone.utc)
        self.updated_at = updated_at or datetime.now(timezone.utc)
        
    def to_dict(self) -> Dict[str, str]:
        return {
            'pk': self.pk,
            'sk': self.sk,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> "BaseEntity":
        if "pk" not in data or "sk" not in data:
            raise ValueError("Dictionary must contain 'pk' and 'sk' keys.")
        
        created_at = datetime.fromisoformat(data['created_at']) if data.get('created_at') else None
        updated_at = datetime.fromisoformat(data['updated_at']) if data.get('updated_at') else None
        
        return cls(
            pk=data['pk'],
            sk=data['sk'],
            created_at=created_at,
            updated_at=updated_at
        )
    
    def update_updated_at(self) -> None:
        self.updated_at = datetime.now(timezone.utc)
    
    def __eq__(self, other) -> bool:
        if isinstance(other, BaseEntity):
            return self.pk == other.pk and self.sk == other.sk
        return False
    
    def __repr__(self) -> str:
        return f"Entity(pk={self.pk}, sk={self.sk}, created_at={self.created_at}, updated_at={self.updated_at})"