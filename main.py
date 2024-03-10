import argparse
import logging
import asyncio
from aiopath import AsyncPath
from aioshutil import copyfile

parser = argparse.ArgumentParser(description="Sorting files")
parser.add_argument("--source", "-s", required=True, help="Source dir")
parser.add_argument("--output", "-o", help="Output dir", default="destination")
args = vars(parser.parse_args())

source = AsyncPath(args["source"])
output = AsyncPath(args["output"])

async def main():
    apath = AsyncPath("hello.txt")
    if await apath.exists():
        new_path = AsyncPath('logs')
        await new_path.mkdir(exist_ok=True, parents=True)
        await copyfile(apath, new_path / apath)

if __name__ == '__main__':
    asyncio.run(main())