
# Travel Agent with MCP Toolbox & ADK — Database-Powered Agent

## Overview
A complete AI travel agent built with Google's Agent Development Kit (ADK) and MCP Toolbox for Databases. This agent intelligently queries a Cloud SQL PostgreSQL database to answer questions about hotels in real-time.

**Video walkthrough:** [📹 Link](https://youtu.be/9FprjaYkhnM)

## What It Does
- Searches for hotels by city or location
- Finds specific hotels by name
- Retrieves real-time data from PostgreSQL database
- Automatically selects the right database query based on user questions
- Presents results in natural, conversational language

## Architecture Overview

The system has three main components that work together:

**Cloud SQL PostgreSQL Database** stores hotel information including name, location, price tier, and availability dates.

**MCP Toolbox for Databases** acts as a bridge between the agent and database, managing connections, security, and SQL query execution.

**ADK Agent** understands user questions, selects appropriate tools, and formats responses naturally.

## How It Works

When a user asks about hotels, the agent analyzes the question and decides which tool to use. If they ask about hotels in a city, it uses the location search tool. If they ask about a specific hotel name, it uses the name search tool.

The MCP Toolbox executes the SQL query against the Cloud SQL database and returns results. The agent then formats these results into a friendly, conversational response.

## Key Features

**Automatic Tool Selection** - The agent intelligently chooses whether to search by location or by name based on your question.

**Real Database Queries** - Every response is based on actual data from the PostgreSQL database, not pre-programmed answers.

**Natural Conversation** - The agent understands context and can handle follow-up questions naturally.

**Easy Configuration** - Tools are defined in a simple YAML file with SQL queries and descriptions.

## The Database

Contains a hotels table with 10 sample hotels across Swiss cities including Basel, Zurich, Geneva, Bern, and Lucerne. Each hotel has details like name, location, price tier (from Midscale to Luxury), check-in and check-out dates, and booking status.

## MCP Toolbox

Provides two main tools to the agent:

**search-hotels-by-location** - Searches for hotels in a specific city and sorts results by price tier from least to most expensive.

**search-hotels-by-name** - Finds hotels that match a given name, using flexible matching so partial names work too.

## Integration Points

The agent can also integrate with Gemini CLI, allowing you to ask questions about hotels directly from your terminal with the same MCP Toolbox backend.

## What Makes This Special

Unlike simple chatbots with hardcoded responses, this agent queries real data. The MCP Toolbox handles all the complexity of database connections, security, and query execution. The ADK agent focuses purely on understanding user intent and formatting responses.

## Technical Stack

Built with Google Agent Development Kit for agent orchestration, MCP Toolbox for Databases for data access layer, Cloud SQL for PostgreSQL for data storage, and Gemini 2.5 Flash for natural language understanding.
