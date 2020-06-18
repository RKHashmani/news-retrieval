package Indexer;

import Constants.LuceneConstants;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.document.IntPoint;
import org.apache.lucene.document.TextField;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.search.similarities.ClassicSimilarity;
import org.apache.lucene.search.similarities.Similarity;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;

import java.io.*;
import java.util.Scanner;

public class TestIndexer {

    private IndexWriter writer;
    Similarity similarity;

    public TestIndexer(String indexDirectoryPath, IndexWriterConfig config) throws IOException {
        Directory indexDirectory = FSDirectory.open(new File(indexDirectoryPath).toPath());
        similarity = new ClassicSimilarity(); //Choose Ranking Method here. Make sure it matches the one in Searcher.java
        config.setSimilarity(similarity);
        config.setOpenMode(IndexWriterConfig.OpenMode.CREATE);
        writer = new IndexWriter(indexDirectory, config);
    }

    public void close() throws IOException {
        writer.close();
    }

    private Document getDocument(File body, File metadata, int i) throws FileNotFoundException {
        Document document = new Document();
        Scanner bodyReader = new Scanner(body);
        String bodyContent = "";
        while (bodyReader.hasNextLine()) {
            bodyContent += bodyReader.nextLine();
        }

        Scanner headerReader = new Scanner(metadata);
        String metadataContent = "";
        while (headerReader.hasNextLine()) {
            metadataContent += headerReader.nextLine();
        }
        String [] metadataSplit = metadataContent.split(" \\.");
        TextField headerField = new TextField(LuceneConstants.HEADER, metadataSplit[0], Field.Store.YES);
        TextField contentField = new TextField(LuceneConstants.CONTENTS, bodyContent, Field.Store.YES);
        TextField idField = new TextField("id", i + "", Field.Store.YES);
        document.add(idField);
        document.add(contentField);
        document.add(headerField);

        return document;
    }

    private void indexFile(File body, File metadata, int i) throws IOException {
        Document document = getDocument(body, metadata, i);
        writer.addDocument(document);
    }

    public int createIndex(String dataDirPath) {
        int numIndexed = 0;
        try {
            File [] listOfFiles = new File(dataDirPath).listFiles();
            for (int j = 1; j <= 1400; j++) {
                try {
                    File [] files = new File(dataDirPath + "/" + j).listFiles();
                    indexFile(files[0], files[1], j);
                    numIndexed++;
                }
                catch (NullPointerException ignored) {
                }
            }
        }
        catch (Exception e) {
            e.printStackTrace();
        }
        return numIndexed;
    }
}
