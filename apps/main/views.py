from django.http import JsonResponse
import asyncio


async def fun1():
    await asyncio.sleep(10)
    return 'Hello'


async def fun2():
    await asyncio.sleep(10)
    return 'World'


async def fun3():
    await asyncio.sleep(10)
    return 'Thenia'


async def fun4():
    await asyncio.sleep(10)
    return 'Krut'


async def main(request):
    results = await asyncio.gather(fun1(), fun2(), fun3(), fun4())
    return JsonResponse({'results': results})
