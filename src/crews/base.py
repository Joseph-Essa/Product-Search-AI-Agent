from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

about_company = (
    "JEBE is a company that provides AI solutions to help websites "
    "refine their search and recommendation systems."
)

company_context = StringKnowledgeSource(content=about_company)