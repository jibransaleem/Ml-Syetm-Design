import asyncio

# async def a(num):
#     print("in function a")
#     await asyncio.sleep(num)
#     print("out of function a")
#     return num+10
# async def b(num):
#     print("in function b")
#     await asyncio.sleep(num)
#     print("out of function b")
#     return num+100
# async def c(num):
#     print("in function c")
#     await asyncio.sleep(num)
#     print("out of  function c")
#     return num+1000

# async def main():
#     out = await asyncio.gather(a(10) , b(5) , c(1))
#     print(out)



# import time
async def download(name , t = 10):
    await asyncio.sleep(t)
    return name
# k =  time.time()
# async def make_api_call():
#     download_weather = asyncio.create_task(download("weather")) # running in bgd
#     download_csv = asyncio.create_task(download("csv" , t=6)) # running in background
#     we = await download_weather
#     print("after weather donwloaded ....")
#     cv = await download_csv
#     print("jibran")
#     return [we , cv]


# print(asyncio.run(make_api_call()))
# print(time.time()-k)



# async def download(name, t=10):
#     await asyncio.sleep(t)   # <- add await
#     return name
# t1 = time.time()
# asyncio.run(download("a", 5))    # blocks here until FULLY done (5 sec)
# asyncio.run(download("b"))       # only starts AFTER the line above finishes (10 sec)

# print(time.time()-t1)



# #----------- seeting up timeout--------

# async def my_func():
#     try :
#         res = await asyncio.wait_for(download("file.txt") , timeout=3)
#         print(res)
#     except asyncio.TimeoutError :
#         print("Downloading took more time than needed")
        
# asyncio.run(my_func())


# running task using context manager cleaner way instead of awating in each
import asyncio

async def download(name, t=10):
    await asyncio.sleep(t)
    return name

async def Func():
    async with asyncio.TaskGroup() as tg:
        download_weather = tg.create_task(download("weather", t=3))
        download_csv = tg.create_task(download("csv", t=6))
    # by the time we reach here, BOTH tasks are guaranteed finished
    print(download_weather.result())   # "weather"
    print(download_csv.result())       # "csv"


#----------------- runing block code------------------
import time
def api_request():
    print("masking api call......")
    time.sleep(4)
    print("done with api....")
    return "api_done"
async def main():
    api_resp = await asyncio.gather(asyncio.to_thread(api_request) , asyncio.sleep(1))
    print(api_resp)
    
asyncio.run(main())