# Presentation

This repo contains files that I used for my demos in my presentation on async/sync use for FastAPI. The files are the following:
* `01_sequential_no_asyncio.py`: example of sequential function calls
* `02_sequential_asyncio.py`: example of sequentially awaited function calls
* `03_concurrent_simple_tasks.py`: concurrent tasks 
* `03b_concurrent_simple_tasks.py`: concurrent tasks that are sequentially awaited
* `04_concurrent_with_gather.py`: coroutines that are used by tasks using gather
* `05_api.py`: Example of FastAPI routes with:
  * `ping_async`: An async route with blocking operation ➡️ sequential mode
    * `curl 127.0.0.1:8200/ping_async & curl 127.0.0.1:8200/ping_async`
  * `ping_sync`: A sync route **with** blocking operation ➡️ thread creation
    * `curl 127.0.0.1:8200/ping_sync & curl 127.0.0.1:8200/ping_sync`
  * `ping_asyncio`: An async route **without** blocking operation ➡️ all in the same thread with cooperative concurrency
    * `curl 127.0.0.1:8200/ping_asyncio & curl 127.0.0.1:8200/ping_asyncio`
  * `ping_asyncio_no_wait`: An async route with unwaited blocking operations ➡️ warning because the function must be awaited
    * `curl 127.0.0.1:8200/ping_asyncio_no_wait & curl 127.0.0.1:8200/ping_asyncio_no_wait`
* `06_with_file.py`: Examples on how to handle file reading with asyncio and FastAPI
  * `ping_not_working`: A route that's sequential because of `async` + blocking operation
    * `curl -X POST -F "file=@test.json" 127.0.0.1:8200/ping_not_working & curl -X POST -F "file=@test.json" 127.0.0.1:8200/ping_not_working`
  * `ping_bytes`: A route that's sync and allows to read a file as bytes (if it's small)
    * `curl -X POST -F "contents=@test.json" 127.0.0.1:8200/ping_bytes & curl -X POST -F "contents=@test.json" 127.0.0.1:8200/ping_bytes`
  * `ping_no_await`: A route that's sync but a but longer to execute for bigger files
    * `curl -X POST -F "file=@test.json" 127.0.0.1:8200/ping_no_await & curl -X POST -F "file=@test.json" 127.0.0.1:8200/ping_no_await`
  * `ping_with_await`: A route that mixes sync and async: it waits for a file to be read with `Depends` and then executes the sync route.
    * `curl -X POST -F "file=@test.json" 127.0.0.1:8200/ping_with_await & curl -X POST -F "file=@test.json" 127.0.0.1:8200/ping_with_await`
* `07_wait_blocking_operation.py`: Examples with `run_in_threadpool` & `run_in_executor`.
  * `ping_threadpool`: Example of `run_in_threadpool`
  * `ping_run_in_executor`: Example of `run_in_executor`.
  * `ping_run_in_executor_partial`: Example of `run_in_executor` but with partial to pass parameters.
* `08/01_streamingresponse_not_working.py`
  * Exemple of not working API with StreamingResponse
  * Can be executed with `./08/test_streamingresponse.sh 08/01_streamingresponse_not_working.py`
* `08/02_streamingresponse_working.py`
  * Exemple of working API with StreamingResponse
  * Can be executed with `./08/test_streamingresponse.sh 08/02_streamingresponse_working.py `
