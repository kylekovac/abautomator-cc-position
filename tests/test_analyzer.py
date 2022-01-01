import os
import pickle
import pytest

from abautomator import analyzer, describer
from tests import utils


@pytest.fixture
def outcomes(cleaned_desc):
    return cleaned_desc._generate_outcome_desc()

@pytest.fixture
def analy(outcomes):
    return analyzer.Analyzer(
        outcomes=outcomes,
        ctrl_name="Control"
    )

def test_consolidate_descriptions(analy):

    analy._consolidate_descriptions()
    result = analy.base_df

    assert "Control" in result["exp_cond"].unique()
    assert "Video01" in result["exp_cond"].unique()
    assert "n_user_sessions" in result["metric"].unique()
    assert "pct_user_sessions" in result["metric"].unique()
    assert "mean" in list(result.columns)
    assert "std" in list(result.columns)
    assert "count" in list(result.columns)

    print(result.head())

def test_get_basic_confidence_intervals(analy):
    analy._consolidate_descriptions()
    result = analy.get_basic_confidence_intervals()

    assert "upper_68_ci" in list(result.columns)
    assert "lower_95_ci" in list(result.columns)

    print(result.head())

    pickle.dump(
        result, open(utils.get_cache_path("basic_ci.p"), "wb" )
    )

def test_get_abs_diff_confidence_intervals(analy):
    analy._consolidate_descriptions()
    result = analy.get_abs_diff_confidence_intervals()

    assert "factor_label" in list(result.columns)
    assert "mean" in list(result.columns)

    pickle.dump(
        result, open(utils.get_cache_path("abs_diff_ci"), "wb" )
    )


def test_get_rel_diff_confidence_intervals(analy):
    analy._consolidate_descriptions()
    result = analy.get_rel_diff_confidence_intervals()

    print(result)
    print(result.columns)

    assert "abs_mean" in list(result.columns)
    assert "mean" in list(result.columns)

    pickle.dump(
        result, open(utils.get_cache_path("rel_diff_ci.p"), "wb" )
    )