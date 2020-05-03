/*
TO-DO: Make it so that we can CHOOSE the FIELD to search in. Very Easy fix, leave it for Raheem.
 */

package Searcher;

import java.io.IOException;

import Constants.LuceneConstants;
import org.apache.lucene.document.Document;
import org.apache.lucene.queryparser.classic.ParseException;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;

public class SearcherMain {

    static String standard = "src/main/resources/StandardIndex";
    static String stopwords = "src/main/resources/StopWordsIndex";

    Searcher searcher;

    public static void main(String[] args) {
        SearcherMain tester;
        try {
            tester = new SearcherMain();
            tester.search("Nokia"); // Choose Search Query here. Choose Field below.
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ParseException e) {
            e.printStackTrace();
        }
    }

    private void search(String searchQuery) throws IOException, ParseException {
        searcher = new Searcher(standard);   //Choosing which Index
        long startTime = System.currentTimeMillis();
        TopDocs hits = searcher.search(searchQuery);
        long endTime = System.currentTimeMillis();

        System.out.println(hits.totalHits +
                " documents found. Time :" + (endTime - startTime));
        for(ScoreDoc scoreDoc : hits.scoreDocs) {
            Document doc = searcher.getDocument(scoreDoc);
            System.out.println("Article: "
                    + doc.get(LuceneConstants.HEADER));
        }
    }
}
