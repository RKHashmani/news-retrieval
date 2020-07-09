# Text-based Informational Retrieval
## Creating an IR System for a Local News Corpus

This project was originally created for the CENG596 Information Retrieval Term Project.

We built an Information Retrieval system that can work on any local text corpus. We used <a href="https://trec.nist.gov/data/reuters/reuters.html">Reuter’s TRC2 corpus</a> for testing and designed our system with <a href="https://lucene.apache.org/">Apache Lucene</a> to preprocess the data and create indices that allow us to perform Boolean queries, phrase queries, and wildcard queries with spellcheck support. For query parsing, we setup our system to take a query, perform a Boolean retrieval of all the relevant documents, and then rank them using an advanced version of the tf-idf vector model ranking system. Finally, the system returns top 10 ranked articles to the user and is wrapped in a Java based user interface. Additionally, we performed evaluations and generated various metrics.
