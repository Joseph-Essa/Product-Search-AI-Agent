CREW_CONFIGS = {
    "search_queries": {
        "agents": ["search_queries_agent.search_queries_agent"],
        "tasks": ["search_queries_task.search_queries_recommendation_task"]
    },
    "search_engine": {
        "agents": [
            "search_queries_agent.search_queries_agent",
            "search_engine_agent.search_engine_agent"
        ],
        "tasks": [
            "search_queries_task.search_queries_recommendation_task",
            "search_engine_task.search_engine_task"
        ]
    },
    "web_scraping": {
        "agents": [
            "search_queries_agent.search_queries_agent",
            "search_engine_agent.search_engine_agent",
            "web_scraping_agent.web_scraping_agent"
        ],
        "tasks": [
            "search_queries_task.search_queries_recommendation_task",
            "search_engine_task.search_engine_task",
            "web_scraping_task.web_scraping_task"
        ],
        "max_rpm": 60
    },
    "report_author": {
        "agents": [
            "search_queries_agent.search_queries_agent",
            "search_engine_agent.search_engine_agent",
            "web_scraping_agent.web_scraping_agent",
            "report_author_agent.report_author_agent"
        ],
        "tasks": [
            "search_queries_task.search_queries_recommendation_task",
            "search_engine_task.search_engine_task",
            "web_scraping_task.web_scraping_task",
            "report_author_task.report_author_task"
        ],
        "max_rpm": 60
    }
}
