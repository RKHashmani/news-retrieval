package Indexer;

import Constants.LuceneConstants;
import org.apache.lucene.document.Document;
import org.apache.lucene.document.Field;
import org.apache.lucene.document.IntPoint;
import org.apache.lucene.document.TextField;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;

import java.io.*;
import java.util.Scanner;

public class TestIndexer {

    private IndexWriter writer;

    public TestIndexer(String indexDirectoryPath, IndexWriterConfig config) throws IOException {
        Directory indexDirectory = FSDirectory.open(new File(indexDirectoryPath).toPath());
        writer = new IndexWriter(indexDirectory, config);
    }

    public void close() throws IOException {
        writer.close();
    }

    private Document getDocument(File body, int i) throws FileNotFoundException {
        Document document = new Document();
        Scanner bodyReader = new Scanner(body);
        String bodyContent = "";
        while (bodyReader.hasNextLine()) {
            bodyContent += bodyReader.nextLine();
        }
        TextField contentField = new TextField(LuceneConstants.CONTENTS, bodyContent, Field.Store.YES);
        IntPoint id = new IntPoint("id", i);
        document.add(id);
        document.add(contentField);

        return document;
    }

    private void indexFile(File body, int i) throws IOException {
        Document document = getDocument(body, i);
        writer.addDocument(document);
    }

    public int createIndex(String dataDirPath) {
        int numIndexed = 0;
        try {
            File [] listOfFiles = new File(dataDirPath).listFiles();
            for (int j = 1; j <= 1400; j++) {
                try {
                    File [] files = new File(dataDirPath + "/" + j).listFiles();
                    indexFile(files[0], j);
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
