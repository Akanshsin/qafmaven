package com.qmetry.qaf.example.steps;

import static com.qmetry.qaf.automation.step.CommonStep.*;

import com.qmetry.qaf.automation.step.QAFTestStep;

import com.qmetry.qaf.automation.ui.webdriver.*;

public class StepsLibrary {

	@QAFTestStep(description = "navigate to search page")
	public static void navigateToSearchPage() throws Exception{
		get("/");
		rejectAllCookies();
		Thread.sleep(5000);
	}

	/**
	 * @param searchTerm
	 *            : search term to be searched
	 */
	@QAFTestStep(description = "search for {0}")
	public static void searchFor(String searchTerm) {
//		QAFWebElement inputField = new WebDriverTestBase().getDriver().findElement("#todo-input");
		sendKeys(searchTerm, "#todo-input");
		sendKeys("\n", "#todo-input");
		sendKeys(searchTerm, "#todo-input");
		sendKeys("\n", "#todo-input");
		sendKeys(searchTerm, "#todo-input");
		sendKeys("\n", "#todo-input");
		sendKeys(searchTerm, "#todo-input");
		sendKeys("\n", "#todo-input");
		sendKeys(searchTerm, "#todo-input");
		sendKeys("\n", "#todo-input");
		try {
			Thread.sleep(5000); // Handle InterruptedException
		} catch (InterruptedException e) {
			Thread.currentThread().interrupt(); // Restore the interrupted status
			System.err.println("Thread was interrupted: " + e.getMessage());
		}
//		sendKeys("ENTER", "");
//		submit("input.search");
	}
//	@QAFTestStep(description = "I should see {0} in {1}")
//	public void verifyTextVisible(String expectedText, String locator) {
//		QAFWebElement todoItem = new WebDriverTestBase().getDriver().findElement(locator);
//		assert todoItem.getText().equals(expectedText) : "Text not found!";
//	}

	/**
	 * In Europe, a cookies popup appears in google before search is available.
	 * It has Reject All button. Once clicked, cookies are rejected and the search page appears.
	 * */
	private static void rejectAllCookies() {
		QAFWebElement rejectAllButton = new QAFExtendedWebElement("reject.all");

		if (rejectAllButton.isPresent()) {
			rejectAllButton.click();
		}
	}
}
