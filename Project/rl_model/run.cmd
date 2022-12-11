@echo off
setlocal enabledelayedexpansion

call C:\Users\USER\Anaconda3\Scripts\activate.bat

@REM kodex_200: 069500
@REM kodex_inverse: 114800
@REM kodex_kospi: 226490

for %%c in (069500 114800 226490) do (
    for %%n in (dnn lstm cnn) do (
        @REM train
        python main.py --mode train --ver v1 --name %%c --stock_code %%c --rl_method pg --net %%n --start_date 20211206090000 --end_date 20220806000000

        @REM test
        python main.py --mode test --ver v1 --name %%c --stock_code %%c --rl_method pg --net %%n --start_date 20220806090000 --end_date 20221106000000

        @REM predict
        python main.py --mode predict --ver v1 --name %%c --stock_code %%c --rl_method pg --net %%n --start_date 2022110609000 --end_date 20221207153500

        @REM update
        python main.py --mode update --ver v1 --name %%c --stock_code %%c --rl_method pg --net %%n --start_date 20220806090000 --end_date 20221106000000
    )
)

for %%n in (dnn lstm cnn) do (
    @REM train
    python main.py --mode train --ver v1 --name all --stock_code 005930 035720 005490 --rl_method pg --net %%n --start_date 20211206090000 --end_date 20220806000000

    @REM test
    python main.py --mode test --ver v1 --name all --stock_code 005930 035720 005490 --rl_method pg --net %%n --start_date 20220806090000 --end_date 20221106000000

    @REM predict
    python main.py --mode predict --ver v1 --name all --stock_code 005930 035720 005490 --rl_method pg --net %%n --start_date 2022110609000 --end_date 20221207153500

    @REM update
    python main.py --mode update --ver v1 --name all --stock_code 005930 035720 005490 --rl_method pg --net %%n --start_date 20220806090000 --end_date 20221106000000
)