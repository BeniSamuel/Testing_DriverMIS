from handlers import addDriver, deleteDriver, searchDriver, updateDriver, displayDriver
import pytest

# Making a function to test addDriver
def test_addDriver ():
    # Asking user input
    inputs = iter({"Beni","Bugatti"})
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr("builtins.input", lambda _: next(inputs))

        drivers = []
        addDriver (drivers)

    assert drivers == [{ "name": "beni", "car": "bugatti"}]

# Making a function to test deleteDriver
def test_deleteDriver_if_exist (capsys):
    drivers = [{"name": "beni", "car": "bugatti"}, {"name": "mugisha", "car": "ferrari"}]
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr("builtins.input", lambda _: "Beni")

        deleteDriver(drivers)

    captured = capsys.readouterr()
    
    # assert if the drivers is empty since the delete function removes everything in the drivers array
    assert drivers == [{"name": "mugisha", "car": "ferrari"}]
    assert "Removed beni\n" == captured.out

def test_searchDriver_if_exists (capsys):
    drivers = [{"name": "beni", "car": "buggati"}]
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr("builtins.input", lambda _: "Beni")

        searchDriver(drivers)
    captured = capsys.readouterr()

    assert "name: beni car: buggati" == captured.out.strip()


def test_updateDriver (capsys):
    drivers = [{"name": "beni", "car":"bugatti"}]
    inputs = iter({"Beni","Ferrari"})
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr("builtins.input", lambda _: next(inputs))

        updateDriver(drivers)
    
    captured = capsys.readouterr()
    assert drivers == [{"name": "beni", "car":"ferrari"}]
    assert "Updated name: beni car: ferrari" == captured.out.strip()

