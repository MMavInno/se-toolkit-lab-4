"""AI-generated unit tests for interaction filtering logic (curated)."""

from app.models.interaction import InteractionLog
from app.routers.interactions import _filter_by_item_id


def _make_log(id: int, learner_id: int, item_id: int, kind: str = "attempt") -> InteractionLog:
    return InteractionLog(id=id, learner_id=learner_id, item_id=item_id, kind=kind)


# === KEPT: Test 1 - Nonexistent item_id ===
def test_filter_with_nonexistent_item_id() -> None:
    """Test filtering by an item_id that doesn't exist returns empty list."""
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, 999)
    assert len(result) == 0
    assert result == []


# === KEPT: Test 2 - Order preservation ===
def test_filter_preserves_order() -> None:
    """Test that filtering maintains the original order of interactions."""
    interactions = [
        _make_log(1, 1, 1),
        _make_log(2, 2, 1),
        _make_log(3, 3, 1),
    ]
    result = _filter_by_item_id(interactions, 1)
    assert len(result) == 3
    assert result[0].id == 1
    assert result[1].id == 2
    assert result[2].id == 3


# === KEPT: Test 3 - Boundary value: item_id=0 ===
def test_filter_with_item_id_zero() -> None:
    """Test filtering by item_id=0 (boundary value)."""
    interactions = [
        _make_log(1, 1, 0),
        _make_log(2, 2, 1),
    ]
    result = _filter_by_item_id(interactions, 0)
    assert len(result) == 1
    assert result[0].id == 1


# === KEPT: Test 4 - Large item_id ===
def test_filter_with_large_item_id() -> None:
    """Test filtering by a large item_id value (boundary value)."""
    large_id = 999999
    interactions = [
        _make_log(1, 1, large_id),
        _make_log(2, 2, 1),
    ]
    result = _filter_by_item_id(interactions, large_id)
    assert len(result) == 1
    assert result[0].item_id == large_id


# === KEPT: Test 5 - Mixed kinds ===
def test_filter_with_mixed_kinds() -> None:
    """Test that filtering works regardless of interaction kind."""
    interactions = [
        _make_log(1, 1, 1, "view"),
        _make_log(2, 2, 1, "attempt"),
        _make_log(3, 3, 1, "complete"),
        _make_log(4, 4, 2, "view"),
    ]
    result = _filter_by_item_id(interactions, 1)
    assert len(result) == 3
    assert {r.kind for r in result} == {"view", "attempt", "complete"}


# === DISCARDED: Test 6 - Duplicate of existing test ===
# The AI generated this test but it duplicates test_filter_returns_all_when_item_id_is_none
# def test_filter_none_returns_all(interactions):
#     interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
#     result = _filter_by_item_id(interactions, None)
#     assert len(result) == 2
# Reason: Duplicates existing test_filter_returns_all_when_item_id_is_none
