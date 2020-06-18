package Searcher;

import Constants.LuceneConstants;
import javafx.application.Application;
import javafx.application.Platform;
import javafx.scene.Scene;
import javafx.scene.control.Alert;
import javafx.scene.text.Text;
import javafx.stage.Stage;
import org.apache.lucene.queryparser.classic.ParseException;

import java.io.IOException;

public class SearchApplication extends Application {

    private final int windowWidth = 1200;
    private final int windowHeight = 800;

    @Override
    public void start(Stage stage) {
        GUIController guiController = new GUIController();
        Scene scene = new Scene(guiController.getParent(), windowWidth, windowHeight);
        guiController.button_search.setOnAction(e -> {
            if (guiController.searchBar.getText() == null || guiController.searchBar.getText().trim().isEmpty()) {
                Alert alert = new Alert(Alert.AlertType.ERROR);
                alert.setTitle("Search bar is empty.");
                alert.setHeaderText("Search bar is empty.");
                alert.setContentText("Please provide some query into the search bar.");
                alert.showAndWait();
            } else {
                if (guiController.stopWordsInclude.isSelected()){
                    if (guiController.cranfield.isSelected()) {
                        performSearch(guiController, LuceneConstants.TestIndexDir);
                    } else if (guiController.reuters.isSelected()){
                        performSearch(guiController, LuceneConstants.StandardIndexDir);
                    }
                    else {
                        Alert alert = new Alert(Alert.AlertType.ERROR);
                        alert.setTitle("Corpus is not chosen.");
                        alert.setHeaderText("Corpus is not chosen.");
                        alert.setContentText("Please choose one of the corpora above.");
                        alert.showAndWait();
                    }
                } else {
                    if (guiController.cranfield.isSelected()) {
                        performSearch(guiController, LuceneConstants.TestStopWordsIndexDir);
                    } else if (guiController.reuters.isSelected()){
                        performSearch(guiController, LuceneConstants.StopWordsIndexDir);
                    } else {
                        Alert alert = new Alert(Alert.AlertType.ERROR);
                        alert.setTitle("Corpus is not chosen.");
                        alert.setHeaderText("Corpus is not chosen.");
                        alert.setContentText("Please choose one of the corpora above.");
                        alert.showAndWait();
                    }
                }
            }
        });
        stage.setOnCloseRequest((ae) -> {
            Platform.exit();
            System.exit(0);
        });
        stage.setScene(scene);
        stage.show();
    }

    @Override
    public void stop() {
        Platform.exit();
    }

    private void performSearch(GUIController guiController, String indexDir) {
        SearcherMain searcherMain = new SearcherMain(indexDir);
        String searchQuery = guiController.searchBar.getText().trim();
        try {
            guiController.resultArea.getChildren().clear();
            String results = searcherMain.search(searchQuery);
            Text text = new Text(results);
            guiController.resultArea.getChildren().add(text);
        } catch (IOException | ParseException e) {
            e.printStackTrace();
        }
    }
}
