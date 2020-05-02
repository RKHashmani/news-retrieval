package Indexer;

import Constants.LuceneConstants;
import org.apache.lucene.document.*;
import org.apache.lucene.index.IndexWriter;
import org.apache.lucene.index.IndexWriterConfig;
import org.apache.lucene.store.Directory;
import org.apache.lucene.store.FSDirectory;

import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import com.opencsv.CSVReader;

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
        CSVReader reader = null;
        int i = 0;
        String [] nextLine;
        try {
            reader = new CSVReader(new FileReader(dataDirPath));
            reader.readNext(); // omit column names
            while ((nextLine = reader.readNext()) != null) {
                i++;
                System.out.println(i);
                indexFile(nextLine, i);
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
