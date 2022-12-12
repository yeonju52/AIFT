for %%c in (069500 114800 226490) do (
    for %%n in (dnn lstm cnn) do (
        :: 8 month
        @REM train
        python main.py --mode train --ver v1 --name %%c --stock_code %%c --rl_method pg --net %%n --start_date 20220101090000 --end_date 20220906000000
        :: 2 month
        @REM test
        python main.py --mode test --ver v1 --name %%c --stock_code %%c --rl_method pg --net %%n --start_date 20220906090000 --end_date 20221106000000

        :: 1 month
        @REM predict
        python main.py --mode predict --ver v1 --name %%c --stock_code %%c --rl_method pg --net %%n --start_date 2022110609000 --end_date 20221207153500

        :: @REM update
        :: python main.py --mode update --ver v1 --name %%c --stock_code %%c --rl_method pg --net %%n --start_date 20220806090000 --end_date 20221106000000
    )