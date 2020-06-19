package Searcher;

import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.control.RadioButton;
import javafx.scene.control.TextField;
import javafx.scene.control.CheckBox;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.Pane;
import javafx.scene.control.Button;

import java.io.IOException;

public class GUIController {
    @FXML private Parent load;
    @FXML private FXMLLoader fxmlLoader;

    @FXML public BorderPane generalLayout;
    @FXML public CheckBox stopWordsInclude;
    @FXML public RadioButton cranfield;
    @FXML public RadioButton reuters;
    @FXML public TextField searchBar;
    @FXML public Button button_search;
    @FXML public Pane resultArea;
    @FXML public CheckBox headers;
    @FXML public CheckBox content;

    public GUIController() {
        fxmlLoader = new FXMLLoader(GUIController.class.getClassLoader().getResource("SearchPage.fxml"));
        fxmlLoader.setController(this);
        try {
            load = fxmlLoader.load();
        }catch (IOException ioe) {
            throw new RuntimeException(ioe);
        }
    }

    @FXML
    public Parent getParent() {
        return load;
    }

}
