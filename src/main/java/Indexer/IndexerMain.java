package Indexer;

import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.index.IndexWriterConfig;

import java.io.FileReader;
import java.io.IOException;

public class IndexerMain {

    private static void makeIndex(IndexWriterConfig config, String indexDir) throws IOException {
        Indexer indexer = new Indexer(indexDir, config);
        int numIndexed;
        long startTime = System.currentTimeMillis();
        numIndexed = indexer.createIndex(dataDir);
        long endTime = System.currentTimeMillis();
        indexer.close();
        System.out.println(numIndexed+" File indexed, time taken: "
                +(endTime-startTime)+" ms");
    }

    static String standard = "src/main/resources/StandardIndex";
    static String stopwords = "src/main/resources/StopWordsIndex";
    static String dataDir = "src/main/resources/reuters/trc2/headlines-docs.csv";
    static String stopWordsDir = "src/main/resources/stopwords.txt";

    public static void main(String[] args) throws IOException {
        makeIndex(new IndexWriterConfig(), standard); //no stop words
        makeIndex(new IndexWriterConfig(new StandardAnalyzer(new FileReader(stopWordsDir))), stopwords); // with given stop words
    }
}
