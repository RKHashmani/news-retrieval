package Indexer;

import Constants.LuceneConstants;
import org.apache.lucene.index.IndexWriterConfig;

import java.io.IOException;

public class TestIndexerMain {
    public static String dataDir = LuceneConstants.testDir;

    private static void makeIndex(IndexWriterConfig config, String indexDir) throws IOException {
        TestIndexer indexer = new TestIndexer(indexDir, config);
        int numIndexed;
        long startTime = System.currentTimeMillis();
        numIndexed = indexer.createIndex(dataDir);
        long endTime = System.currentTimeMillis();
        indexer.close();
        System.out.println(numIndexed + " File indexed, time taken: "
                + (endTime-startTime) + " ms");
    }

    public static void main(String[] args) throws IOException {
        makeIndex(new IndexWriterConfig(), LuceneConstants.TestIndexDir);
    }
}