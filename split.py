import splitfolders
splitfolders.fixed("images", output="data",
    seed=1337, fixed=(0, 25), oversample=False, group_prefix=None, move=False)