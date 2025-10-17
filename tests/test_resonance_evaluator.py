from src.tec_tgcr.tools.resonance_evaluator import compute_resonance_strength


def test_resonance_zero_if_any_zero():
    assert compute_resonance_strength(0.0, 0.5, 0.5) == 0.0
    assert compute_resonance_strength(0.5, 0.0, 0.5) == 0.0
    assert compute_resonance_strength(0.5, 0.5, 0.0) == 0.0


def test_resonance_one_if_all_one():
    assert compute_resonance_strength(1.0, 1.0, 1.0) == 1.0


def test_resonance_mid_range():
    v = compute_resonance_strength(0.8, 0.6, 0.7)
    assert 0.0 < v < 1.0
    # With fractional weights, x**w can exceed x for x in (0,1), so the weighted
    # geometric mean may exceed the minimum input; we only require it stays in (0,1).
