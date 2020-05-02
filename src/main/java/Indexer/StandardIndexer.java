package Indexer;

import Constants.LuceneConstants;
import org.apache.lucene.document.*;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class StandardIndexer {

    private final IndexWriter writer;

    public StandardIndexer(String indexDirectoryPath) throws IOException {
        Directory indexDirectory = FSDirectory.open(new File(indexDirectoryPath).toPath());
        writer = new IndexWriter(indexDirectory, new IndexWriterConfig());
    }

    public void close() throws IOException {
        writer.close();
    }

    private Document getDocument(String [] line, int i) {
        Document document = new Document();
        assert line.length == 3;
        TextField contentField = new TextField(LuceneConstants.CONTENTS, line[2], Field.Store.YES);
        StringField headerField = new StringField(LuceneConstants.HEADER,
                line[1], Field.Store.YES);
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
        System.out.println("Line " + i + " indexed.");
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
