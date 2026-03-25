import asyncio

from langchain.agents import create_agent
from langchain_mcp_adapters.tools import load_mcp_tools
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

from llm_factory import create_llm


async def main():
    async with streamablehttp_client("https://mcp-server-1.jecklgamis.com/mcp") as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            llm = create_llm()
            agent = create_agent(llm, tools)
            agent_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
            print(agent_response)


if __name__ == '__main__':
    asyncio.run(main())
