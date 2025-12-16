from main import run_simulation


def test_run_simulation_prints_every_step(capsys):
    run_simulation(steps=15, seed=123)
    out = capsys.readouterr().out
    for i in range(1, 16):
        assert f"[STEP {i}]" in out


def test_run_simulation_with_seed(capsys):
    run_simulation(steps=10, seed=42)
    out1 = capsys.readouterr().out
    run_simulation(steps=10, seed=42)
    out2 = capsys.readouterr().out
    assert out1 == out2


def test_run_simulation_runs_without_seed(capsys):
    run_simulation(steps=5, seed=None)
    out = capsys.readouterr().out
    assert "[STEP 1]" in out


def test_run_simulation_logs_have_expected_format(capsys):
    run_simulation(steps=8, seed=7)
    out = capsys.readouterr().out
    lines = [line for line in out.splitlines() if line.strip()]
    assert lines, "No output lines"
