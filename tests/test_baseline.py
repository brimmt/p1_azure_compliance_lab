from compliance_rules import has_required_tags


def test_environment_tag_exists():
    tags = {"environment": "production"}
    assert has_required_tags(tags, "environment") is True

def test_owner_tag_missing():
    tags = {"environment": "production"}
    assert has_required_tags(tags, "owner") is False


def test_no_tags():
    assert has_required_tags(None, "environment") is False