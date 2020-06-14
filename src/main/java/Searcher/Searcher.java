package Searcher;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;

import Constants.LuceneConstants;
import org.apache.lucene.analysis.core.WhitespaceAnalyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.index.CorruptIndexException;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.queryparser.classic.ParseException;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.*;
import org.apache.lucene.search.similarities.BM25Similarity;
import org.apache.lucene.search.similarities.ClassicSimilarity;
import org.apache.lucene.search.similarities.Similarity;
import org.apache.lucene.search.similarities.TFIDFSimilarity;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;
import org.apache.lucene.util.Version;

public class Searcher {

    IndexSearcher indexSearcher;
    QueryParser queryParser;
    Query query;
    StandardAnalyzer standardAnalyzer = new StandardAnalyzer(); //Using the standard Analyzer for now
    StandardAnalyzer NoStopWord = new StandardAnalyzer(new FileReader(LuceneConstants.stopWordsDir));
    WhitespaceAnalyzer WhiteSpace = new WhitespaceAnalyzer();
    Similarity similarity;

    public Searcher(String indexDirectoryPath) throws IOException {
        Directory indexDirectory = FSDirectory.open(new File(indexDirectoryPath).toPath());
        IndexReader reader = DirectoryReader.open(indexDirectory);
        indexSearcher = new IndexSearcher(reader);
        similarity = new ClassicSimilarity(); //Choose Ranking Method here. Make sure it matches the one in Indexer.java
        indexSearcher.setSimilarity(similarity);
        //queryParser = new QueryParser(LuceneConstants.CONTENTS, standardAnalyzer);
        queryParser = new QueryParser(LuceneConstants.CONTENTS, NoStopWord);//Choose FIELD here
        //queryParser = new QueryParser(LuceneConstants.CONTENTS, WhiteSpace);
        // Change above's standard Analyzer to match whatever analyzer we use for the index
    }

    public TopDocs search( String searchQuery) throws IOException, ParseException {
        query = queryParser.parse(searchQuery);
        return indexSearcher.search(query, LuceneConstants.MAX_SEARCH);
    }

    public Explanation explanation (int docID)throws IOException, ParseException{
        Explanation explain = indexSearcher.explain(query,docID);
        return explain;
    }

    public Document getDocument(ScoreDoc scoreDoc) throws IOException {
        return indexSearcher.doc(scoreDoc.doc);
    }

    public CollectionStatistics getStats() throws IOException {
        return indexSearcher.collectionStatistics(LuceneConstants.CONTENTS);
    }
}
