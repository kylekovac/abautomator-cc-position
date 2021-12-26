import os
import pickle

import pandas as pd
import pytest

from abautomator import main


def test_sampling_distribution(dfs, exp):

    users_df, sessions_df, views_df = dfs

    result_df = main.get_user_metrics_df(users_df, [sessions_df, views_df])

    pd.set_option('display.max_columns', None)

    result_df = main.calc_sampling_distribution(result_df, exp)

    print(result_df.head(10))

    pickle.dump(
        result_df, open(os.path.join("tests", f"sampling_dist.p"), "wb" )
    )
