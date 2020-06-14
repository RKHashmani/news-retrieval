package Indexer;

import Constants.LuceneConstants;
import org.apache.lucene.document.*;
import org.apache.lucene.index.FieldInvertState;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.search.CollectionStatistics;
import org.apache.lucene.search.TermStatistics;
import org.apache.lucene.search.similarities.BM25Similarity;
import org.apache.lucene.search.similarities.ClassicSimilarity;
import org.apache.lucene.search.similarities.Similarity;
import org.apache.lucene.search.similarities.TFIDFSimilarity;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class Indexer{

    protected IndexWriter writer;
    Similarity similarity;

    public Indexer(String indexDirectoryPath, IndexWriterConfig config) throws IOException {
        Directory indexDirectory = FSDirectory.open(new File(indexDirectoryPath).toPath());

        /*
        // Custom made similarity method. Mimics the ClassicSimilarity, but doesn't give the exact same results.
        // If you decide to use this, make sure to copy paste it in the appropriate location in Searcher.java
        similarity = new TFIDFSimilarity() {
            @Override
            public float tf(float v) {
                return v;
            }

            @Override
            public float idf(long l, long l1) {
                float idf_value = (float) Math.log((l1+1)/(l+1)) + 1; //Uses Log base e (ln)
                return idf_value;
            }

            @Override
            public float lengthNorm(int i) {
                return (float)0.35355338;
            }
        }; // Choose Ranking Method Here. Make sure it matches the one in Searcher.java
         */

        similarity = new ClassicSimilarity(); //Choose Ranking Method here. Make sure it matches the one in Searcher.java
        config.setSimilarity(similarity);
        config.setOpenMode(IndexWriterConfig.OpenMode.CREATE);
        writer = new IndexWriter(indexDirectory, config);
    }

    public void close() throws IOException {
        writer.close();
    }

    private Document getDocument(String [] line, int i) {
        Document document = new Document();
        assert line.length == 3;
        TextField contentField = new TextField(LuceneConstants.CONTENTS, line[2], Field.Store.YES);
        TextField headerField = new TextField(LuceneConstants.HEADER,
                line[1], Field.Store.YES); // Changed from StringField to TextField
        TextField dateField = new TextField(LuceneConstants.DATE,
                line[0],Field.Store.YES);

        IntPoint id = new IntPoint("id", i);
        document.add(id);
        document.add(dateField);
        document.add(headerField);
        document.add(contentField);

        return document;
    }

    private void indexFile(String [] line, int i) throws IOException {
        Document document = getDocument(line, i);
        writer.addDocument(document);
    }

    public int createIndex(String dataDirPath) {
        BufferedReader reader = null;
        int i = 0;
        String nextLine;
        try {
            reader = new BufferedReader(new FileReader(dataDirPath));
            reader.readLine();
            while ((nextLine = reader.readLine()) != null) {
                i++;
                String [] line = new String[3];
                nextLine = nextLine.trim();
                int endIndex = nextLine.indexOf(",");
                String date = nextLine.substring(0, endIndex);
                line[0] = date;
                String [] header_content = nextLine.substring(endIndex + 1).split("\"*\",");
                line[1] = header_content[0];
                line[2] = header_content[1];
                indexFile(line, i);
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        }
        finally {
            try {
                assert reader != null;
                reader.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return i;
    }
}
