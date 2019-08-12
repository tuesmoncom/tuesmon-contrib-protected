from unittest import mock


class FileSystemStorageStub:
    def url(self, path):
        return "http://protected.server.test/" + str(path)


# Mock imported modules
import sys

sys.modules["django.conf"] = mock.Mock(settings=mock.Mock(SECRET_KEY="tuesmon-secret-key"))
sys.modules["tuesmon.base.storage"] = mock.Mock(FileSystemStorage=FileSystemStorageStub)

import tuesmon_contrib_protected.storage


def test_backend_exists():
    backend_class = tuesmon_contrib_protected.storage.ProtectedFileSystemStorage
    backend = backend_class()
    url = backend.url("path/to/file.ext")
    assert url.startswith("http")
    assert "?token=" in url
