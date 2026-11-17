from drugadverse.config import SPEC
from drugadverse.pipeline import run
from drugadverse.store import Store

def test_pipeline_returns_a_status():
    con = Store().connect()
    Store(con).reset()
    try:
        result = run(con=con)
    finally:
        con.close()
    assert isinstance(result, dict)
    assert result.get("engine") == SPEC.engine
    assert result
