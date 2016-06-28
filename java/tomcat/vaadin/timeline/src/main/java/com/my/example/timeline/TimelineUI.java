package com.my.example.timeline;

import com.vaadin.annotations.Title;
import com.vaadin.data.Container.Filter;
import com.vaadin.data.Item;
import com.vaadin.data.Property;
import com.vaadin.data.Property.ValueChangeEvent;
import com.vaadin.data.fieldgroup.FieldGroup;
import com.vaadin.data.util.IndexedContainer;
import com.vaadin.event.FieldEvents.TextChangeEvent;
import com.vaadin.event.FieldEvents.TextChangeListener;
import com.vaadin.server.VaadinRequest;
import com.vaadin.ui.AbstractTextField.TextChangeEventMode;
import com.vaadin.ui.Button;
import com.vaadin.ui.Button.ClickEvent;
import com.vaadin.ui.Button.ClickListener;
import com.vaadin.ui.FormLayout;
import com.vaadin.ui.HorizontalLayout;
import com.vaadin.ui.HorizontalSplitPanel;
import com.vaadin.ui.Table;
import com.vaadin.ui.TextField;
import com.vaadin.ui.RichTextArea;
import com.vaadin.ui.Label;
import com.vaadin.ui.UI;
import com.vaadin.ui.VerticalLayout;
import java.util.ArrayList;
import java.util.List;

/* 
 * Main class.
 * 
 * This will implement the base system, and import all the diferent pages. 
 * 
 */
@Title("Timeline")
public class TimelineUI extends UI {

	private static final String XNAME = "X";
	private static final String YNAME = "Y";

	/* User interface components are stored in session. */
	private TextField XField = new TextField();
	private TextField YField = new TextField();
	private Button addButton = new Button("Add");
	private RichTextArea logArea = new RichTextArea();
	private FormLayout logLayout = new FormLayout();

    private Label      XLabel = new Label(XNAME);
    private Label      YLabel = new Label(YNAME);


    private List<Integer> X;
    private List<Integer> Y;



	/*
	 * After UI class is created, init() is executed. You should build and wire
	 * up your user interface here.
	 */
	protected void init(VaadinRequest request) {
		initData();
		initLayout();
		initAddButtons();
	}


    /*
     * initializa all internal data structures
     */
    protected void initData() {
       X = new ArrayList<Integer>();
       Y = new ArrayList<Integer>();
     }

	/*
	 * In this example layouts are programmed in Java. You may choose use a
	 * visual editor, CSS or HTML templates for layout instead.
	 */
	private void initLayout() {

		/* Root of the user interface component tree is set */
		HorizontalSplitPanel splitPanel = new HorizontalSplitPanel();
		setContent(splitPanel);

		/* Build the component tree */
		VerticalLayout leftLayout = new VerticalLayout();
		splitPanel.addComponent(leftLayout);
		splitPanel.addComponent(logLayout);
		HorizontalLayout bottomLeftLayout = new HorizontalLayout();
		leftLayout.addComponent(bottomLeftLayout);
		bottomLeftLayout.addComponent(XLabel);
		bottomLeftLayout.addComponent(XField);
		bottomLeftLayout.addComponent(YLabel);
		bottomLeftLayout.addComponent(YField);
		bottomLeftLayout.addComponent(addButton);

		/* Set the contents in the left of the split panel to use all the space */
		leftLayout.setSizeFull();

		bottomLeftLayout.setWidth("100%");

		/* Put a little margin around the fields in the right side editor */
        logLayout.addComponent(logArea);
		logLayout.setMargin(true);
		logLayout.setVisible(true);
	}


    private void historyAdd(String x, String y) {
                    Y.add(Integer.valueOf(y, 10));
                    X.add(Integer.valueOf(x, 10));
    }


	private void initAddButtons() {
		addButton.addClickListener(new ClickListener() {
			public void buttonClick(ClickEvent event) {

                String x = XField.getValue();
                String y = YField.getValue();
                if ( (x.length()>0) && (y.length()>0 ) ) {
                    logArea.setValue(logArea.getValue() + " " + x + ":" +y);
                    XField.setValue("");
                    YField.setValue("");
                    historyAdd(x,y);
                }

				// TODO, add to the main list and clean....
			}
		});

	}



}
