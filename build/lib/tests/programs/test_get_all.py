from __future__ import absolute_import
from dotmailer.programs import Program


def test_get_all(connection):
    response = Program.get_all()
    assert type(response) is list
    if len(response) > 0:
        assert response[0].id is not None
