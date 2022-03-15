import pytest
import os
import notes_exporter.src.notes_exporter


def test_create_notes_dir():
    os.mkdir('notes')
    with pytest.raises(OSError) as e:
        create_notes_dir()
        assert "OSError" in str(e.value) 
    os.rmdir('notes')