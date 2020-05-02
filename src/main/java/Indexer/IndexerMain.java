package Indexer;

import java.io.IOException;

public class IndexerMain {

    static String indexDir = "src/main/resources/StandardIndex";
    static String dataDir = "src/main/resources/reuters/trc2/headlines-docs.csv";

    public static void main(String[] args) throws IOException {
        StandardIndexer indexer = new StandardIndexer(indexDir);
        int numIndexed;
        long startTime = System.currentTimeMillis();
        numIndexed = indexer.createIndex(dataDir);
        long endTime = System.currentTimeMillis();
        indexer.close();
        System.out.println(numIndexed+" File indexed, time taken: "
                +(endTime-startTime)+" ms");
    }
}
