package Indexer;

import Constants.LuceneConstants;
import org.apache.lucene.analysis.core.WhitespaceAnalyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.index.IndexWriterConfig;

import java.io.FileReader;
import java.io.IOException;

public class IndexerMain {

    public static String dataDir = LuceneConstants.dataDir;

    private static void makeIndex(IndexWriterConfig config, String indexDir) throws IOException {
        Indexer indexer = new Indexer(indexDir, config);
        int numIndexed;
        long startTime = System.currentTimeMillis();
        numIndexed = indexer.createIndex(dataDir);
        long endTime = System.currentTimeMillis();
        indexer.close();
        System.out.println(numIndexed + " File indexed, time taken: "
                + (endTime-startTime) + " ms");
    }

    public static void main(String[] args) throws IOException {
        makeIndex(new IndexWriterConfig(), LuceneConstants.StandardIndexDir); //no stop words
        makeIndex(new IndexWriterConfig(new StandardAnalyzer(new FileReader(LuceneConstants.stopWordsDir))), LuceneConstants.StopWordsIndexDir); // without given stop words
        makeIndex(new IndexWriterConfig(new WhitespaceAnalyzer()), LuceneConstants.WhiteSpaceIndexDir);
    }
}
